from email.policy import default
from symtable import Function
from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.figure
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import numpy as np
import math
import scipy.stats as sc
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Create:
    def __init__(self):
        x = self
        self.root = Tk()
        self.root.title("Создание")

        icon = PhotoImage(master=self.root,file="img/menu_book_37dp_000000_FILL0_wght400_GRAD0_opsz40.png")
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
        self.lift()  # Поднять окно поверх других
        self.focus_force()  # Принудительно дать фокус (может работать не на всех ОС)
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

        
        func_menu.add_cascade(label="Dispersion analyze",command= lambda x = self:Book.function1(self))
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
        self.raw_data = []
        self.raw_indexes = []
        
        functiontk = Tk()
        functiontk.geometry("500x500")
        functiontk.title("Parametres")

        

        frame_select = Frame(functiontk)
        col_names = []
        for i in self.data:
            col_names.append(i[0].get())
            continue
        col_names_var = Variable(frame_select,value = col_names)
        listbox = Listbox(frame_select,listvariable=col_names_var,selectmode=MULTIPLE)
        lbl = ttk.Label(frame_select,text="Выберите параметры")
        lbl.pack()
        listbox.pack()
        


        def get_selected():
            indices = listbox.curselection()
            self.raw_data = []
            for i in indices:
                self.raw_data.append(self.data[i])
            
        but = ttk.Button(frame_select, text="Выбрать", command=get_selected)
        but.pack()
        
        
            
        def func():
            
            func1 = Function1(raw_data=self.raw_data,raw_indexes=self.raw_indexes)

        frame_select1 = Frame(functiontk)
        listbox1 = Listbox(frame_select1,listvariable=col_names_var,selectmode=MULTIPLE)
        lbl1 = ttk.Label(frame_select1,text="Выберите cтолбец обозначений")
        lbl1.pack()
        listbox1.pack()

        def get_selected1():
            
            self.raw_indexes = []
            indices = listbox1.curselection()
            for i in indices:
                
                self.raw_indexes.append(self.data[i])

        but1 = ttk.Button(frame_select1, text="Выбрать", command=get_selected1)
        but1.pack()
        frame_select.grid(row=0,column=0)
        functiontk.columnconfigure(index = 0,weight=1)
        functiontk.columnconfigure(index = 1,weight=1)
        # functiontk.rowconfigure(index=1,weight=1)
        frame_select1.grid(row=0,column=1)

        but2 = ttk.Button(functiontk, text="Выполнить", command=func)
        but2.grid(row=1,column=0,columnspan=2,sticky="s")

        
        
        functiontk.mainloop()





