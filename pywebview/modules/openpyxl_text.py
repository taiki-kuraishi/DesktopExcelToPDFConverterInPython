import openpyxl

path = '/Users/gyodon/Desktop/text/Book1.xlsx'

wb = openpyxl.load_workbook(path)
ws = wb.active
cell = ws['A1']

# シートを閉じる
wb.close()

print(cell.value)