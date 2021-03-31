import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from pathlib import Path

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='cyan', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='cyan')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def convertToCSV():

    import_file_path = filedialog.askopenfilename()
    #print(os.path.basename(import_file_path))

    result = Path(import_file_path).stem

    read_file = pd.read_excel(import_file_path, sheet_name=None)

    sheets = read_file.keys()

    for sheet_name in sheets:
        sheet = pd.read_excel(import_file_path, sheet_name=sheet_name)
        sheet.to_csv("data/%s.csv" % sheet_name, index=False)
        #sheet.to_csv("data/{result}/%s.csv"  % sheet_name, index=False)


saveAsButton_CSV = tk.Button(text='Convert Excel to CSV', command=convertToCSV, bg='green', fg='black',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='black',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()