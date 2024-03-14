from tkinter import *
import owner 
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

developer  = owner.developer
class product:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title(f'Inventory Management System | Developed By {developer}')
        self.root.config(bg="white")
        self.root.focus_force()

        #********variabels*******
        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_proID = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()



        #*************************
        productFrame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        productFrame.place(x=10,y=10,width=450,height=480)

        #********title********
        title = Label(productFrame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)


        #*******column1********
        lbl_cat = Label(productFrame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_sup = Label(productFrame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product = Label(productFrame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price = Label(productFrame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty = Label(productFrame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_stat = Label(productFrame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)


        #********column2*******

        cmb_cat = ttk.Combobox(productFrame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        
        cmb_sup = ttk.Combobox(productFrame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)
        
        txt_name = Entry(productFrame,textvariable=self.var_name,justify=CENTER,bd=2,relief=RIDGE,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        
        txt_price = Entry(productFrame,textvariable=self.var_price,justify=CENTER,bd=2,relief=RIDGE,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        
        txt_qty = Entry(productFrame,textvariable=self.var_qty,justify=CENTER,bd=2,relief=RIDGE,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)
        
        cmb_status = ttk.Combobox(productFrame,textvariable=self.var_status,values=("Active",'Inactive'),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #********button********
        btn_search = Button(productFrame,text="Save",command=self.add,cursor="hand2",font=("goudy old style",15),bg="#2196f3",fg="white").place(x=10,y=400,width=100,height=40)
        btn_update = Button(productFrame,text="Update",command=self.update,cursor="hand2",font=("goudy old style",15),bg="green",fg="white").place(x=120,y=400,width=100,height=40)
        btn_delete = Button(productFrame,text="Delete",command=self.delete,cursor="hand2",font=("goudy old style",15),bg="red",fg="white").place(x=230,y=400,width=100,height=40)
        btn_clear = Button(productFrame,text="Clear",command=self.clear,cursor="hand2",font=("goudy old style",15),bg="grey",fg="white").place(x=340,y=400,width=100,height=40)



        #********searchFrame********
        searchFrame = LabelFrame(self.root,text="Search Product",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        searchFrame.place(x=480,y=10,width=600,height=80)

        #********Options********
        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(searchFrame,text="Search",command=self.search,cursor="hand2",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)


        #********Product Details********

        pro_frame = Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=480,y=100,width=600,height=390)

        scrolly = Scrollbar(pro_frame,orient=VERTICAL)
        scrollx = Scrollbar(pro_frame,orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(pro_frame,columns=("proID","Category","Supplier","Name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("proID",text="Pro ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("Name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")


        self.ProductTable["show"] = "headings"

        self.ProductTable.column("proID",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=50)
        self.ProductTable.column("Name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)

        self.ProductTable.pack(fill=BOTH,expand=1)

        self.ProductTable.bind("<ButtonRelease-1>",self.getData)

        self.show()

    #*********functions**********

    def fetch(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=='Select' or self.var_name.get()=='' or self.var_sup.get()=='Empty':
                messagebox.showerror("Error","All fields required",parent=self.root)
            else:
                cur.execute("SELECT * FROM product where Name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product already Present try Different",parent=self.root)
                else:
                    cur.execute("INSERT INTO product(Category,Supplier,Name,price,qty,status) VALUES(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            
            self.ProductTable.delete(*self.ProductTable.get_children())

            for row in rows:
                self.ProductTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def getData(self,ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content['values']

        self.var_proID.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),


    def update(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_proID.get()=="":
                messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                cur.execute("SELECT * FROM product where proID=?",(self.var_proID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    cur.execute("UPDATE product SET Category=?,Supplier=?,Name=?,price=?,qty=?,status=?",(
                        
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_proID.get()=="":
                messagebox.showerror("Error","Select product from list required",parent=self.root)
            else:
                cur.execute("SELECT * FROM product where proID=?",(self.var_proID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM product WHERE proID=?",(self.var_proID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content['values']
        try:
            self.var_cat.set("Select"),
            self.var_sup.set("Select"),
            self.var_name.set(""),
            self.var_price.set(""),
            self.var_qty.set(""),
            self.var_status.set("Active"),
            self.var_proID.set(""),

            self.var_searchtext.set("")
            self.var_searchby.set("Select")
            self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def search(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Option",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Nothing selected",parent=self.root)
            else:
                cur.execute("SELECT * FROM product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows = cur.fetchall()

                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())

                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = product(root)
    root.mainloop()