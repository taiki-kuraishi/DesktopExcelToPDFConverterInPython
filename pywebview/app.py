import webview
import os
import xlwings as xw

TMP_FOLDER_PATH = "pywebview/web/img"  # 出力先のパスを設定'


def is_valid_path(path):  # pathがfileかfolderか存在するか確認
    """
    pathがfileの場合は0を返す
    pathがfolderの場合は1を返す
    それ以外の場合は2を返す
    """
    if os.path.isfile(path):
        return 0
    elif os.path.isdir(path):
        return 1
    else:
        return 2


def convert_excel_to_pdf(path):  # excelファイルからpdfファイルを作成する
    global TMP_FOLDER_PATH
    excel_file_name = path.split('/')[-1]
    pdf_file_name = excel_file_name.replace(".xlsx", ".pdf")

    App = xw.App()  # 単一のアプリ実行環境管理

    # ExcelファイルをPDFファイルに変換
    wb = xw.Book(path)
    wb.to_pdf(path=TMP_FOLDER_PATH + '/' + pdf_file_name, include=None,
              exclude=None, exclude_start_string='#', show=False)
    wb.close()

    App.quit()  # アプリ実行環境を終了


def get_excel_files(folder_path):  # folder内のexcelファイルのpathを取得
    excel_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            excel_files.append(os.path.join(folder_path, file))
    return excel_files


def on_closing():  # windowを閉じている最中に呼ばれる
    print("on_closing")


def on_closed():  # windowが閉じた時に呼ばれる
    # imgの中のpdfを全て削除
    for file in os.listdir(TMP_FOLDER_PATH):
        if file.endswith(".pdf"):
            os.remove(os.path.join(TMP_FOLDER_PATH, file))
    print("on_closed")


class Api:  # Jsから呼ばれる関数を定義
    def showFileDialog(self):  # fileダイアログを表示
        """
        return
        filepathをタプルで返す
        """
        global window
        result = window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True, file_types=('Excel Files (*.xlsx)',))
        return result

    def showFolderDialog(self):  # folderダイアログを表示
        """
        return
        filepathをタプルで返す
        """
        global window
        result = window.create_file_dialog(webview.FOLDER_DIALOG)
        return result

    # 入力されたpathを受け取り、excelのpathのリストを返す
    # file not found 1, success 0
    def submitPath(self, paths):
        status = 0
        path_list = []
        # num_files = 0 #pathに含まれるfileの数
        print(paths)

        # pathが複数か単数かで処理を分ける
        if ',' in paths:
            path_list = paths.split(',')
            # 全てのpathがfileであることを確認する
            for path in path_list:
                status = is_valid_path(path)
                if status != 0:
                    return [1]
            # # 全てのpathを変換する
            # for path in path_list:
            #     convert_excel_to_pdf(path)
        else:
            # pathがfileかfolderか存在するか確認
            status = is_valid_path(paths)
            if status == 0:  # fileの場合
                # convert_excel_to_pdf(paths)
                path_list.append(paths)
            elif status == 1:  # folderの場合
                path_list = get_excel_files(paths)
                # for excel_path in path_list:
                #     convert_excel_to_pdf(excel_path)
            elif status == 2:  # 存在しない場合
                return [1]

        return path_list


api = Api()
window = webview.create_window(
    "DesktopExcelToPDFConverterInPython", url="./web/index.html", js_api=api)
window.events.closed += on_closed
window.events.closing += on_closing
webview.start(http_server=True, debug=True)
