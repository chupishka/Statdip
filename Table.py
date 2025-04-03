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
        self.columns = []
        for i in range(int(rows)+1):
            for j in range(int(col)+1):
                if i==0 and j== 0:
                    continue
                if i==0:
                    lbl = ttk.Label(self,text = "Var"+str(j))
                    lbl.grid(row = i,column=j)
                elif j==0:
                    lbl = ttk.Label(self,text = str(i))
                    lbl.grid(row = i,column=j)
                else:
                    entry = ttk.Entry(self,text=str(i)+str(j))
                    entry.grid(row = i,column=j)

        # for i in range(int(col)):
        #     self.columns += ["Var"+str(i)]
        #
        # self.tree = ttk.Treeview(self,columns = self.columns,show="headings")
        # for i in self.columns:
        #     self.tree.heading(str(i),text = str(i))
        # self.tree.pack()

