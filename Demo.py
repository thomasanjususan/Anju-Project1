from tkinter import *
import cx_Oracle
import datetime import *
root = Tk()
con=cx_Oracle.connect("Saint/Saint@UST")
	cur=con.Cursor()
def call_create():
	
	cur.Execute(""" Create table reminder (msg varchar2(20),date date ,time time)""")
    num1 = (n1.get())
    num2 = (n2.get())
	num3=(n3.get())
	cur.Execute(' insert into reminder values(:1,:2,:3)',(num1,num2,num3))
    var = StringVar()
	a = Message( root, textvariable=var, relief=RAISED )
	var.set("table created  and inserted successfully")
	a.pack()
    return
	
def call_view():
	
	cur.Execute(""" select  * from reminder""")
	print(cur.fetchall())
    return
 
 def call_update():
	
	cur.Execute(" update reminder set msg=:1,date=:2,time=:3 where date=:2",(num1,num2,num3))
	print(cur.fetchall())
    return

root.geometry('500x500')
root.title('Calculator') 
 
n1 = StringVar()
n2 = StringVar()
 n3=StringVar()
labelTitle = Label(root, text="Enter the reminder")
labelTitle.place(x=125,y=50) 
labelNum1 = Label(root, text="Enter the date")
labelNum1.place(x=50,y=100)
labelNum2 = Label(root, text="Enter the  time") 
labelNum2.place(x=50,y=150)
entryNum1 = Entry(root, textvariable=n1)
entryNum1.place(x=200,y=100)
entryNum2 = Entry(root, textvariable=n2)
entryNum2.place(x=200,y=150)
entryNum2 = Entry(root, textvariable=n3)
entryNum2.place(x=200,y=150)
label_result= Label(root)
label_result.place(x=200,y=250)
buttonCal = Button(root, text="Create", command=call_create)
buttonCal.place(x=100,y=200)
buttonCal = Button(root, text="View", command=call_view)
buttonCal.place(x=200,y=300)
buttonCal = Button(root, text="Update", command=call_update)
buttonCal.place(x=300,y=400)
root.mainloop()
