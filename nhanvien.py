#import all the modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
import math

class nhanvien:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Nhân Viên")
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()

        #tất cả biến
        self.var_searchby= StringVar()
        self.var_searchtxt = StringVar()


        self.var_nv_id = StringVar()
        self.var_nv_ten = StringVar()
        self.var_nv_email = StringVar()
        self.var_nv_diachi = StringVar()
        self.var_nv_gt = StringVar()
        self.var_nv_sdt = StringVar()
        self.var_nv_mk = StringVar()
        self.var_usertyp = StringVar()
        self.var_luong = StringVar()

        #bảng tìm kiếm
        timkiem=LabelFrame(self.root,text="Tìm kiếm",bg='white',font=('arial',12,'bold'),bd=2,relief=RIDGE)
        timkiem.place(x=250,y=20,width=600,height=70)

        #option
        cmb_timkiem = ttk.Combobox(timkiem,textvariable=self.var_searchby,values=("Lựa chọn","Email","Ten","ID"),state='readonly',justify=CENTER,font=("time new roman",15,'bold'))
        cmb_timkiem.place(x=10,y=10,width=180)
        cmb_timkiem.current(0)

        txt_timkiem = Entry(timkiem,textvariable=self.var_searchtxt,font=('arial',15),bg='lightyellow')
        txt_timkiem.place(x=200,y=10)
        btn_timkiem = Button(timkiem,text='Tìm kiếm',command=self.search,font=('arial',15,'bold'),bg='#4caf50',fg='white')
        btn_timkiem.place(x=430,y=10,width=150,height=30)
        #tilte
        title = Label(self.root,text="Thông tin nhân viên",font=('times new roman', 15,'bold'),bg="yellow",fg='#DC143C')
        title.place(x=50,y=100,width=1000)
        #nội dung
        #dòng 1
        lbl_nvid = Label(self.root,text="ID:",font=('times new roman', 15,'bold'),bg="white")
        lbl_nvid.place(x=50,y=150)
        lbl_gt = Label(self.root, text="Giới tính:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_gt.place(x=350, y=150)
        lbl_sdt = Label(self.root, text="SĐT:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_sdt.place(x=650, y=150)

        txt_nvid = Entry(self.root,textvariable=self.var_nv_id,font=('times new roman', 15, 'bold'), bg="lightyellow")
        txt_nvid.place(x=100, y=150,width=150)
        # txt_gt = Entry(self.root,textvariable=self.var_nv_gt,font=('times new roman', 15, 'bold'), bg="white")
        # txt_gt.place(x=440, y=150,width=150)
        cmb_gt = ttk.Combobox(self.root, textvariable=self.var_nv_gt,values=("Lựa chọn", "Nam", "Nữ", "Khác"), state='readonly',justify=CENTER, font=("time new roman", 13))
        cmb_gt.place(x=440, y=150, width=150)
        cmb_gt.current(0)
        txt_sdt =Entry(self.root,textvariable=self.var_nv_sdt, font=('times new roman', 15, 'bold'),bg="lightyellow")
        txt_sdt.place(x=710, y=150,width=150)
        #dòng 2
        lbl_nvten = Label(self.root, text="Tên:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_nvten.place(x=50, y=200)
        lbl_mk = Label(self.root, text="Mật khẩu:",font=('times new roman', 15, 'bold'), bg="white")
        lbl_mk.place(x=350, y=200)
        lbl_email = Label(self.root, text="Email:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_email.place(x=650, y=200)

        txt_nvten = Entry(self.root, textvariable=self.var_nv_ten, font=('times new roman', 15, 'bold'), bg="lightyellow")
        txt_nvten.place(x=100, y=200, width=150)
        txt_mk = Entry(self.root, textvariable=self.var_nv_mk,font=('times new roman', 15, 'bold'), bg="lightyellow",show='*')
        txt_mk.place(x=440, y=200, width=150)
        txt_email = Entry(self.root, textvariable=self.var_nv_email, font=('times new roman', 15, 'bold'), bg="lightyellow")
        txt_email.place(x=710, y=200,width=150)
        # dòng 3
        lbl_nvdiachi = Label(self.root, text="Địa chỉ:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_nvdiachi.place(x=50, y=250)
        lbl_luong = Label(self.root, text="Lương:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_luong.place(x=450, y=250)
        lbl_usertype = Label(self.root, text="User Type:", font=('times new roman', 15, 'bold'), bg="white")
        lbl_usertype.place(x=750, y=250)

        self.txt_nvdiachi = Text(self.root, font=('times new roman', 15, 'bold'),bg="lightyellow")
        self.txt_nvdiachi.place(x=130, y=250, width=300,height=100)
        txt_luong = Entry(self.root, textvariable=self.var_luong, font=('times new roman', 15, 'bold'),bg="lightyellow")
        txt_luong.place(x=520, y=250, width=180)
        # txt_usertype = Entry(self.root, textvariable=self.var_usertyp, font=('times new roman', 15, 'bold'),bg="lightyellow")
        # txt_usertype.place(x=440, y=200, width=150)
        cmb_usertype = ttk.Combobox(self.root,textvariable=self.var_usertyp, values=("Lựa chọn", "Admin", "User"),state='readonly', justify=CENTER, font=("time new roman", 13))
        cmb_usertype.place(x=860, y=250, width=150)
        cmb_usertype.current(0)
        #button
        btn_add = Button(self.root,text='Thêm',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white')
        btn_add.place(x=500,y=320,width=110,height=28)
        btn_update = Button(self.root,command=self.update, text='Cập nhật', font=('goudy old style', 15), bg='red', fg='white')
        btn_update.place(x=650, y=320, width=110, height=28)
        btn_delete = Button(self.root,command=self.delete, text='Xóa', font=('goudy old style', 15), bg='green', fg='white')
        btn_delete.place(x=800, y=320, width=110, height=28)
        btn_clear = Button(self.root,command=self.clear, text='Clear', font=('goudy old style', 15), bg='black', fg='white')
        btn_clear.place(x=950, y=320, width=110, height=28)

        #bảng
        nv_frame = Frame(self.root,bd=3,relief=RIDGE)
        nv_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly = Scrollbar(nv_frame,orient=VERTICAL)
        scrollx = Scrollbar(nv_frame, orient=HORIZONTAL)

        self.nv_bang = ttk.Treeview(nv_frame,columns=("ID",'Tên','SĐT','Giới tính','Địa chỉ','Email','Lương','User type'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.nv_bang.yview)
        scrollx.config(command=self.nv_bang.xview)

        self.nv_bang.heading("ID",text="ID")
        self.nv_bang.heading("Tên", text="Họ và Tên")
        self.nv_bang.heading("SĐT", text="SĐT")
        self.nv_bang.heading("Giới tính", text="Giới tính")
        self.nv_bang.heading("Địa chỉ", text="Địa chỉ")
        self.nv_bang.heading("Email", text="Email")
        self.nv_bang.heading("Lương", text="Lương")
        self.nv_bang.heading("User type", text="User type")
        self.nv_bang['show']='headings'
        #--------------------
        self.nv_bang.column("ID",width=90)
        self.nv_bang.column("Tên",width=190)
        self.nv_bang.column("SĐT",width=190)
        self.nv_bang.column("Giới tính",width=190)
        self.nv_bang.column("Địa chỉ",width=190)
        self.nv_bang.column("Email",width=190)
        self.nv_bang.column("Lương",width=190)
        self.nv_bang.column("User type",width=190)
        self.nv_bang.pack(fill=BOTH,expand=1)
        self.nv_bang.bind('<ButtonRelease-1>',self.get_data)
        self.show()
        #==========================

    def add(self):
        con=sqlite3.connect('ims.db')
        cur=con.cursor()
        try:
            if self.var_nv_id.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin vào chỗ trống',parent=self.root)
            else:
                cur.execute("Select * from employee where ID=?",(self.var_nv_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Lỗi','ID này đã tồn tại, hãy nhập một ID khác',parent=self.root)
                else:
                    cur.execute('Insert into employee (ID,Ten,Sdt,GT,diachi,Email,Luong,Usertype,pass) values(?,?,?,?,?,?,?,?,?)',
                                (   self.var_nv_id.get(),
                                    self.var_nv_ten.get(),
                                    self.var_nv_sdt.get(),
                                    self.var_nv_gt.get(),
                                    self.txt_nvdiachi.get('1.0',END),
                                    self.var_nv_email.get(),
                                    self.var_luong.get(),
                                    self.var_usertyp.get(),
                                    self.var_nv_mk.get()
                                ))
                    con.commit()
                    messagebox.showinfo('Thành công','Nhập thông tin nhân viên thành công',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Lỗi',f'Lỗi vì : {str(ex)}',parent=self.root)

    def show(self):
        con = sqlite3.connect('ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.nv_bang.delete(*self.nv_bang.get_children())
            for row in rows:
                self.nv_bang.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Lỗi', f'Lỗi vì : {str(ex)}', parent=self.root)

    def update(self):
        con=sqlite3.connect('ims.db')
        cur=con.cursor()
        try:
            if self.var_nv_id.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin vào chỗ trống',parent=self.root)
            else:
                cur.execute("Select * from employee where ID=?",(self.var_nv_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Lỗi','Lỗi không tìm thấy dữ liệu',parent=self.root)
                else:
                    cur.execute('Update employee set Ten=?,Sdt=?,GT=?,diachi=?,Email=?,Luong=?,Usertype=?,pass = ? where ID=?',
                                (
                                    self.var_nv_ten.get(),
                                    self.var_nv_sdt.get(),
                                    self.var_nv_gt.get(),
                                    self.txt_nvdiachi.get('1.0',END),
                                    self.var_nv_email.get(),
                                    self.var_luong.get(),
                                    self.var_usertyp.get(),
                                    self.var_nv_mk.get(),
                                    self.var_nv_id.get()

                                ))
                    con.commit()
                    messagebox.showinfo('Thành công','Cập nhât thông tin nhân viên thành công',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Lỗi',f'Lỗi vì : {str(ex)}',parent=self.root)

    def delete(self):
        con=sqlite3.connect('ims.db')
        cur=con.cursor()
        try:
            if self.var_nv_id.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin vào chỗ trống',parent=self.root)
            else:
                cur.execute("Select * from employee where ID=?",(self.var_nv_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Lỗi','Lỗi không tìm thấy dữ liệu',parent=self.root)
                else:
                    op=messagebox.askyesno("Xác nhận",'Bạn thât sự muốn xóa thông tin này',parent=self.root)
                    if op == True:
                        cur.execute('delete from employee where ID=?',(self.var_nv_id.get(),))
                        con.commit()
                        messagebox.showinfo('Xóa','Đã xóa thành công',parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Lỗi', f'Lỗi vì : {str(ex)}', parent=self.root)

    def get_data(self,ev):
        f=self.nv_bang.focus()
        content=(self.nv_bang.item(f))
        row=content['values']
        # print(row)
        self.var_nv_id.set(row[0])
        self.var_nv_ten.set(row[1])
        self.var_nv_sdt.set(row[2])
        self.var_nv_gt.set(row[3])
        self.txt_nvdiachi.delete('1.0',END)
        self.txt_nvdiachi.insert(END,row[4])
        self.var_nv_email.set(row[5])
        self.var_luong.set(row[6])
        self.var_usertyp.set(row[7])

    def clear(self):
        self.var_nv_id.set('')
        self.var_nv_ten.set('')
        self.var_nv_sdt.set('')
        self.var_nv_gt.set('Lựa chọn')
        self.txt_nvdiachi.delete('1.0', END)
        self.var_nv_email.set('')
        self.var_luong.set('')
        self.var_usertyp.set('Admin')
        self.var_searchtxt.set('')
        self.var_searchby.set('Lựa chọn')
        self.show()

    def search(self):
        con = sqlite3.connect('ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Lựa chọn":
                messagebox.showerror('Lỗi','Hãy lựa chọn thông tin cần tìm',parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin cần tìm',parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows) !=0:
                    self.nv_bang.delete(*self.nv_bang.get_children())
                    for row in rows:
                        self.nv_bang.insert('',END,values=row)
                else:
                    messagebox.showerror("Lỗi","Không có thông tin tìm kiếm",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Lỗi', f'Lỗi vì : {str(ex)}', parent=self.root)


if __name__ =="__main__":
    root= Tk()
    obj = nhanvien(root)
    root.mainloop()