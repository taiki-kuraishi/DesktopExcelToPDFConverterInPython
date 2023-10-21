import eel
import io
import sys

eel.init('web')

@eel.expose
def receiveFile(file_name, file_contents):
    with io.BytesIO(file_contents) as f:
        contents = f.read().decode('utf-8')
        print(contents)

def onCloseWindow(page, sockets):
    print(page + 'が閉じられました。プログラムを終了します。')
    sys.exit()

def main():
    eel.init('web')
    eel.start('index.html',mode='default', size=(700, 700), close_callback=onCloseWindow)

if __name__ == '__main__':
    main()