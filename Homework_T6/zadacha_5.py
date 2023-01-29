import pandas as pd
csv = pd.read_csv('my.csv')
excelWriter = pd.ExcelWriter('new_exel.xlsx')
csv.to_excel(excelWriter)
excelWriter.save()