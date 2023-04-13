#import all the modules
from tkinter import *
from tkinter import messagebox

import sqlite3
import tkinter.messagebox
import datetime
import math

# conn = sqlite3.connect('quanlyvattu.db')
date=datetime.datetime.now().date()
#viet cua so
class App():
    def __init__(self,master,*args,**kwargs):
        self.master = master

        self.left = Frame(master,width=700,height=800,bg='gray')
        self.left.pack(side=LEFT)
        self.right = Frame(master,width=700,height=800,bg='white')
        self.right.pack(side=RIGHT)

        #label
        self.name = Label(self.left, text='Ten sp',font='Arial 15 bold',bg='gray',fg='Blue')
        self.name.place(x=0,y=0)

        self.ID = Label(self.left, text='ID',font='Arial 15 bold',bg='gray',fg='Blue')
        self.ID.place (x=0,y=30)

        self.Serial = Label(self.left, text='Serial', font='Arial 15 bold', bg='gray', fg='Blue')
        self.Serial.place(x=0, y=60)

        self.Model = Label(self.left, text='Model', font='Arial 15 bold', bg='gray', fg='Blue')
        self.Model.place(x=0, y=90)

        self.NSX = Label(self.left, text='NSX', font='Arial 15 bold', bg='gray', fg='Blue')
        self.NSX.place(x=0, y=120)

        self.Time = Label(self.left, text='Thoi gian', font='Arial 15 bold', bg='gray', fg='Blue')
        self.Time.place(x=0, y=150)

        self.Price = Label(self.left, text='Gia', font='Arial 15 bold', bg='gray', fg='Blue')
        self.Price.place(x=0, y=180)

        self.HD = Label(self.left, text='Hop dong', font='Arial 15 bold', bg='gray', fg='Blue')
        self.HD.place(x=0, y=210)

        self.Place = Label(self.left, text='Dia phuong', font='Arial 15 bold', bg='gray', fg='Blue')
        self.Place.place(x=0, y=240)
        #entry
        self.name_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.name_e.place(x=150, y=0)

        self.ID_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.ID_e.place(x=150, y=30)

        self.Serial_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.Serial_e.place(x=150, y=60)

        self.Model_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.Model_e.place(x=150, y=90)

        self.NSX_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.NSX_e.place(x=150, y=120)

        self.Time_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.Time_e.place(x=150, y=150)

        self.Price_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.Price_e.place(x=150, y=180)

        self.HD_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.HD_e.place(x=150, y=210)

        self.Place_e = Entry(self.left, width=25, font=('arial 15'), bg='lightblue')
        self.Place_e.place(x=150, y=240)
        # button
        self.add = Button(self.left, text='add', font='Arial 15 bold', bg='gray', fg='Blue', width=5, command=self.add)
        self.add.place(x=0, y=300)
        self.clear = Button(self.left, text='clear', font='Arial 15 bold', bg='gray', fg='Blue', width=5,
                            command=self.clear)
        self.clear.place(x=200, y=300)
        self.remove = Button(self.left, text='remove', font='Arial 15 bold', bg='gray', fg='Blue', width=5,
                             command=self.remove)
        self.remove.place(x=300, y=300)
        self.update = Button(self.left, text='update', font='Arial 15 bold', bg='gray', fg='Blue', width=5,
                             command=self.update)
        self.update.place(x=100, y=300)
    def add(self,*args,**kwargs):
        self.name = self.name_e.get()
        self.ID = self.ID_e.get()
        self.Serial = self.Serial_e.get()
        self.Model = self.Model_e.get()
        self.NSX = self.NSX_e.get()
        self.Time = self.Time_e.get()
        self.Price = self.Price_e.get()
        self.HD = self.HD_e.get()
        self.Place = self.Place_e.get()
        if (self.name == "" or self.ID == "" or self.Serial == "" or self.Model == "" or self.NSX == "" or self.Time == "" or self.Price == "" or self.HD == "" or self.Place == ""):
            messagebox.showinfo("add thong tin","can them cac thong tin vao o trong")
        else:
            self.conn = sqlite3.connect(host='localhost',user = 'root',database='QLVT')
            self.cursor = self.conn.cursor()
            self.cursor.execute("insert into QLVT values('"+self.name+"','"+self.ID+"','"+self.Serial+"','"+self.Model+"','"+self.NSX+"','"+self.Time+"','"+self.Price+"','"+self.HD+"'.'"+self.Place+"')")
            self.cursor.execute("commit")
            messagebox.showinfo("add status","add thanh cong")
            self.conn.close()
            #xoa entry
            self.name_e.delete(0,'end')
            self.ID_e.delete(0, 'end')
            self.Serial_e.delete(0, 'end')
            self.Model_e.delete(0, 'end')
            self.NSX_e.delete(0, 'end')
            self.Time_e.delete(0, 'end')
            self.Price_e.delete(0, 'end')
            self.HD_e.delete(0, 'end')
            self.Place_e.delete(0, 'end')
    def remove(self,*args,**kwargs):
        if (self.name_e.get() ==""):
            messagebox.showinfo("remove thong tin","them thong tin vao")
        else:
            self.conn = sqlite3.connect(host='localhost',user = 'root',database='QLVT')
            self.cursor = self.conn.cursor()
            self.cursor.execute("delete from QLVT where name='"+self.name_e.get()+"'")
            self.cursor.execute("commit")
            messagebox.showinfo("remove status","da remove thanh cong")
            self.conn.close()

            self.name_e.delete(0,'end')

    def update(self,*args,**kwargs):
        self.name = self.name_e.get()
        self.ID = self.ID_e.get()
        self.Serial = self.Serial_e.get()
        self.Model = self.Model_e.get()
        self.NSX = self.NSX_e.get()
        self.Time = self.Time_e.get()
        self.Price = self.Price_e.get()
        self.HD = self.HD_e.get()
        self.Place = self.Place_e.get()
        if (self.name == "" or self.ID == "" or self.Serial == "" or self.Model == "" or self.NSX == "" or self.Time == "" or self.Price == "" or self.HD == "" or self.Place == ""):
            messagebox.showinfo("update thong tin","nhap thong tin can update")
        else:
            self.conn = sqlite3.connect(host='localhost',user = 'root', database='QLVT')
            self.cursor = self.conn.cursor()
            self.cursor.execute("update QLVT set name = '"+self.name+"', Serial='"+self.Serial+"', Model ='"+self.Model+"', NSX ='"+self.NSX+"', Time='"+self.Time+"', HD='"+self.HD+"', Price='"+self.Price+"',Place='"+self.Place+"'where ID='"+self.ID+"'")
            self.cursor.execute("commit")
            messagebox.showinfo("update status","update thanh cong")
            self.conn.close()
            # xoa entry
            self.name_e.delete(0, 'end')
            self.ID_e.delete(0, 'end')
            self.Serial_e.delete(0, 'end')
            self.Model_e.delete(0, 'end')
            self.NSX_e.delete(0, 'end')
            self.Time_e.delete(0, 'end')
            self.Price_e.delete(0, 'end')
            self.HD_e.delete(0, 'end')
            self.Place_e.delete(0, 'end')
    def clear(self,*args,**kwargs):
        self.name_e.delete(0, 'end')
        self.ID_e.delete(0, 'end')
        self.Serial_e.delete(0, 'end')
        self.Model_e.delete(0, 'end')
        self.NSX_e.delete(0, 'end')
        self.Time_e.delete(0, 'end')
        self.Price_e.delete(0, 'end')
        self.HD_e.delete(0, 'end')
        self.Place_e.delete(0, 'end')

root=Tk()
App(root)
root.geometry("1366x768+0+0")
root.title("QUẢN LÝ VẬT TƯ")
root.mainloop()



