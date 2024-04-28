import openpyxl

filename=r"C:\Users\admin\Desktop\vivek.xlsx"
my_workbook=openpyxl.load_workbook(filename)
my_active_sheet=my_workbook.active

my_active_sheet.cell(row=2, column=3).value="Passed"

my_workbook.save(filename)