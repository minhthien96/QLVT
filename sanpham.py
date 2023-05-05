#import all the modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
import tkinter.messagebox
import datetime
import math

class sanpham:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sản phẩm")
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()

        #tất cả các biến
        self.var_stt = StringVar()
        self.var_serial = StringVar()
        self.var_model = StringVar()
        self.var_NSX = StringVar()
        self.var_tgm = StringVar()
        self.var_gia = StringVar()
        self.var_hopdong = StringVar()
        self.var_dp = StringVar()
        self.var_timkiemby = StringVar()
        self.var_timkiemtxt = StringVar()
        #==================================
        sanpham_frame= Frame(self.root,bd=2,relief=RIDGE,bg='White')
        sanpham_frame.place(x=10,y=10,width=450,height=480)

        #tilte
        title = Label(sanpham_frame,text="Thông tin sản phẩm",font=('Arial', 18),bg="#0f4d7d",fg='white')
        title.pack(side=TOP,fill=X)

        #Label
        stt= Label(sanpham_frame,text='Mã sản phẩm:',font=('Arial',12,'bold'))
        stt.place(x=10,y=50)
        serial = Label(sanpham_frame, text='Serial:', font=('Arial',12,'bold'))
        serial.place(x=10, y=90)
        model = Label(sanpham_frame, text='Model:', font=('Arial',12,'bold'))
        model.place(x=10, y=130)
        NSX = Label(sanpham_frame, text='Nhà sản xuất:', font=('Arial',12,'bold'))
        NSX.place(x=10, y=170)
        tgm = Label(sanpham_frame, text='Thời gian mua:', font=('Arial',12,'bold'))
        tgm.place(x=10, y=210)
        gia = Label(sanpham_frame, text='Giá tiền:', font=('Arial',12,'bold'))
        gia.place(x=10, y=250)
        hopdong = Label(sanpham_frame, text='Hợp đồng:', font=('Arial',12,'bold'))
        hopdong.place(x=10, y=290)
        dp = Label(sanpham_frame, text='Địa phương sử dụng:', font=('Arial',12,'bold'))
        dp.place(x=10, y=330)

        #Entry
        e_stt = Entry(self.root,textvariable=self.var_stt,font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_stt.place(x=150, y=60,width=300)
        e_serial = Entry(self.root, textvariable=self.var_serial, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_serial.place(x=150, y=100, width=300)
        e_model = Entry(self.root, textvariable=self.var_model, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_model.place(x=150, y=140, width=300)
        e_NSX = Entry(self.root, textvariable=self.var_NSX, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_NSX.place(x=150, y=180, width=300)
        e_tgm = DateEntry(self.root, textvariable=self.var_tgm,selectmode='day',font=('Arial',15))
        e_tgm.place(x=150, y=220, width=150)
        e_gia = Entry(self.root, textvariable=self.var_gia, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_gia.place(x=150, y=260, width=300)
        e_hopdong = Entry(self.root, textvariable=self.var_hopdong, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_hopdong.place(x=150, y=300, width=300)
        e_dp = Entry(self.root, textvariable=self.var_dp, font=('times new roman', 15, 'bold'), bg="lightyellow")
        e_dp.place(x=200, y=340, width=250)

        #button
        btn_add = Button(self.root, text='Thêm', font=('times new roman', 15), bg='#2196f3', fg='white')
        btn_add.place(x=20, y=420, width=90, height=28)
        btn_update = Button(self.root,  text='Cập nhật', font=('times new roman', 15), bg='red', fg='white')
        btn_update.place(x=130, y=420, width=90, height=28)
        btn_delete = Button(self.root,  text='Xóa', font=('times new roman', 15), bg='green', fg='white')
        btn_delete.place(x=240, y=420, width=90, height=28)
        btn_clear = Button(self.root, text='Clear', font=('times new roman', 15), bg='black', fg='white')
        btn_clear.place(x=350, y=420, width=90, height=28)

        #search box
        timkiem = LabelFrame(self.root, text="Tìm kiếm", bg='white', font=('arial', 12, 'bold'), bd=2, relief=RIDGE)
        timkiem.place(x=480, y=5, width=600, height=90)

        #combo box search
        cmb_timkiem = ttk.Combobox(timkiem,textvariable=self.var_timkiemby,values=("Lựa chọn","NSX","Model","Serial","Tên sản phẩm"),state='readonly',justify=CENTER,font=("time new roman",15,'bold'))
        cmb_timkiem.place(x=10,y=20,width=150)
        cmb_timkiem.current(0)

        txt_timkiem = Entry(timkiem,textvariable=self.var_timkiemtxt,font=('arial',15),bg='lightyellow')
        txt_timkiem.place(x=190,y=20)
        btn_timkiem = Button(timkiem,text='Tìm kiếm',font=('arial',15),bg='#4caf50',fg='white')
        btn_timkiem.place(x=430,y=20,width=150,height=30)

        #bảng
        sp_frame = Frame(self.root,bd=3,relief=RIDGE)
        sp_frame.place(x=480,y=110,width=600,height=380)

        scrolly = Scrollbar(sp_frame,orient=VERTICAL)
        scrollx = Scrollbar(sp_frame, orient=HORIZONTAL)

        self.sp_bang = ttk.Treeview(sp_frame,columns=("STT","Tên sp",'Serial','Model','NSX','Thời gian','Giá','Hợp đồng','Địa phương'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sp_bang.yview)
        scrollx.config(command=self.sp_bang.xview)

        self.sp_bang.heading("STT",text="STT")
        self.sp_bang.heading("Tên sp",text="Tên sản phẩm")
        self.sp_bang.heading("Serial", text="Serial")
        self.sp_bang.heading("Model", text="Model")
        self.sp_bang.heading("NSX", text="NSX")
        self.sp_bang.heading("Thời gian", text="Thời gian")
        self.sp_bang.heading("Giá", text="Giá")
        self.sp_bang.heading("Hợp đồng", text="Hợp đồng")
        self.sp_bang.heading("Địa phương", text="Địa phương")
        self.sp_bang['show']='headings'
        #--------------------
        self.sp_bang.column("STT",width=90)
        self.sp_bang.column("Tên sp", width=100)
        self.sp_bang.column("Serial",width=100)
        self.sp_bang.column("Model",width=100)
        self.sp_bang.column("NSX",width=100)
        self.sp_bang.column("Thời gian",width=100)
        self.sp_bang.column("Giá",width=100)
        self.sp_bang.column("Hợp đồng",width=100)
        self.sp_bang.column('Địa phương',width=100)
        self.sp_bang.pack(fill=BOTH,expand=1)
        # self.sp_bang.bind('<ButtonRelease-1>',self.get_data)
        # self.show()
        #========================================
    def add(self):
        con=sqlite3.connect('ims.db')
        cur=con.cursor()
        try:
            if self.var_serial.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin vào chỗ trống',parent=self.root)
            else:
                cur.execute("Select * from employee where Serial=?",(self.var_stt.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Lỗi','Serial này đã tồn tại, hãy nhập một Serial khác',parent=self.root)
                else:
                    cur.execute('Insert into Employee (ID,Ten,Sdt,GT,diachi,Email,Luong,Usertype) values(?,?,?,?,?,?,?,?)',
                                (   self.var_stt.get(),
                                    self.var_serial.get(),
                                    self.var_model.get(),
                                    self.var_NSX.get(),
                                    self.var_tgm.get(),
                                    self.var_gia.get(),
                                    self.var_hopdong.get(),
                                    self.var_dp.get()
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
            self.sp_bang.delete(*self.sp_bang.get_children())
            for row in rows:
                self.sp_bang.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Lỗi', f'Lỗi vì : {str(ex)}', parent=self.root)

    def update(self):
        con=sqlite3.connect('ims.db')
        cur=con.cursor()
        try:
            if self.var_serial.get()=="":
                messagebox.showerror('Lỗi','Hãy điền thông tin vào chỗ trống',parent=self.root)
            else:
                cur.execute("Select * from employee where ID=?",(self.var_serial.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Lỗi','Lỗi không tìm thấy dữ liệu',parent=self.root)
                else:
                    cur.execute('Update Employee set Ten=?,Sdt=?,GT=?,diachi=?,Email=?,Luong=?,Usertype=? where ID=?',
                                (
                                    self.var_stt.get(),
                                    self.var_serial.get(),
                                    self.var_model.get(),
                                    self.var_NSX.get(),
                                    self.var_tgm.get(),
                                    self.var_gia.get(),
                                    self.var_hopdong.get(),
                                    self.var_dp.get()
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
                        cur.execute('delete from Employee where ID=?',(self.var_nv_id.get(),))
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
                cur.execute("select * from Employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows) !=0:
                    self.nv_bang.delete(*self.nv_bang.get_children())
                    for row in rows:
                        self.nv_bang.insert('',END,values=row)
                else:
                    messagebox.showerror("Lỗi","Không có thông tin tìm kiếm",parent=self.root)
        except Exception as ex:
            messagebox.showerror('Lỗi', f'Lỗi vì : {str(ex)}', parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = sanpham(root)
    root.mainloop()