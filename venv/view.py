from tkinter import filedialog
from tkinter import *
from rename import Renaming

def get_folder():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def get_file():
    global file_path
    filename = filedialog.askopenfilename( filetypes=(("CSV files", "*.csv"), ) )
    file_path.set(filename)

def rename():
    global msg
    a = Renaming()
    global folder_path
    a.get_path(folder_path.get())
    a.get_path_csv(file_path.get())
    try:
        a.rename()
        msg.set('Переименование файлов завершено успешно!')
    except:
        msg.set('Возникла непредвиденная ошибка!')

root = Tk()
root.title('LIDIA - поточный переименовыватель PDF файлов')
root.geometry(f'500x300+500+200') # ширина=500, высота=400, x=300, y=200
root.resizable(False, False) # размер окна может быть изменён только по горизонтали

folder_path = StringVar()
file_path = StringVar()
folder_path.set('Выберите папку с файлами для переименовывания')
file_path.set('Выберите scv файл с именами файлов')

lbl1 = Label(master=root, width=50, height=5, textvariable=folder_path)
lbl1.grid(row=0, column=1)

buttonB1 = Button(text="Выберите папку", command=get_folder)
buttonB1.grid(row=0, column=2)

lbl2 = Label(master=root, width=50, height=5, textvariable=file_path)
lbl2.grid(row=1, column=1)

buttonB2 = Button(text="Выберите файл", command=get_file)
buttonB2.grid(row=1, column=2)

buttonB3 = Button(text="Переименовать файлы", command=rename)
buttonB3.grid(row=2, column=1)

msg = StringVar()

lbl3 = Label(master=root, width=50, height=5, fg='red', textvariable=msg)
lbl3.grid(row=3, column=1)

root.mainloop()
