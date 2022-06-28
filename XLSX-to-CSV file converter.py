excel_file = '/content/Sample_Data - Python Assignment.xlsx'
all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv("/content/Sample_Data-Python Assignment/%s.csv" % sheet_name, index=False)