from tkinter import *
from tkinker import messagebox

def btnShow click():
	name: lbName.get()
	messagebox.showinfo("thông báo",name)

frm = Tk()
frm.title("Lập trình tkinter")
lbName= Label(frm,text ="Hoàng Văn Quý")
lbName.pack()

btnShow=Button(frm, text="Xuất",font=("consolas", 14, "blod"),bg="cyan", fg="red", width=20, height=1, command=btnShow_click)
btnShow.pack()
frm.mainloop() 