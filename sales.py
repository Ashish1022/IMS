from tkinter import *
import owner 
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3
import os

developer  = owner.developer
class sales:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title(f'Inventory Management System | Developed By {developer}')
        self.root.config(bg="white")
        self.root.focus_force()

        #********variables********
        self.var_invoice = StringVar()
        self.var_billList = []

        #********title********

        lbl_title = Label(self.root,text='Customer Billing Area',font=("goudy old style",30),bg='#184a45',fg='white',bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice = Label(self.root,text='Invoice No.',font=("times new roman",15),bg='white').place(x=50,y=100)
        txt_invoice = Entry(self.root,textvariable=self.var_invoice,font=("goudy old style",18),bg='lightyellow').place(x=160,y=100,width=180,height=28)

        btn_search = Button(self.root,text="Search",command=self.search,cursor='hand2',font=('times new roman',15,'bold'),bg='#2196f3',fg='white').place(x=360,y=100,width=120,height=28)

        btn_clear = Button(self.root,text="Clear",command=self.clear,cursor='hand2',font=('times new roman',15,'bold'),bg='lightgrey').place(x=490,y=100,width=120,height=28)

        salesFrame = Frame(self.root,bd=3,relief=RIDGE)
        salesFrame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(salesFrame,orient=VERTICAL)
        scrollx=Scrollbar(salesFrame,orient=HORIZONTAL)

        self.SalesList = Listbox(salesFrame,font=('goudy old style',15),bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.SalesList.yview)
        self.SalesList.pack(fill=BOTH,expand=1)
        self.SalesList.bind("<ButtonRelease-1>",self.getData)

        #*******Billing Area*******
        billFrame = Frame(self.root,bd=3,relief=RIDGE)
        billFrame.place(x=280,y=140,width=410,height=330)

        lbl_title2 = Label(billFrame,text='Customer Billing Area',font=("goudy old style",20),bg='orange').pack(side=TOP,fill=X)

        scrolly2=Scrollbar(billFrame,orient=VERTICAL)
        scrollx=Scrollbar(billFrame,orient=HORIZONTAL)

        self.billArea = Text(billFrame,font=('goudy old style',15),bg='lightyellow',yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.SalesList.yview)
        self.billArea.pack(fill=BOTH,expand=1)

        #********Images********
        self.billPhoto = Image.open("images/cat2.jpg")
        self.billPhoto = self.billPhoto.resize((450,300),Image.BICUBIC)
        self.billPhoto = ImageTk.PhotoImage(self.billPhoto)

        lbl_image = Label(self.root,image=self.billPhoto,bd=0)
        lbl_image.place(x=700,y=110)

        self.show()
    #**********functions*********
    def show(self):
        del self.var_billList[:]
        self.SalesList.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.SalesList.insert(END,i)
                self.var_billList.append(i.split('.')[0])

    def getData(self,ev):
        index_ = self.SalesList.curselection()
        fileName = self.SalesList.get(index_)
        print(fileName)
        self.billArea.delete('1.0',END)
        filePath = open(f'bill/{fileName}','r')
        for i in filePath:
            self.billArea.insert(END,i)
        filePath.close()

    def search(self):
        if self.var_invoice.get()=='':
            messagebox.showerror("Error","Invoice No. required",parent=self.root)
        else:
            if self.var_invoice.get() in self.var_billList:
                filePath = open(f'bill/{self.var_invoice.get()}.txt','r')
                self.billArea.delete('1.0',END)
                for i in filePath:
                    self.billArea.insert(END,i)
                filePath.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

    def clear(self):
        self.show()
        self.billArea.delete('1.0',END)


if __name__ == "__main__":
    root = Tk()
    obj = sales(root)
    root.mainloop()