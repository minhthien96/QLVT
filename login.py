from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Đăng Nhập")
        self.root.geometry("500x700+0+0")
        self.root.config(bg='#fafafa')
        #hình ảnh
        # self.image = ImageTk.PhotoImage(file="login.png")
        # self.lbl_image= Label(self.root,image=self.image,bd=0)
        # self.lbl_image.place(x=200,y=50)
        #Frame
        self.var_nv_id = StringVar()
        self.var_nv_mk = StringVar()
        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg='White')
        login_frame.place(x=80,y=90,width=350,height=460)

        title=Label(login_frame,text="Đăng nhập",font=("Arial",30,'bold'),bg='white')
        title.place(x=0,y=30,relwidth=1)

        lbl_user = Label(login_frame,text="ID nhân viên",font=("Arial",15),bg='white',fg='#767171')
        lbl_user.place(x=50,y=100)

        txt_username = Entry(login_frame,font=('times new roman',15),bg='#ECECEC',textvariable=self.var_nv_id)
        txt_username.place(x=50,y=140,width=250)

        lbl_password = Label(login_frame, text='Mật khẩu', font=("Arial", 15), bg='white', fg='#767171')
        lbl_password.place(x=50, y=200)
        txt_password = Entry(login_frame,show="*",textvariable=self.var_nv_mk, font=('times new roman', 15), bg='#ECECEC')
        txt_password.place(x=50, y=240, width=250)

        btn_login = Button(login_frame,text="Đăng nhập",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",fg='White',activebackground="#00B0F0",activeforeground='white',cursor='hand2')
        btn_login.place(x=50,y=300,width=250,height=35)

        hr= Label(login_frame,bg="lightgray")
        hr.place(x=50,y=370,width=250,height=2)
        or_ = Label(login_frame, fg="lightgray",text="Hoặc",font=('times new romann',15,'bold'),bg='white')
        or_.place(x=150, y=350)

        btn_forget= Button(login_frame,text='Quên mật khẩu?',font=('times new roman',13),bg='white',fg='#00759E',bd=0,activeforeground='#00759E',activebackground='white')
        btn_forget.place(x=120,y=390)


    def login(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_nv_id.get()==""or self.var_nv_mk=="":
                messagebox.showerror('Lỗi','Xin hãy điền đày đủ thông tin',paren=self.root)
            else:
                cur.execute('select Usertype from employee where ID = ? And pass=?', (self.var_nv_id.get(),self.var_nv_mk.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror('Lỗi',"ID hoặc mặt khẩu không chính xác",parent=self.root)
                else:
                    if user == "Admin":
                        self.root.destroy()
                        os.system("python quanlyvattu2.py")
                    else:
                        pass
        except Exception as ex:
            messagebox.showerror('Lỗi',f'Lỗi do {str(ex)}',parent=self.root)






root = Tk()
obj = Login_System(root)
root.mainloop()
