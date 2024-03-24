# Readme

## MGALIPONG's SIMPLE LOGIN SYSTEM
Simple Login and Register System, develop in Python platform using Tkinter and MySql. As a requirement for partial fulfilment in the subject Integrative Programming Technologies 2.

### Features:
 1. New User Registration
 2. User Login
 3. ogout
 4. Stores username and password
 5. Gives error messages
 
### Requirements:
* tkinter library
  
 

### Database
##### -  For mainscreen Database connection
```python

con=pymysql.connect(host='localhost',user='root',password='1234',database='1fdata')
        cur=con.cursor()
        cur.execute('insert into data values(%s,%s,%s,%s,%s,%s,%s)',(user_var.get(),name_var.get(),contact_var.get(),email_var.get(),gender_var.get(),dob_var.get(),
        address_var.get()))
        con.commit()
        fetch_data()
        clear()
        con.close()
```

##### -  For Registration Database connection
```python
 try:
        con=pymysql.connect(host='localhost',user='root',password='1234')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error!','Database Connectivity Issue, Please try Again')
        return
    try:
        query='create database Lipongdata'
        mycursor.execute(query)
        query='use Lipongdata'
        mycursor.execute(query)
        query='create table data(id int auto_increment primary key not null, username varchar(100),password varchar(30),Ulamnya varchar(200))'
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
```
##### - For Login Database connection
```python
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

```
### Visuals
####  Login Page:
 ![Reference Image](redmi/login.png)

####  Registration Page:
![Reference Image](redmi/reg.png)

#### Forget Password page:
![Reference Image](redmi/forget.png)

#### Main Screen:
![Reference Image](redmi/m.png)

### Language 
Python

# Summary
This is the simple system that we created using the python programming language