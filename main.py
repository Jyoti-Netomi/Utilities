import pandas as pd


read_file = pd.read_excel (r'/Users/netomi/Downloads/Apption_Lab_TCs.xlsx', sheet_name=None)
sheets = read_file.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(r'/Users/netomi/Downloads/Apption_Lab_TCs.xlsx', sheet_name=sheet_name)
    sheet.to_csv("data/%s.csv" % sheet_name, index=False)

#read_file.to_csv (r'/Users/netomi/PycharmProjects/Utilities/data/test.csv', index = None, header=True)



