from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def out():
    answer = messagebox.askquestion('Sign out?','Are you sure you want to Sign out?')
    if answer =='yes':
        root.quit()

root=Tk()
root.resizable(0,0)
root.title("Lipong Management System")
root.geometry("1300x700+0+0")
bg='orange'

icon = PhotoImage(file='fp.png')
root.iconphoto(True, icon)

#=========Variables========#
user_var=StringVar()
name_var=StringVar()
contact_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
dob_var=StringVar()
address_var=StringVar()

search_by=StringVar()
search_text=StringVar()


title=Label(root,text='Lipong Management System',bd=10,relief=GROOVE,font=('Harlow Solid Italic',25,'bold'),bg='yellow',fg='green')
title.pack(side=TOP,fil=X)
#--------Manage frame-----------#
m_frame=Frame(root,bd=4,relief=RIDGE,bg="skyblue")
m_frame.place(x=20,y=75,width=330,height=480)

M_title=Label(m_frame,text='Manage memebers',bd=5,relief=GROOVE,bg='skyblue',fg='white',font=('Lucida Calligraphy',13,'bold'))
M_title.place(x=50,y=0)

lbl_user=Label(m_frame,text='User No.',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_user.place(x=30,y=50)

t_user=Entry(m_frame,textvariable=user_var,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
t_user.place(x=110,y=46)

lbl_name=Label(m_frame,text='Name:',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_name.place(x=30,y=99)

t_name=Entry(m_frame,textvariable=name_var,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
t_name.place(x=110,y=96)

lbl_contact=Label(m_frame,text='Contact No.',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_contact.place(x=3,y=146)

t_contact=Entry(m_frame,textvariable=contact_var,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
t_contact.place(x=110,y=146)

lbl_mail=Label(m_frame,text='Email:',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_mail.place(x=30,y=198)

t_mail=Entry(m_frame,textvariable=email_var,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
t_mail.place(x=110,y=196)


lbl_gender=Label(m_frame,text='Gender:',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_gender.place(x=30,y=248)

combo_gender=ttk.Combobox(m_frame,textvariable=gender_var,font=('Yu Gothic UI Semibold',10,'bold'))
combo_gender['values']=('M','F','Other')
combo_gender.place(x=110,y=246)

lbl_db=Label(m_frame,text='D.O.B:',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_db.place(x=30,y=298)

t_db=Entry(m_frame,textvariable=dob_var,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
t_db.place(x=110,y=298)

lbl_Add=Label(m_frame,text='Address:',bg='skyblue',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbl_Add.place(x=15,y=360)

t_Add=Entry(m_frame,textvariable=address_var,font=('Yu Gothic UI Semibold',10,'bold'))
t_Add.place(x=110,y=348,width=200,height=40)

#==========Button=========#
btn_frame=Frame(m_frame,bd=4,relief=RIDGE,bg='skyblue')
btn_frame.place(x=0,y=430,width=323)

def add_member():
    if user_var.get()=='' or name_var.get()=="":
        messagebox.showerror("Error", 'Please input user no. and name!!!')
    else:
        con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
        cur=con.cursor()
        cur.execute('insert into data values(%s,%s,%s,%s,%s,%s,%s)',(user_var.get(),name_var.get(),contact_var.get(),email_var.get(),gender_var.get(),dob_var.get(),
        address_var.get()))
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Success","Record inserted")

def fetch_data():
    con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
    cur=con.cursor()
    cur.execute('select * from data')
    rows=cur.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('',END,values=row)
            con.commit()
        con.close()
    
def clear():
    user_var.set('')
    name_var.set('')
    contact_var.set('')
    email_var.set('')
    gender_var.set('')
    dob_var.set('')
    address_var.set('')

def get_cursor(ev):
    cursor_row=table.focus()
    contents=table.item(cursor_row)
    row=contents['values']
    user_var.set(row[0])
    name_var.set(row[1])
    contact_var.set(row[2])
    email_var.set(row[3])
    gender_var.set(row[4])
    dob_var.set(row[5])
    address_var.set(row[6])

def update():
    con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
    cur=con.cursor()
    query='update data set name=%s,contact=%s,email=%s,gender=%s,dob=%s,address=%s where user=%s'
    cur.execute(query,(name_var.get(),contact_var.get(),email_var.get(),gender_var.get(),dob_var.get(),address_var.get(),user_var.get())) 
    con.commit()
    fetch_data()
    clear()
    con.close

def delete():
    con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
    cur=con.cursor()
    cur.execute('delete from data where user=%s',user_var.get())
    con.commit()
    con.close()
    fetch_data()
    clear()

def search():
    con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
    cursor=con.cursor()
    
    cursor.execute("select * from data where "+str(search_by.get())+" LIKE '%"+str(search_text.get())+"%'")
    rows=cursor.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('',END,values=row)
            con.commit()
    con.close()





Addbtn=Button(btn_frame,text='Add',width=7,command=add_member).grid(row=0,column=0,padx=10)
Updatebtn=Button(btn_frame,text='Update',width=7,command=update).grid(row=0,column=1,padx=10)
Deletebtn=Button(btn_frame,text='Delete',width=7,command=delete).grid(row=0,column=2,padx=10)
Clearbtn=Button(btn_frame,text='Reset',width=7,command=clear).grid(row=0,column=3,padx=10)
Button(root, text="Sign Out",fg='red', bg='white', border=0,cursor='hand2',command=out).place(x=1200, y=550)



#--------Detail Frame-----------#
d_frame=Frame(root,bd=4,relief=RIDGE,bg="skyblue")
d_frame.place(x=380,y=75,width=900,height=480)

lblsearch=Label(d_frame,text='Search By',bg='skyblue',fg='black',font=('Lucida Calligraphy',12,'bold'))
lblsearch.grid(row=0,column=0,pady=10,padx=20,sticky='w')

combo_search=ttk.Combobox(d_frame,textvariable=search_by,width=8,font=('Yu Gothic UI Semibold',10,'bold'))
combo_search['values']=('User','Name','Gender')
combo_search.grid(row=0,column=1,pady=10,padx=20,sticky='w')

s=Entry(d_frame,textvariable=search_text,font=('Yu Gothic UI Semibold',10,'bold'),bd=5,relief=GROOVE)
s.grid(row=0,column=2,pady=10,padx=20,sticky="w")

sbtn=Button(d_frame,text='Search',width=7,command=search).grid(row=0,column=3,padx=10)
shbtn=Button(d_frame,text='Show All',width=7,command=fetch_data).grid(row=0,column=4,padx=10)

       
#===========Table======#
table_frame=Frame(d_frame,bd=4,relief=RIDGE,bg="skyblue")
table_frame.place(x=10,y=70,width=875,height=396)

scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)
table=ttk.Treeview(table_frame,columns=('user','name','contact no.','email','gender','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)
table.heading('user',text='User no.')
table.heading('name',text='Name')
table.heading('contact no.',text='Contact No.')
table.heading('email',text='Email')
table.heading('gender',text='Gender')
table.heading('dob',text='D.O.B')
table.heading('address',text='Address')
table['show']='headings'
table.column('user',width=90)
table.column('name',width=100)
table.column('contact no.',width=150)
table.column('email',width=200)
table.column('gender',width=80)
table.column('dob',width=100)
table.column('address',width=200)
table.pack(fill=BOTH,expand=1)
table.bind('<ButtonRelease-1>',get_cursor)

fetch_data()

#==========About us==========#
about_frame=Frame(root,bd=0,relief=RIDGE,bg="gray")
about_frame.place(x=0,y=570,width=1370,height=400)

lblabout=Label(about_frame,text='About Us',bg='gray',fg='black',font=('Lucida Calligraphy',20,'bold'))
lblabout.place(x=599,y=0)

lbla=Label(about_frame,text='Authors:',bg='gray',fg='black',font=('Lucida Calligraphy',10,'bold'))
lbla.place(x=630,y=40)

lblM=Label(about_frame,text='Marcos Relox Jr.',bg='gray',fg='black',font=('Lucida Calligraphy',15,'bold'))
lblM.place(x=140,y=70)

lblP=Label(about_frame,text='Peter Paul Rojas',bg='gray',fg='black',font=('Lucida Calligraphy',15,'bold'))
lblP.place(x=390,y=70)

lblC=Label(about_frame,text='Clarence Rabino',bg='gray',fg='black',font=('Lucida Calligraphy',15,'bold'))
lblC.place(x=640,y=70)

lblCr=Label(about_frame,text='Cris G. Pagayanan',bg='gray',fg='black',font=('Lucida Calligraphy',15,'bold'))
lblCr.place(x=880,y=70)

img=PhotoImage(file='hyy.png')
it=PhotoImage(file='hyy.png')

Label(about_frame, image=img, width=0, height=100, bg='gray').place(x=1100, y=12)
Label(about_frame, image=it, width=0, height=0, bg='gray').place(x=0, y=12)
lblp=Label(about_frame,text='?',bg='gray',fg='black',font=('Algerian',80,'bold'))
lblp.place(x=1240,y=2)




root.mainloop()