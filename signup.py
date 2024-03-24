from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import pymysql


def back():
   reg_window.destroy()
   import login


def clear():
    username.delete(0,END)
    password.delete(0,END)
    confirm_password.delete(0,END)


def connect_database():
  if username.get()=='' or password.get()=='' or confirm_password.get()==''or Ulam.get()=='':
    messagebox.showerror('Error!','Please Input all Field')
  elif password.get() != confirm_password.get():
    messagebox.showerror('Error!','Password missmatch!') 
  else:
    try:
        con=pymysql.connect(host='localhost',user='root',password='1234',database='Lipongdata')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error!','Database Connectivity Issue, Please try Again')
        return
    try:
        query='use Lipongdata'
        mycursor.execute(query)
    except:
        mycursor.execute('use Lipongdata')

    query='select * from data where username=%s'
    mycursor.execute(query,(username.get()))

    row=mycursor.fetchone()
    if row !=None:
      messagebox.showerror('Error!!','Username Already exists!')

    else:
      query='insert into data(username,password,Ulamnya) values(%s,%s,%s)'
      mycursor.execute(query,(username.get(),password.get(),Ulam.get()))
      con.commit()
      con.close()
      messagebox.showinfo('Success!','Registered Successfully!')
      clear()
      reg_window.destroy()
      import login
    

    
reg_window=Tk()
reg_window.title("Registration")
reg_window.geometry('925x550')
reg_window.config(bg='white')
reg_window.resizable(False, False)

icon = PhotoImage(file='hyy.png')
reg_window.iconphoto(True, icon)

Username = StringVar()
Password = StringVar()
Confirm_Password = StringVar()

#-----REGISTRATIONFORM--------#
img=PhotoImage(file='vector.png')
user_img=ImageTk.PhotoImage(file='user.png')
entry_frame1=ImageTk.PhotoImage(file='entry.png')
code_img=ImageTk.PhotoImage(file='code.png')
entry_frame2=ImageTk.PhotoImage(file='entry.png')
entry_frame3=ImageTk.PhotoImage(file='entry.png')
signup_btn=ImageTk.PhotoImage(file='signup_btn.png')

reg_frame=Frame(reg_window, width=925, height=550, bg='white')
reg_frame.pack(expand=True)

mgalipong_label=Label(reg_frame, text='MGA LIPONG REGISTRATION FORM', fg='black', bg='white', font=('times new roman', 29, 'bold')).place(x=100, y=5)

Label(reg_frame, image=img, width=450, height=450, bg='white').place(x=40, y=70)

frame=Frame(reg_frame, width=390, height=400, bg='white')
frame.place(x=500, y=105)

heading=Label(frame, text='Registration Form', fg='purple', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=60, y=5)

Label(frame, image=user_img, bg='white').place(x=30, y=93)

Label(frame, image=entry_frame1, border=0, bg='white').place(x=60, y=90)
username=Entry(frame, textvariable=Username, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
username.place(x=80, y=97)

def user(event):
  if username.get()=='Username':
    username.delete(0,END)

def pass_entry(event):
  if password.get()=='Password':
   password.delete(0,END)

def confirm_entry(event):
  if confirm_password.get()=='Confirm Your Password':
   confirm_password.delete(0,END)

username.insert(0,'Username')

username.bind('<FocusIn>',user)

Label(frame, image=code_img, bg='white').place(x=30, y=153)

Label(frame, image=entry_frame2, border=0, bg='white').place(x=60, y=150)
password=Entry(frame, textvariable=Password, width=30, show="", fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
password.place(x=80, y=156)

password.insert(0,'Password')

password.bind('<FocusIn>',pass_entry)

Label(frame, image=code_img, bg='white').place(x=30, y=213)

Label(frame, image=entry_frame3, border=0, bg='white').place(x=60, y=210)
confirm_password=Entry(frame, textvariable=Confirm_Password, width=30, show="•", fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_password.place(x=80, y=216)

confirm_password.insert(0,'Confirm Your Password')

confirm_password.bind('<FocusIn>',confirm_entry)

#--------Security-----------#
question=Label(frame,text="Security Questions:",font=("times new roman",15,"bold"),bg="white",fg="magenta").place(x=130,y=270)

Ulam=Label(frame,text="Ano ulam mo?",font=("times new roman",12,"bold"),bg="white",fg="magenta").place(x=30,y=302,width=150)
Ulam=Entry(frame, textvariable=Ulam,border=1,bg='white')
Ulam.place(x=160,y=305)


def show():
        hide_button=Button(frame, pady=0, image=hide_image, command=hide, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
        hide_button.place(x=330, y=217)
        confirm_password.config(show='')

def hide():
        show_button=Button(frame, pady=0, image=show_image, command=show, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
        show_button.place(x=330, y=217)
        confirm_password.config(show='•')

show_image=ImageTk.PhotoImage(file='show .png')
hide_image=ImageTk.PhotoImage(file='hide.png')

show_button=Button(frame, pady=0, image=show_image, command=show, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
show_button.place(x=330, y=217)

Button(frame, image=signup_btn, bg='white', border=0, command=connect_database).place(x=150, y=350)

alreadyaccount=Label(frame, text='Already Have an Account?', font=('open Sans', '9', 'bold'), bg='white', fg='firebrick')
alreadyaccount.place(x=110,y=380)

loginButton=Button(frame, text='Login', font=('Open Sans','9', 'bold underline'), bg='white', fg='blue',bd='0',cursor='hand2',activebackground='white',activeforeground='blue',command=back)
loginButton.place(x=260,y=380)



reg_window.mainloop()
