from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

w=Tk()

w.title('WELCOME')
w.resizable(0,0)

icon = PhotoImage(file='hyy.png')
w.iconphoto(True, icon)
w.title=('Welcome')

width_of_window=427
height_of_window=250
screen_width=w.winfo_screenwidth()
screen_height=w.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))

q=ttk.Style()
q.theme_use('clam')
q.configure("red.Horizontal.TProgressbar",foreground='red',background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')

def bar():
            l4=Label(w,text="Loading...",fg='white',bg='#249794')
            lst4=('Calibri(Body)',10)
            l4.configure(font=lst4)
            l4.place(x=0,y=210)

            import time
            r=0
            for i in range(100):
                progress['value']=r
                w.update_idletasks()
                time.sleep(0.03)
                r=r+1
            w.destroy()
            
       

progress.place(x=-10,y=235)

def main():
    root=Tk()
    root.title('LoginPage')
    root.geometry('925x550')
    root.configure(bg='white')
    root.resizable(False, False)

    icon = PhotoImage(file='icon.png')
    root.iconphoto(True, icon)
    def reg():
        root.destroy()
        import signup
    #Variables
    Username = StringVar()
    Password = StringVar()

    #Login   
    def Login():
        if Username.get() == "" or Password.get() == "":
            messagebox.showerror("Invalid", "Please type Username and Password")

        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='1234')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error!!','Please Check your connection and try again')

                return

            query = 'use Lipongdata'
            mycursor.execute(query)
            query='select * from data where username=%s and password=%s'
            mycursor.execute(query,(Username.get(),Password.get()))
            row=mycursor.fetchone()

        if row==None:
                messagebox.showerror('Error!!','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome ' + Username.get() + '!!','Login Sucessfully')

            root.destroy()
            import Mainscreen
                    
                    
                

    # Login Images
    img=PhotoImage(file='image_2.png')
    user_img=ImageTk.PhotoImage(file='user.png')
    entry_frame1=ImageTk.PhotoImage(file='entry.png')
    code_img=ImageTk.PhotoImage(file='code.png')
    entry_frame2=ImageTk.PhotoImage(file='entry.png')
    login_btn=ImageTk.PhotoImage(file='login_btn.png')
    signup_btn=ImageTk.PhotoImage(file='signup_btn.png')

    # Login Frame
    def LoginForm():
            
            #def ToggleToRegister():
            #    Login_frame.destroy()
            #    RegisterForm()

        Login_frame=Frame(root, width=925, height=550, bg='white')
        Login_frame.pack(expand=True)

        mgalipong_label=Label(Login_frame, text='WELCOME TO MGA MGA LIPONG', fg='black', bg='white', font=('times new roman', 36, 'bold')).place(x=60, y=5)

        Label(Login_frame, image=img, width=450, height=450, bg='white').place(x=40, y=70)

        frame=Frame(Login_frame, width=390, height=400, bg='white')
        frame.place(x=500, y=105)

        heading=Label(frame, text='Login', fg='purple', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=160, y=5)

        # Entry
        Label(frame, image=user_img, bg='white').place(x=30, y=93)

        Label(frame, image=entry_frame1, border=0, bg='white').place(x=60, y=90)
        username=Entry(frame, textvariable=Username, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        username.place(x=80, y=97)

        Label(frame, image=code_img, bg='white').place(x=30, y=153)

        Label(frame, image=entry_frame2, border=0, bg='white').place(x=60, y=150)
        password=Entry(frame, textvariable=Password, width=30, show="•", fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        password.place(x=80, y=156)

        # ShowHide
        def show():
            hide_button=Button(frame, pady=0, image=hide_image, command=hide, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
            hide_button.place(x=330, y=157)
            password.config(show='')

        def hide():
            show_button=Button(frame, pady=0, image=show_image, command=show, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
            show_button.place(x=330, y=157)
            password.config(show='•')

        show_image=ImageTk.PhotoImage(file='show .png')
        hide_image=ImageTk.PhotoImage(file='hide.png')

        show_button=Button(frame, pady=0, image=show_image, command=show, cursor='hand2', relief=FLAT, activebackground='white', bg='white')
        show_button.place(x=330, y=157)

        Button(frame, text="Forget Password?",fg='red', bg='white', border=0,cursor='hand2',command=forget).place(x=260, y=190)

        Button(frame, image=login_btn, bg='white', border=0, cursor='hand2', command=Login).place(x=75, y=215)

        label=Label(frame, text="Don't have an account yet?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=125, y=280)

        register_btn=Button(frame, image=signup_btn, border=0, bg='white', cursor='hand2', command=reg).place(x=160, y=315)

    #--------Forget Pass-------#
    def forget():
        def c_password():
            if user_entry.get()=='' or pass_entry.get()=='' or cpass_entry.get()=='':
                        messagebox.showerror('Error!!','Please Input All Fields!!',parent=window)
            elif pass_entry.get()!=cpass_entry.get():
                        messagebox.showerror('Error!!','Password Not Matched!!!',parent=window)
            else:
                con = pymysql.connect(host='localhost',user='root',password='1234',database='Lipongdata')
                mycursor = con.cursor()
                query = 'select * from data where username=%s'
                mycursor.execute(query,(user_entry.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error!!', 'Incorrect Username',parent=window)
                else:
                    query='update data set password=%s where username=%s'
                    mycursor.execute(query,(pass_entry.get(),user_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', "Password change successfully",parent=window)
                    window.destroy()
        window = Toplevel()
        window.title("Forget Password")
        bgPic = ImageTk.PhotoImage(file='e.jpg')
        bglabel = Label(window,image=bgPic)
        bglabel.grid()
                    

        heading_label = Label(window, text='Forget Password', font=('times new roman',19,'bold'),bg='white', fg='blue')
        heading_label.place(x=160,y=60)

        userlabel = Label(window, text='Username:', font=('arial',12,'bold'),bg='white', fg='blue')
        userlabel.place(x=30,y=130)

        user_entry=Entry(window, width=25, fg='black',font=('arial',11,),bg='skyblue',bd=0)
        user_entry.place(x=30,y=160)


        passlabel = Label(window, text='Enter New Password:', font=('arial',12,'bold'),bg='white', fg='blue')
        passlabel.place(x=30,y=220)

        pass_entry=Entry(window, width=25, fg='black',font=('arial',11,),bd=0,bg='skyblue')
        pass_entry.place(x=30,y=250)

        cpasslabel = Label(window, text='Confirm New Password:', font=('arial',12,'bold'),bg='white', fg='blue')
        cpasslabel.place(x=30,y=310)

        cpass_entry=Entry(window, width=25, fg='black',font=('arial',11,),bg='skyblue',bd=0)
        cpass_entry.place(x=30,y=340)

        sButton=Button(window, text='Confirm', bd=2,bg='white',fg='black',font=("Open Snas",'16','bold'),width='19',cursor='hand2',activebackground='gray',activeforeground='white',command=c_password)
        sButton.place(x=20,y=390)
    
        
        window.mainloop()



    LoginForm()
    root.mainloop()

def bar():
            l4=Label(w,text="Loading...",fg='white',bg='#249794')
            lst4=('Calibri(Body)',10)
            l4.configure(font=lst4)
            l4.place(x=0,y=210)

            import time
            r=0
            for i in range(100):
                progress['value']=r
                w.update_idletasks()
                time.sleep(0.03)
                r=r+1
            w.destroy()
            main()
       

progress.place(x=-10,y=235)


#=======Add Frame====
Frame(w,width=427,height=241,bg='skyblue').place(x=0,y=0)
b1=Button(w,width=10,height=1,text='Please Enter',command=bar,cursor='hand2',border=0,fg='Blue')
b1.place(x=170,y=200)

#====label========#
l1=Label(w,text='WELCOME',fg='black',bg='skyblue')
lst1=('Calibri(Body)',18,'bold')
l1.configure(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='TO',fg='black',bg='skyblue')
lst2=('Calibri(Body)',18,'bold')
l2.configure(font=lst2)
l2.place(x=190,y=80)

l3=Label(w,text='MGA',fg='black',bg='skyblue')
lst3=('Calibri(Body)',18,'bold')
l3.configure(font=lst3)
l3.place(x=230,y=80)

l3=Label(w,text='LIPONG',fg='black',bg='skyblue')
lst3=('Calibri(Body)',18,'bold')
l3.configure(font=lst3)
l3.place(x=300,y=82)

l4=Label(w,text='PROGRAMMED',fg='black',bg='skyblue')
lst4=('Calibri(Body)',14,'bold')
l4.configure(font=lst4)
l4.place(x=50,y=110)

w.mainloop()