from openpyxl import Workbook

HEADERS_RESULT_TABLE = [1, 1, 1, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5]

 # Добавление заголовков в таблицу excel
wb = Workbook()
ws = wb.active
ws.append(HEADERS_RESULT_TABLE) 
ws.append(HEADERS_RESULT_TABLE) 
wb.save('Parsing/Venchur_fonds/result.xlsx')



add_row_to_table = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]



ws.append(add_row_to_table) 
wb.save('Parsing/Venchur_fonds/result.xlsx')
wb.close()