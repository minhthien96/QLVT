#import all the modules
from tkinter import *
from tkinter import messagebox
from nhanvien import nhanvien
from sanpham import sanpham
# from login import Login_System
import os

import sqlite3
import tkinter.messagebox
import datetime
import math
import time




class app:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Quản lý vật tư")
        self.root.config(bg="#FFFFFF")
        #title
        title = Label(self.root,text="QUẢN LÝ VẬT TƯ",font=('times new roman', 40,'bold'),bg="#6A5ACD",fg='#DC143C',padx=20,anchor='w')
        title.place(x=0,y=0,relwidth=1,height=70)
        # nut đăng xuất
        btn_logout=Button(self.root,text='Logout',command=self.logout,font=('times new roman',15,'bold'),bg='#FFFF00')
        btn_logout.place(x=1150,y=20,height=30,width=150)
        #thời gian
        self.clock = Label(self.root,text="Chào mừng bạn tới quản lý vật tư\t\t Ngảy tháng:DD-MM-YYYY\t\t Thời gian: HH:MM:SS",font=('times new roman', 15),bg="#000000",fg='#ADFF2F',padx=20,anchor='w')
        self.clock.place(x=0,y=70,relwidth=1,height=30)
        #bảng tùy chọn
        leftmenu = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        leftmenu.place(x=0,y=102,width=200,height=565)
        Label_menu = Label(leftmenu,text='Bảng tùy chọn',font=('times new roman',20,'bold'),bg="black",fg='#DC143C')
        Label_menu.pack(side=TOP,fill=X)
        btn_nv= Button(leftmenu, text='Nhân viên',command=self.nhanvien,font=('times new roman',25, 'bold'), bg="white",fg='black')
        btn_nv.pack(side=TOP,fill=X)
        btn_ncc = Button(leftmenu, text='Nhà cung cấp', font=('times new roman', 25, 'bold'), bg="white", fg='black')
        btn_ncc.pack(side=TOP,fill=X)
        btn_SP = Button(leftmenu, text='Các sản phẩm',command=self.sanpham, font=('times new roman', 25, 'bold'), bg="white", fg='black')
        btn_SP.pack(side=TOP,fill=X)
        btn_search = Button(leftmenu, text='Tìm kiếm', font=('times new roman', 25, 'bold'), bg="white",fg='black')
        btn_search.pack(side=TOP,fill=X)
        btn_import =Button(leftmenu, text='Import', font=('times new roman', 25, 'bold'), bg="white", fg='black')
        btn_import.pack(side=TOP,fill=X)
        btn_export =Button(leftmenu, text='Export', font=('times new roman', 25, 'bold'), bg="white", fg='black')
        btn_export.pack(side=TOP,fill=X)
        def times():
            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.clock.config(text=f"Chào mừng tới hệ thống Quản lý vật tư \t\t Ngày tháng:{str(date_)}\t\t Thời gian: {str(time_)}")
            self.clock.after(1000,times)
        times()
    def logout(self):
        self.root.destroy()
        os.system('python login.py')
    # def update_content(self):
    #     con=sqlite3.connect(database='ims.db')
    #     cur=con.cursor()
    #     try:
    #     cur.execute("select * employee")
    #     employee = cur.fetchall()
    #     self.


#==============================
    def nhanvien(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = nhanvien(self.new_win)

    def sanpham(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = sanpham(self.new_win)

    # def Login_system(self):
    #     pass

if __name__ =="__main__":
    root= Tk()
    obj = app(root)
    root.mainloop()