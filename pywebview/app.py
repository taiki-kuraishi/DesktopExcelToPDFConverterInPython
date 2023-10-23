import webview


class Api:
    def add(self, a, b):
        print("Python")
        return a+b

    def printPath(self, path):
        print(path)

    def choseFile(self):
        global window
        result = window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True)
        print(result)
        return True


api = Api()
window = webview.create_window(
    "JS to Python", url="./web/index.html", js_api=api)
webview.start(debug=True)