class Function1(Tk):
    def __init__(self,raw_data,raw_indexes):
        
        
        super().__init__()
        self.title("Dispersion analyze")

        self.geometry("1000x1000")

        self.canv = tk.Canvas(self)
        self.canv.pack(side="top", fill="both", expand=True)

        frame_table = Frame(self.canv)
        frame_table.bind("<Configure>", lambda e: self.canv.configure(scrollregion=self.canv.bbox("all")))
        self.canv.create_window((0,0),window=frame_table,anchor="nw")

        data1 = [0]*(len(raw_data[0])-1)
        ln = len(raw_data[0])
        for i in range(len(raw_data)):
                
            for  j in range(1,len(raw_data[i])):
                data1[j-1] += (math.pow(float(raw_data[i][j].get()),2))/ln

        for i in range(len(data1)):
            data1[i] = -10 *(math.log10(data1[i]))


        phisher_analyse_arr = []
        unique_list = []
        y_dots = []
        for raw_indexes_col in raw_indexes:

            list1 = []
            for i in raw_indexes_col[1:]:
                list1.append(i.get())
            
            # unique = list(set(list1))
            unique = []
            for i in list1:
                if i in unique:
                    continue
                else:
                    unique.append(i)
            unique_list.append(unique)
            

            

            # analyse_data = []
            # for cur_col in raw_data:
            col_data = []
            for un in unique:

                col_data_col = []

                for i in range(1,len(raw_data[0])):
                        # if float(cur_col[i].get()) == float(0):
                        #     continue
                        

                    if raw_indexes_col[i].get() == un:
                        col_data_col.append(data1[i-1])
                        
                col_data.append(col_data_col)
                # analyse_data.append(col_data)

            # print(analyse_data)
            
            phisher_analyse = []
            for data in [col_data]:
                

                alpha = 0.06
                summ_mean = 0
                SSb = 0
                SSw = 0
                SSt = 0
                
                
                n_col_list=[]
                n = 0
                for i in data:

                    n_col = 0
                    for j in i:

                        
                        
                        n_col+=1
                        n+=1
                        summ_mean+=float(j)
                    n_col_list.append(n_col)



                    
                
                k = len(data)
                

                summ_mean = summ_mean/n
                
                # ssb = 2.51 dfb = 3 msb = 0.83 f = 0.56 p = 0.67 r кривизны по верт мм

                dfb = k-1
                dfw = n-k
                dft = n - 1
                dispers = 0
                x_col_mean_list = []
                for i in range(len(data)):
                    x_col_mean = 0
                    for j in range(len(data[i])):
                        
                        x_col_mean += (float(data[i][j])/n_col_list[i])
                    SSb += math.pow((x_col_mean - summ_mean),2)*n_col_list[i]
                    x_col_mean_list.append(x_col_mean)
                y_dots.append(x_col_mean_list)
                for i in range(len(data)):

                    for j in range(len(data[i])):
                        
                        SSw+=math.pow((float(data[i][j]) - x_col_mean_list[i]),2)
                        SSt+=math.pow((float(data[i][j]) - summ_mean),2)

                MSb = SSb/dfb
                MSw = SSw/dfw
                MSt = SSt/dft

                
                F = MSb/MSw
                F_critical = sc.f.ppf(1-alpha,dfb,dfw)
                P_value = sc.f.sf(F,dfb,dfw)

                phisher = [SSb,SSw,dfb,dfw,MSb,MSw,F,F_critical,P_value]

                # phisher_analyse.append(phisher)
            phisher_analyse_arr.append(phisher)
        

        std = np.std(data1,ddof=1)
        mean = np.mean(data1)

        fig = matplotlib.figure.Figure(figsize=(12, 8), dpi=100)
        
        ax = fig.add_subplot(111)
        

        


        ax.axhline(y=mean + 2*std, color='gray', linestyle='--', linewidth=1)
        ax.axhline(y=mean - 2*std, color='gray', linestyle='--', linewidth=1)
        ax.axhline(y=mean, color='red', linewidth=1)
        counter = 3.5
        stri=""
        for i in range(len(unique_list)):
            if i == len(unique_list)-1:
                stri+=raw_indexes[i][0].get()
            else:
                ax.axvline(0+counter)
                stri+=raw_indexes[i][0].get()+",    "
            
            counter+=4

        counter = 0
        x_positions = np.arange(len(np.reshape(np.array(unique_list),(-1))))
        for i in range(len(unique_list)):
            x_cur = x_positions[0+counter:4+counter]
            ax.plot(x_cur,y_dots[i],marker = "o")
            counter+=4

        mn = np.min(x_col_mean_list)
        mx = np.max(x_col_mean_list)

        


        ax.set_xticks(x_positions, np.reshape(np.array(unique_list),(-1)), ha='right')
        ax.set_yticks(np.arange(np.floor(mn)-3,np.ceil(mx)+3,0.5))
        ax.set_ylabel('ЭТА = -10log10(sum((yi^2)/n)')
        ax.set_title(stri)
        ax.grid(True, linestyle=':', alpha=0.7)
        # ax.legend()

        
        




        


        
            


        names = ["SSb","SSw","dfb","dfw","MSb","MSw","F","F-crit","p"]
        counter = 0
        # for raw_index in range(len(raw_indexes)):
        # lbl = ttk.Label(frame_table, text=raw_indexes[raw_index][0].get(), justify=RIGHT)
        # lbl.grid(row=0+counter, column=0,rowspan=2)
        for i in range(len(raw_indexes)):
                
            lbl = ttk.Label(frame_table, text=raw_indexes[i][0].get(), justify=RIGHT)
            lbl.grid(row=i+1, column=0)

        for i in range(len(names)):
                
            lbl = ttk.Label(frame_table, text=names[i], justify=RIGHT)
            lbl.grid(row=0, column=i+1)
        phisher_analyse = phisher_analyse_arr
        for i in range(len(phisher_analyse)):

            for j in range(len(phisher_analyse[i])):
                entry = ttk.Entry(frame_table, justify=RIGHT)
                entry.insert(0, str(phisher_analyse[i][j]))
                entry.grid(row=i+1, column=j+1)
       
        frame_img = Frame(master=self)
        frame_img.pack(side="bottom")
        canvas = FigureCanvasTkAgg(fig, master=frame_img)
        canvas.draw()
        canvas.get_tk_widget().pack()


        self.canv.bind_all("<MouseWheel>", lambda e: self.canv.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.canv.bind_all("<Shift-MouseWheel>", lambda e: self.canv.xview_scroll(int(-1*(e.delta/120)), "units"))





c = Create()





