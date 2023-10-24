import webview


class Api:
    def printPath(self, path):
        print(path)

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


api = Api()
window = webview.create_window(
    "JS to Python", url="./web/index.html", js_api=api)
webview.start(debug=True)
