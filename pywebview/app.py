import webview,os
import xlwings as xw

# ファイルが存在するか確認
#fileの場合0, folderの場合1, 存在しない場合2
def isValidPath(path):
    if os.path.isfile(path):
        return 0
    elif os.path.isdir(path):
        return 1
    else:
        return 2

#Excelファイルを開く
def openExcel(path):
    excel_file_name = path.split('/')[-1]
    savefile_path = "pywebview/web/img" #出力先のパスを設定

    App = xw.App() #単一のアプリ実行環境管理

    #ExcelファイルをPDFファイルに変換
    pdf_file_name = excel_file_name.replace(".xlsx", ".pdf")
    wb = xw.Book(path)
    wb.to_pdf(path= savefile_path + '/' + pdf_file_name, include=None, exclude=None, exclude_start_string='#', show=False)
    wb.close()

    App.quit() #アプリ実行環境を終了


class Api:
    def choseFile(self):
        global window
        # Folder dialog
        # result = window.create_file_dialog(
        #     webview.FOLDER_DIALOG, allow_multiple=True)
        # File dialog
        result = window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True)
        print(type(result))
        print(result)
        return result

    #excelファイルをPDFに変換する
    #file not found 1, folder not found 2, success 0
    def main(self, paths):
        status = 0
        print(paths)

        # pathが複数か単数かで処理を分ける
        if ',' in paths:
            path_list = paths.split(',')
        else:
            #pathがfileかfolderか存在するか確認
            status = isValidPath(paths)
            #fileの場合
            if status == 0:
                openExcel(paths)
            # #folderの場合
            # elif status == 1:
            # #存在しない場合
            # elif status == 2:
            #     return 1

        return 0


api = Api()
window = webview.create_window(
    "JS to Python", url="./web/index.html", js_api=api)
webview.start(http_server=True,debug=True)
