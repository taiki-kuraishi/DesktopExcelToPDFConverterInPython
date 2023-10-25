import glob, xlwings as xw

path= '/Users/gyodon/Documents/GitHub/DesktopExcelToPDFConverterInPython/pywebview/web/img/データベース仕様.xlsx'
file_name = path.split('/')[-1]
savefile_path = "/Users/gyodon/Documents/GitHub/DesktopExcelToPDFConverterInPython/pywebview/web/img" #出力先のパスを設定

App = xw.App() #単一のアプリ実行環境管理

#ExcelファイルをPDFファイルに変換
filename = file_name.replace(".xlsx", ".pdf")
wb = xw.Book(path)
wb.to_pdf(path= savefile_path +'/' + filename, include=None, exclude=None, exclude_start_string='#', show=False)
wb.close()

App.quit() #アプリ実行環境を終了