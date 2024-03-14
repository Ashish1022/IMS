from tkinter import *
import owner 
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

developer  = owner.developer
class category:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title(f'Inventory Management System | Developed By {developer}')
        self.root.config(bg="white")
        self.root.focus_force()


        #**********Variables*********
        self.var_cat_id = StringVar()
        self.var_name =StringVar()

        #********title********

        lbl_title = Label(self.root,text='Manage Product Category',font=("goudy old style",30),bg='#184a45',fg='white',bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name = Label(self.root,text='Enter Category Name',font=("goudy old style",30),bg='white').place(x=50,y=100)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg='lightyellow').place(x=50,y=170,width=300)


        btn_add = Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg='green',fg='white',cursor='hand2').place(x=360,y=170,width=150,height=30)
        btn_remove = Button(self.root,text="Remove",command=self.delete,font=("goudy old style",15),bg='red',fg='white',cursor='hand2').place(x=520,y=170,width=150,height=30)


        #******category details******

        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly = Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame,columns=("catID","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("catID",text="catID")
        self.categoryTable.heading("name",text="Name")
        


        self.categoryTable["show"] = "headings"

        self.categoryTable.column("catID",width=90)
        self.categoryTable.column("name",width=100)

        self.categoryTable.pack(fill=BOTH,expand=1)

        self.categoryTable.bind("<ButtonRelease-1>",self.getData)

        #*******Images*******
        self.img1 = Image.open('images/cat.jpg')
        self.img1 = self.img1.resize((500,250),Image.BICUBIC)
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.lbl_img1 = Label(self.root,image=self.img1,bd=2,relief=RAISED)
        self.lbl_img1.place(x=50,y=220)


        self.img2 = Image.open('images/category.jpg')
        self.img2 = self.img2.resize((500,250),Image.BICUBIC)
        self.img2 = ImageTk.PhotoImage(self.img2)

        self.lbl_img2 = Label(self.root,image=self.img2,bd=2,relief=RAISED)
        self.lbl_img2.place(x=580,y=220)

        self.show()

    #***********functions**********
    def add(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name required",parent=self.root)
            else:
                cur.execute("SELECT * FROM category where catID=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Categroy already present, try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO category(name) VALUES(?)",(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            
            self.categoryTable.delete(*self.categoryTable.get_children())

            for row in rows:
                self.categoryTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def getData(self,ev):
        f = self.categoryTable.focus()
        content = (self.categoryTable.item(f))
        row = content['values']
        # print(row)
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),


    def delete(self):
        con = sqlite3.connect(database=r'db.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select category from list",parent=self.root)
            else:
                cur.execute("SELECT * FROM category where catID=?",(self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Error please try again.",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM category WHERE catID=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.var_cat_id.set('')
                        self.var_name.set('')
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = category(root)
    root.mainloop()