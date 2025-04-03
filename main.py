from tkinter import *
import tkinter as tk
from tkinter import ttk
from Table import Table

# def create():
#
#     labl = ttk.Label(text="jopa")
#     labl.pack()
#     root.mainloop()
# root = Tk()
# root.geometry("500x200")
# lbl1 = ttk.Label(text="Введите кол-во столбцов:")
# edit_col = ttk.Entry()
# lbl2 = ttk.Label(text="Введите кол-во строк:")
#
# edit_raws = ttk.Entry()
# btn_create = ttk.Button(text="Создать",command=create)
# lbl1.place(x="10",y="10")
# edit_col.place(x = "200",y="10")
# lbl2.place(x="10",y="40")
# edit_raws.place(x = "200",y="40")
# btn_create.pack(anchor = "s",side = 'bottom',pady = "20")
# root.mainloop()
class Create:
    def __init__(self):
        x = self
        self.root = Tk()
        self.root.geometry("500x200")
        lbl1 = ttk.Label(text="Введите кол-во столбцов:")
        self.edit_col = ttk.Entry()
        lbl2 = ttk.Label(text="Введите кол-во строк:")
        self.edit_raws = ttk.Entry()
        btn_create = ttk.Button(text="Создать",command=lambda self=x:Create.create_table(self))
        lbl1.place(x="10", y="10")
        self.edit_col.place(x="200", y="10")
        lbl2.place(x="10", y="40")
        self.edit_raws.place(x="200", y="40")
        btn_create.pack(anchor="s", side='bottom', pady="20")
        self.root.mainloop()
    def create_table(self):
        new_table = Table(self.edit_raws.get(),self.edit_col.get())
        self.root.destroy()



c = Create()





