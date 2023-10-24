import webview
import os
import openpyxl

# ファイルが存在するか確認
def isValidFilePath(path):
    return os.path.isfile(path)

#Excelファイルを開く
def openExcel(path):
    # open file
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    cell = ws['A1']

    # シートを閉じる
    wb.close()
    return cell.value


class Api:
    def choseFile(self):
        global window
        # Folder dialog
        # result = window.create_file_dialog(
        #     webview.FOLDER_DIALOG, allow_multiple=True)
        # File dialog
        result = window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True)
        print(result)
        return result

    def convertToPDF(self, path):
        # ファイルが存在するか確認
        if not isValidFilePath(path):
            return 1

        # open file
        cell = openExcel(path)
        print(cell)
        return 0


api = Api()
window = webview.create_window(
    "JS to Python", url="./web/index.html", js_api=api)
webview.start(http_server=True,debug=True)
