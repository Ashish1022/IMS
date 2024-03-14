from tkinter import *
from PIL import ImageTk,Image
import owner 
from employee import employee
from supplier import supplier
from category import category
from product import product
from sales import sales


developer  = owner.developer
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1368x768+0+0")
        self.root.title(f'Inventory Management System | Developed By {developer}')
        self.root.config(bg="white")

        #*********title*********
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#9DBC98",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #**********btn-logout**********
        btn_logout = Button(self.root,text="Logout",highlightbackground="red",font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1200,y=10,height=40,width=110)

        #**********clock**********
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD/MM/YY\t\t Time: HH:MM:SS",compound=LEFT,font=("times new roman",15),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #********Left Menu********
        self.left_MenuIcon = Image.open("images/menu_im.png")
        self.left_MenuIcon = self.left_MenuIcon.resize((200,200),Image.BICUBIC)
        self.left_MenuIcon = ImageTk.PhotoImage(self.left_MenuIcon)

        left_menu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_menu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo = Label(left_menu,image=self.left_MenuIcon)
        lbl_menuLogo.pack(side=TOP,fill=X)


        self.icon_side=PhotoImage(file="images/side.png")

        btn_menu = Label(left_menu,text="Menu",font=("times new roman",20),bg="#557C55").pack(side=TOP,fill=X)


        btn_employee = Button(left_menu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)
        btn_supplier = Button(left_menu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)
        btn_category = Button(left_menu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)
        btn_product = Button(left_menu,text="Product",command=self.products,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)
        btn_sales = Button(left_menu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)
        btn_Exit = Button(left_menu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",bd=3).pack(side=TOP,fill=X)


        #**********Content**********
        self.lbl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#F8DE22",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#CECE5A",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=650,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFB07F",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#0079FF",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#F31559",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        
        #**********Footer**********
        lbl_footer = Label(self.root,text=f"IMS-Inventory Management System | Developed by {developer}\nFor any technical issue Contact: xxxxxxxxxx",compound=LEFT,font=("times new roman",12),bg="#4D636D",fg="white").pack(side=BOTTOM,fill=X)


    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employee(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplier(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = category(self.new_win)

    def products(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = product(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = sales(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()