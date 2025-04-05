from tkinter import *
import tkinter as tk
from tkinter import ttk


class Table(Tk):
    def __init__(self,rows,col):
        super().__init__()

        self.geometry("500x500")
        # self.lbl = ttk.Label(self,text=rows)
        # self.lbl.pack()
        # self.lbl1 = ttk.Label(self,text=col)
        # self.lbl1.pack()
        frame_table = ttk.Frame(self,borderwidth=10,padding=[10,10],relief=SOLID)
        table_menu = Menu(self)
        file_menu = Menu(self)
        file_menu.add_cascade(label="New book",command= lambda x = self:Table.new_book(self))
        file_menu.add_cascade(label="Save book")

        table_menu.add_cascade(label="File",menu=file_menu)
        table_menu.add_cascade(label="Edit")
        self.config(menu = table_menu)
        self.columns = []
        for i in range(int(rows)+1):
            dat=[]
            for j in range(int(col)+1):

                if i==0 and j== 0:
                    continue
                if i==0:
                    lbl = ttk.Entry(frame_table,text = "Var"+str(j))
                    lbl.insert(0,"Var"+str(j))
                    lbl.grid(row = i,column=j)
                elif j==0:
                    lbl = ttk.Label(frame_table,text = str(i))
                    lbl.grid(row = i,column=j)
                else:
                    entry = ttk.Entry(frame_table,text=str(i)+str(j))
                    entry.grid(row = i,column=j)
        frame_table.pack()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
    def new_book(self):
        # from main import Create
        # new_create = Create()
        return



        # for i in range(int(col)):
        #     self.columns += ["Var"+str(i)]
        #
        # self.tree = ttk.Treeview(self,columns = self.columns,show="headings")
        # for i in self.columns:
        #     self.tree.heading(str(i),text = str(i))
        # self.tree.pack()

