import sqlite3
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import owner 


developer  = owner.developer
class billing:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title(f'Inventory Management System | Developed By {developer}')
        self.root.config(bg="white")
        self.root.focus_force()
        self.cartList=[]
        #*********title*********
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#9DBC98",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #**********btn-logout**********
        btn_logout = Button(self.root,text="Logout",highlightbackground="red",font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1200,y=10,height=40,width=110)

        #**********clock**********
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD/MM/YY\t\t Time: HH:MM:SS",compound=LEFT,font=("times new roman",15),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #********product frame*********

        self.var_search = StringVar()

        productFrame1 = Frame(self.root,bd=4,relief=RIDGE,bg='white')
        productFrame1.place(x=6,y=110,width=410,height=550)
        pTitle = Label(productFrame1,text='All Products',font=('goudy old style',15,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)

        productFrame2 = Frame(productFrame1,bd=2,relief=RIDGE,bg='white')
        productFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search = Label(productFrame2,text='Search Product | By Name',font=('times new roman',15,'bold'),bg="white",fg="green").place(x=2,y=5)

        lbl_search = Label(productFrame2,text='Product Name',font=('times new roman',15,'bold'),bg="white").place(x=2,y=45)
        txt_search = Entry(productFrame2,textvariable=self.var_search,font=('times new roman',15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search = Button(productFrame2,text='Search',command=self.search,cursor='hand2',font=('goudy old style',15),bg='#2196f3',fg='white').place(x=285,y=45,width=100,height=25)
        btn_showAll = Button(productFrame2,text='Show All',command=self.show,cursor='hand2',font=('goudy old style',15),bg='#083531',fg='white').place(x=285,y=10,width=100,height=25)


        #********Employee Details********

        productFrame3 = Frame(productFrame1,bd=3,relief=RIDGE)
        productFrame3.place(x=2,y=140,width=398,height=375)

        scrolly = Scrollbar(productFrame3,orient=VERTICAL)
        scrollx = Scrollbar(productFrame3,orient=HORIZONTAL)

        self.productTable = ttk.Treeview(productFrame3,columns=("proID","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("proID",text="Product ID")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Quantity")
        self.productTable.heading("status",text="Status")


        self.productTable["show"] = "headings"

        self.productTable.column("proID",width=40)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=50)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=90)

        self.productTable.pack(fill=BOTH,expand=1)

        self.productTable.bind("<ButtonRelease-1>",self.getData)


        lbl_note = Label(productFrame1,text='Note : Enter 0 quantity to remove product from cart',font=('goudy old style',12,'bold'),anchor=W,bg='white',fg='red').pack(side=BOTTOM,fill=X)



        #********customer frame*********
        self.var_cname = StringVar()
        self.var_contact = StringVar()

        customerFrame = Frame(self.root,bd=4,relief=RIDGE,bg='white')
        customerFrame.place(x=420,y=110,width=530,height=70)
        cTitle = Label(customerFrame,text='Customer Details',font=('goudy old style',15),bg='lightgrey').pack(side=TOP,fill=X)


        lbl_name = Label(customerFrame,text='Name',font=('times new roman',15),bg="white").place(x=5,y=35)
        txt_name = Entry(customerFrame,textvariable=self.var_cname,font=('times new roman',13),bg="lightyellow").place(x=80,y=35,width=180) 

        lbl_contact = Label(customerFrame,text='Contact No.',font=('times new roman',15),bg="white").place(x=270,y=35)
        txt_contact = Entry(customerFrame,textvariable=self.var_contact,font=('times new roman',13),bg="lightyellow").place(x=380,y=35,width=140) 



        #************cal and cart frame*************

        CalCartFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        CalCartFrame.place(x=420,y=190,width=530,height=360)
        # cTitle = Label(CalCartFrame,text='Customer Details',font=('goudy old style',15),bg='lightgrey').pack(side=TOP,fill=X)

        #********cal frame********
        self.var_CalInput = StringVar()


        CalFrame = Frame(CalCartFrame,bd=9,relief=RIDGE,bg='white')
        CalFrame.place(x=5,y=10,width=268,height=340)

        self.txtCalInput = Entry(CalFrame,textvariable=self.var_CalInput,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        self.txtCalInput.grid(row=0,columnspan=4)

        btn_7 = Button(CalFrame,text='7',font=('arial',15,'bold'),command=lambda:self.getInput(7),cursor='hand2',bd=5,width=4,pady=10).grid(row=1,column=0)
        btn_8 = Button(CalFrame,text='8',font=('arial',15,'bold'),command=lambda:self.getInput(6),cursor='hand2',bd=5,width=4,pady=10).grid(row=1,column=1)
        btn_9 = Button(CalFrame,text='9',font=('arial',15,'bold'),command=lambda:self.getInput(5),cursor='hand2',bd=5,width=4,pady=10).grid(row=1,column=2)
        btn_sum = Button(CalFrame,text='+',font=('arial',15,'bold'),command=lambda:self.getInput('+'),cursor='hand2',bd=5,width=4,pady=10).grid(row=1,column=3)

        btn_6 = Button(CalFrame,text='6',font=('arial',15,'bold'),command=lambda:self.getInput(6),cursor='hand2',bd=5,width=4,pady=10).grid(row=2,column=0)
        btn_5 = Button(CalFrame,text='5',font=('arial',15,'bold'),command=lambda:self.getInput(5),cursor='hand2',bd=5,width=4,pady=10).grid(row=2,column=1)
        btn_4 = Button(CalFrame,text='4',font=('arial',15,'bold'),command=lambda:self.getInput(4),cursor='hand2',bd=5,width=4,pady=10).grid(row=2,column=2)
        btn_sub = Button(CalFrame,text='-',font=('arial',15,'bold'),command=lambda:self.getInput('-'),cursor='hand2',bd=5,width=4,pady=10).grid(row=2,column=3)

        btn_3 = Button(CalFrame,text='3',font=('arial',15,'bold'),command=lambda:self.getInput(3),cursor='hand2',bd=5,width=4,pady=10).grid(row=3,column=0)
        btn_2 = Button(CalFrame,text='2',font=('arial',15,'bold'),command=lambda:self.getInput(2),cursor='hand2',bd=5,width=4,pady=10).grid(row=3,column=1)
        btn_1 = Button(CalFrame,text='1',font=('arial',15,'bold'),command=lambda:self.getInput(1),cursor='hand2',bd=5,width=4,pady=10).grid(row=3,column=2)
        btn_mul = Button(CalFrame,text='*',font=('arial',15,'bold'),command=lambda:self.getInput('*'),cursor='hand2',bd=5,width=4,pady=10).grid(row=3,column=3)

        btn_0 = Button(CalFrame,text='0',font=('arial',15,'bold'),command=lambda:self.getInput(0),cursor='hand2',bd=5,width=4,pady=15).grid(row=4,column=0)
        btn_c = Button(CalFrame,text='C',font=('arial',15,'bold'),command=self.clearCal,cursor='hand2',bd=5,width=4,pady=15).grid(row=4,column=1)
        btn_equal = Button(CalFrame,text='=',font=('arial',15,'bold'),command=self.performCal,cursor='hand2',bd=5,width=4,pady=15).grid(row=4,column=2)
        btn_div = Button(CalFrame,text='/',font=('arial',15,'bold'),command=lambda:self.getInput('/'),cursor='hand2',bd=5,width=4,pady=15).grid(row=4,column=3)



        cartFrame = Frame(CalCartFrame,bd=3,relief=RIDGE)
        cartFrame.place(x=280,y=8,width=245,height=342)
        self.cartTitle = Label(cartFrame,text='Cart \tTotal Product : 0',font=('goudy old style',15),bg='lightgrey')
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly = Scrollbar(cartFrame,orient=VERTICAL)
        scrollx = Scrollbar(cartFrame,orient=HORIZONTAL)

        self.cartTable = ttk.Treeview(cartFrame,columns=("proID","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        self.cartTable.heading("proID",text="PID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("qty",text="QTY")
        self.cartTable.heading("status",text="Status")


        self.cartTable["show"] = "headings"

        self.cartTable.column("proID",width=40)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=90)
        self.cartTable.column("qty",width=40)
        self.cartTable.column("status",width=90)

        self.cartTable.pack(fill=BOTH,expand=1)

        # self.cartTable.bind("<ButtonRelease-1>",self.getData)


        #*********Add cart widgets*********
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_instock = StringVar()


        cartButtonFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        cartButtonFrame.place(x=420,y=550,width=530,height=110)


        lbl_pName = Label(cartButtonFrame,text='Product Name',font=('times new roman',15),bg='white').place(x=5,y=5)
        txt_pName = Entry(cartButtonFrame,textvariable=self.var_pname,font=('times new roman',15),bg="lightyellow",state='readonly').place(x=5,y=30,width=190,height=22)

        lbl_pPrice = Label(cartButtonFrame,text='Price Per QTY',font=('times new roman',15),bg='white').place(x=230,y=5)
        txt_pPrice = Entry(cartButtonFrame,textvariable=self.var_price,font=('times new roman',15),bg="lightyellow",state='readonly').place(x=230,y=30,width=150,height=22)

        lbl_pQTY = Label(cartButtonFrame,text='Quantity',font=('times new roman',15),bg='white').place(x=390,y=5)
        txt_pQTY = Entry(cartButtonFrame,textvariable=self.var_qty,font=('times new roman',15),bg="lightyellow").place(x=390,y=30,width=120,height=22)

        self.lbl_instock = Label(cartButtonFrame,text='In stock',font=('times new roman',15),bg='white')
        self.lbl_instock.place(x=5,y=70)

        btn_clear = Button(cartButtonFrame,text="Clear",cursor="hand2",font=("goudy old style",15,'bold'),bg="lightgrey").place(x=180,y=70,width=150,height=30)
        btn_add = Button(cartButtonFrame,text="Add | Update",command=self.AddUpdateCart,cursor="hand2",font=("goudy old style",15,'bold'),bg="orange").place(x=340,y=70,width=150,height=30)


        #**********billing area*********
        billFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)

        bTitle = Label(billFrame,text='Customer Bill',font=('goudy old style',15,'bold'),bg='#f44336',fg='white').pack(side=TOP,fill=X)

        scrolly = Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_billArea = Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_billArea.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_billArea.yview)

        #**********billing buttons*********
        billMenuFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=410,height=140)


        self.lbl_amnt = Label(billMenuFrame,text='Bill Amount\n[0]',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white',bd=2,relief=RIDGE)
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount = Label(billMenuFrame,text='Discount\n[5%]',font=('goudy old style',15,'bold'),bg='#8bc34a',fg='white',bd=2,relief=RIDGE)
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netPay = Label(billMenuFrame,text='Net Pay\n[0]',font=('goudy old style',15,'bold'),bg='#607d8b',fg='white',bd=2,relief=RIDGE)
        self.lbl_netPay.place(x=246,y=5,width=160,height=70)

        btn_lbl_print = Button(billMenuFrame,text='Print',cursor='hand2',font=('goudy old style',15,'bold'),bg='green',fg='white',bd=2,relief=RIDGE)
        btn_lbl_print.place(x=2,y=80,width=120,height=50)

        btn_lbl_clear = Button(billMenuFrame,text='Clear All',cursor='hand2',font=('goudy old style',15,'bold'),bg='grey',fg='white',bd=2,relief=RIDGE)
        btn_lbl_clear.place(x=124,y=80,width=120,height=50)

        btn_lbl_generate = Button(billMenuFrame,text='Generate Bill/Save Bill',cursor='hand2',font=('goudy old style',15,'bold'),bg='#009688',fg='white',bd=2,relief=RIDGE)
        btn_lbl_generate.place(x=246,y=80,width=160,height=50)



        #*******footer*******

        footer = Label(self.root,text=f'IMS-Inventory Management System | Developed by {developer}\nFor any technical issue contact : xxxxxxxxxx',font=('times new roman',11),bg='#4d636d',fg='white',bd=0,cursor='hand2').pack(side=BOTTOM,fill=X)

        self.show()

#**************functions***************
    def getInput(self,num):
        xnum = self.var_CalInput.get()+str(num)
        self.var_CalInput.set(xnum)

    
    def clearCal(self):
        self.var_CalInput.set('')

    
    def performCal(self):
        result = self.var_CalInput.get()

        self.var_CalInput.set(eval(result))


    def show(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT proID,name,price,qty,status from product where status='Active'")
            rows = cur.fetchall()
            
            self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                self.productTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  


    def search(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Nothing selected",parent=self.root)
            else:
                cur.execute("SELECT proID,name,price,qty,status FROM product where Name Like '%"+self.var_search.get()+"%' and status='Active'")
                rows = cur.fetchall()

                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())

                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def getData(self,ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])

        self.lbl_instock.config(text=f'In stock [{str(row[3])}]')

    def AddUpdateCart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please select product from list",parent=self.root)
        if self.var_qty.get() == '':
            messagebox.showerror("Error","Quantity is required",parent=self.root)
        else:
            price_cal = float(int(self.var_qty.get())*float(self.var_price.get()))
            cart_data = [self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]

            #******update cart*******
            present = 'no'
            index_ = 0
            for row in self.cartList:   
                if self.var_pid.get()==row[0]:
                    present = 'yes'
                    break
                index_ +=1
            if present == 'yes':
                op=messagebox.askyesno("Confirm","Product already present\nDo you want to update | remove form cart list",parent=self.root)
                if op == True:
                    if self.var_qty.get()=="0":
                        self.cartList.pop(index_)
                    else:
                        self.cartList[index_][2] = price_cal
                        self.cartList[index_][3] = self.var_qty.get()

            else:
                self.cartList.append(cart_data)
            self.show_cart()
            self.bill_updates()
        
    
    def bill_updates(self):
        bill_amt = 0
        net_pay = 0
        for row in self.cartList:
            bill_amt = bill_amt + float(row[2])
        net_pay = bill_amt - ((bill_amt*5)/100)

        self.lbl_amnt.config(text=f'Bill Amnt\n{str(bill_amt)}')
        self.lbl_netPay.config(text=f'Net Amnt\n{str(net_pay)}')
        self.cartTitle.config(text=f'Cart \tTotal Product: [{str(len(self.cartList))}]')


    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cartList:
                self.cartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  



if __name__ == "__main__":
    root = Tk()
    obj = billing(root)
    root.mainloop()