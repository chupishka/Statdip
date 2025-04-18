from email.policy import default
from symtable import Function
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib as plt
from tkinter import filedialog
import numpy as np


class Create:
    def __init__(self):
        x = self
        self.root = Tk()
        self.root.title("Создание")

        icon = PhotoImage(file="img/menu_book_37dp_000000_FILL0_wght400_GRAD0_opsz40.png")
        self.root.iconphoto(False,icon)
        self.root.geometry("500x300")
        lbl = ttk.Label(text="Введите название новой книги:")
        self.edit_name = ttk.Entry()
        lbl1 = ttk.Label(text="Введите кол-во столбцов:")
        self.edit_col = ttk.Entry()
        lbl2 = ttk.Label(text="Введите кол-во строк:")
        self.edit_raws = ttk.Entry()
        btn_create = ttk.Button(text="Создать",command=lambda self=x:Create.create_table(self))
        lbl.place(x="10", y="10")
        self.edit_name.place(x="200", y="10")
        lbl1.place(x="10", y="40")
        self.edit_col.place(x="200", y="40")
        lbl2.place(x="10", y="70")
        self.edit_raws.place(x="200", y="70")
        btn_create.pack(anchor="s", side='bottom', pady="20")
        self.root.mainloop()
    def create_table(self):
        new_table = Book(self.edit_raws.get(),self.edit_col.get(),self.edit_name.get())
        self.root.destroy()
        del self




class Book(Tk):
    def __init__(self,rows,col,name,table = None,upload = False):
        super().__init__()
        self.canv = tk.Canvas(self)

        self.geometry("700x700")
        self.title(name)


        self.canv.pack(side="left", fill="both", expand=True)
        
        
        icon1 = PhotoImage(master=self,file="img/book_37dp_000000_FILL0_wght400_GRAD0_opsz40.png")
        self.iconphoto(False, icon1)

        frame_table = ttk.Frame(self.canv,borderwidth=3)

        frame_table.bind("<Configure>", lambda e: self.canv.configure(scrollregion=self.canv.bbox("all")))

        self.canv.create_window((0,0),window=frame_table,anchor="nw")
        table_menu = Menu(self)
        file_menu = Menu(self)
        func_menu = Menu(self)

        
        func_menu.add_cascade(label="Function1",command= lambda x = self:Book.function1(self))
        file_menu.add_cascade(label="New book",command= lambda x = self:Book.new_book(self))
        file_menu.add_cascade(label="Save book",command= lambda x = self:Book.excel_save(self))
        file_menu.add_cascade(label="Download book",command= lambda x = self:Book.excel_open(self))

        table_menu.add_cascade(label="File",menu=file_menu)
        table_menu.add_cascade(label="Edit")
        table_menu.add_cascade(label="Functions",menu=func_menu)
        self.config(menu = table_menu)
        self.columns = []
        self.data = []
        if not upload:
            for i in range(int(col)+1):
                dat = []
                for j in range(int(rows)+1):
                    if i==0 and j== 0:
                        continue
                    if j==0:
                        entry = ttk.Entry(frame_table,text = "Var"+str(i),justify=RIGHT)
                        entry.insert(0,"Var"+str(i))
                        entry.grid(row = j,column=i)
                        dat.append(entry)
                    elif i==0:
                        lbl = ttk.Label(frame_table,text = str(j),justify=RIGHT)
                        lbl.grid(row = j,column=i)
                    else:
                        entry = ttk.Entry(frame_table,text=str(i)+str(j),justify=RIGHT)
                        entry.grid(row = j,column=i)

                        dat.append(entry)
                if i != 0:
                    self.data.append(dat)
        else:
            dd = np.array(table)
            vars = table.columns[1:]
            for i in range(int(col)+1):
                dat = []
                for j in range(int(rows)+1):
                    if i==0 and j== 0:
                        continue
                    if j==0:
                        entry = ttk.Entry(frame_table,text = "Var"+str(i),justify=RIGHT)
                        entry.insert(0,vars[i-1])
                        entry.grid(row = j,column=i)
                        dat.append(entry)
                    elif i==0:
                        lbl = ttk.Label(frame_table,text = str(j),justify=RIGHT)
                        lbl.grid(row = j,column=i)
                    else:
                        entry = ttk.Entry(frame_table,text=str(i)+str(j),justify=RIGHT)
                        entry.insert(0,dd[j-1][i])
                        entry.grid(row = j,column=i)

                        dat.append(entry)
                if i != 0:
                    self.data.append(dat)
        self.canv.bind_all("<MouseWheel>", lambda e: self.canv.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.canv.bind_all("<Shift-MouseWheel>", lambda e: self.canv.xview_scroll(int(-1*(e.delta/120)), "units"))
        
    def excel_save(self):
        excel_dict = {}

        for i in self.data:

            col = list(map(lambda x: x.get(),i))
            excel_dict[col[0]] = col[1:]

        df = pd.DataFrame(excel_dict)
        filepath = filedialog.asksaveasfilename()
        df.to_excel(filepath+".xlsx")
        
    def excel_open(self):
        filepath = filedialog.askopenfilename()
        df = pd.read_excel(filepath) 
        dd = np.array(df)
        new_book = Book(len(dd),len(dd[0])-1,"new",df,True)  

    def new_book(self):

        new_create = Create()

    def function1(self):
        functiontk = Tk()
        functiontk.geometry("500x500")

        frame_select = Frame(functiontk)
        col_names = []
        for i in self.data:
            col_names.append(i[0].get())
            continue
        col_names_var = Variable(value = col_names)
        listbox = Listbox(frame_select,listvariable=col_names_var,selectmode=MULTIPLE)
        listbox.pack()
        frame_select.pack()
        def get_selected():
            indices = listbox.curselection()
            raw_data = []
            for i in indices:
                raw_data.append(self.data[i])
            function1 = Function1(raw_data)


        but = ttk.Button(functiontk, text="Выполнить", command=get_selected)
        but.pack()
        functiontk.mainloop()





class Function1(Tk):
    def __init__(self,raw_data):
        
        super().__init__()
        self.geometry("500x500")

        self.canv = tk.Canvas(self)
        self.canv.pack(side="left", fill="both", expand=True)

        frame_table = Frame(self.canv)
        frame_table.bind("<Configure>", lambda e: self.canv.configure(scrollregion=self.canv.bbox("all")))
        self.canv.create_window((0,0),window=frame_table,anchor="nw")


        for i in range(len(raw_data[0])):
            if i != 0:
                lbl = ttk.Label(frame_table, text=str(i), justify=RIGHT)
                lbl.grid(row=i, column=0)
        for i in range(len(raw_data)):

            for j in range(len(raw_data[i])):

                if j == 0:
                    entry = ttk.Entry(frame_table, justify=RIGHT)
                    entry.insert(0, raw_data[i][j].get())
                    entry.grid(row=j, column=i+1)


                else:
                    entry = ttk.Entry(frame_table, justify=RIGHT)
                    entry.insert(0,raw_data[i][j].get())
                    entry.grid(row=j, column=i+1)



        self.canv.bind_all("<MouseWheel>", lambda e: self.canv.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.canv.bind_all("<Shift-MouseWheel>", lambda e: self.canv.xview_scroll(int(-1*(e.delta/120)), "units"))





c = Create()





