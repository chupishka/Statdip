from symtable import Function
from tkinter import *
import tkinter as tk
from tkinter import ttk

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
        new_table = Book(self.edit_raws.get(),self.edit_col.get())
        self.root.destroy()
        del self




class Book(Tk):
    def __init__(self,rows,col):
        super().__init__()

        self.geometry("500x500")

        frame_table = ttk.Frame(self,borderwidth=3)
        table_menu = Menu(self)
        file_menu = Menu(self)
        file_menu.add_cascade(label="New book",command= lambda x = self:Book.new_book(self))
        file_menu.add_cascade(label="Save book")

        table_menu.add_cascade(label="File",menu=file_menu)
        table_menu.add_cascade(label="Edit")
        table_menu.add_cascade(label="Functions")
        self.config(menu = table_menu)
        self.columns = []
        self.data = [[]]
        for i in range(int(rows)+1):
            for j in range(int(col)+1):
                if i==0 and j== 0:
                    continue
                if i==0:
                    lbl = ttk.Entry(frame_table,text = "Var"+str(j),justify=RIGHT)
                    lbl.insert(0,"Var"+str(j))
                    lbl.grid(row = i,column=j)
                elif j==0:
                    lbl = ttk.Label(frame_table,text = str(i),justify=RIGHT)
                    lbl.grid(row = i,column=j)
                else:
                    entry = ttk.Entry(frame_table,text=str(i)+str(j),justify=RIGHT)
                    entry.grid(row = i,column=j)
        frame_table.pack(anchor = "nw")

    def new_book(self):

        new_create = Create()

    def function1(self):
        functiontk = Tk()


# class Function1(Tk):
#     def __init__(self,vars):
#         super().__init__()





c = Create()





