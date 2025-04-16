from email.policy import default
from symtable import Function
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd


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
    def __init__(self, rows, col, name):
        super().__init__()
        self.canv = tk.Canvas(self)
        self.geometry("700x700")
        self.title(name)
        
        # Создаем фрейм для скроллбаров и канваса
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        # Горизонтальная прокрутка
        self.scrlx = ttk.Scrollbar(self.main_frame, orient="horizontal", command=self.canv.xview)
        # Вертикальная прокрутка
        self.scrly = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canv.yview)
        
        self.canv.configure(xscrollcommand=self.scrlx.set)
        self.canv.configure(yscrollcommand=self.scrly.set)
        
        # Размещаем канвас и скроллбары
        self.canv.pack(side="left", fill="both", expand=True)
        self.scrly.pack(side="right", fill="y")
        self.scrlx.pack(side="bottom", fill="x")

        icon1 = PhotoImage(master=self, file="img/book_37dp_000000_FILL0_wght400_GRAD0_opsz40.png")
        self.iconphoto(False, icon1)

        frame_table = ttk.Frame(self.canv, borderwidth=3)
        self.canv.create_window((0, 0), window=frame_table, anchor="nw")
        
        # Привязываем изменение размера фрейма к обновлению области прокрутки
        frame_table.bind("<Configure>", lambda e: self.canv.configure(scrollregion=self.canv.bbox("all")))
        
        table_menu = Menu(self)
        file_menu = Menu(self)
        func_menu = Menu(self)

        func_menu.add_cascade(label="Function1", command=lambda x=self: Book.function1(self))
        file_menu.add_cascade(label="New book", command=lambda x=self: Book.new_book(self))
        file_menu.add_cascade(label="Save book")

        table_menu.add_cascade(label="File", menu=file_menu)
        table_menu.add_cascade(label="Edit")
        table_menu.add_cascade(label="Functions", menu=func_menu)
        self.config(menu=table_menu)
        
        self.columns = []
        self.data = []
        for i in range(int(col)+1):
            dat = []
            for j in range(int(rows)+1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    entry = ttk.Entry(frame_table, text="Var"+str(i), justify="right")
                    entry.insert(0, "Var"+str(i))
                    entry.grid(row=j, column=i, sticky="nsew")
                    dat.append(entry)
                elif i == 0:
                    lbl = ttk.Label(frame_table, text=str(j), justify="right")
                    lbl.grid(row=j, column=i, sticky="nsew")
                else:
                    entry = ttk.Entry(frame_table, text=str(i)+str(j), justify="right")
                    entry.grid(row=j, column=i, sticky="nsew")
                    dat.append(entry)
            if i != 0:
                self.data.append(dat)
        
        # Настраиваем растягивание ячеек таблицы
        # for i in range(int(col)+1):
        #     frame_table.grid_columnconfigure(i, weight=1)
        # for j in range(int(rows)+1):
        #     frame_table.grid_rowconfigure(j, weight=1)
        
        # Привязываем колесо мыши для прокрутки
        self.canv.bind_all("<MouseWheel>", lambda e: self.canv.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.canv.bind_all("<Shift-MouseWheel>", lambda e: self.canv.xview_scroll(int(-1*(e.delta/120)), "units"))
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

        frame_table = Frame(self)


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



        frame_table.pack(anchor="nw")





c = Create()





