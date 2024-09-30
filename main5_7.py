from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("stock managment system")
window.geometry("720x640")
my_tree = ttk.Treeview(window, show='headings',height=20)
style=ttk.Style()

placeholderArray = ['','','','','']
numeric='1234567890'
alpha='abcdefghijklmnopqrstuvwxyz'

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stockmanagmentsystem'
    )
    return conn

conn = connection()
cursor=conn.cursor()

for i in range(0,5):
    placeholderArray[i] = tkinter.StringVar()

def read()
    cursor.connection.ping()
    sql = f"SELECT 'item_id', 'item_id', 'name', 'price', 'quantity', 'category', 'date' FROM 'stocks' ORDER BY 'id' DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='',index='end',iid=array, text="",values=(array),tag="orow")
    my_tree.tag_configure('orow',background="#EEEEEE")
    my_tree.pack()

def setph(word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)

def generateRand():
    itemId=''
    for i in range(0,3):
        rando=random.randrange(0,(len(numeric)-1))
        itemId=itemId+str(numeric[rando])
    rando=random.randrange(0,(len(alpha)-1))
    itemId=itemId+'-'+str(alpha[rando])
    print("generated: "+itemId)
    setph(itemId,0)

def save():
    itemId=str(itemIdEntry.get())
    name=str(nameEntry.get())
    price=str(priceEntry.get())
    qnt=str(qntEntry.get())
    cat=str(categoryCombo.get())
    valid=True
    if not(itemId and itemId.strip()) or not(name and name.strip()) or not(price and price.strip()) or not(qnt or qnt.strip()) or not(cat and cat.strip()):
        messagebox.showwarning("", "pls fill up all fields")
        return
    if len(itemId) < 5
        messagebox.showwarning("","invalid item id")
        return
    if(not(itemId[3]=='-')):
        valid=False
    for i in range(0,3):
        if(not(itemId[i] in numeric)):
            valid=False
            break
    if(not(itemId[4] in alpha)):
        valid=False
    if not(valid):
        messagebox.showwarning("","invalid item id")
        return
    try:
        cursor.connection.ping()
        sql=f"SELECT * FROM stocks WHERE 'item_id' = '{itemId}'"
        cursor.execute(sql)
        checkItemNo=cursor.fetchall()
        if len(checkItemNo) > 0:
            messagebox.showwarning("","item is already used")
            return
        else:
            cursor.connection.ping()
            sql=f"INSERT INTO stocks ('id','item id','name','price','quantity','category','date') VALUES('{itemId}','{name}','{price}','{qnt}','{cat}')"
            cursor.execute(sql)
        conn.commit()
        conn.close()
        for num in range(0,5):
            setph('',(num))
    except:
        messagebox.showwarning("","error while saving")
        return
    refreshTable()

def update():
    selectedItemId = ''
    try:
        selectedItem = my_tree.selection()[0]
        selectedItemId = str(my_tree.item(selectedItem)['values'][0])
    except:
        messagebox.showwarning("","please seecet a data row")
    print(selectedItemId)
    itemId= str(itemIdEntry.get())
    name=str(nameEntry.get())
    price=str(priceEntry.get())
    qnt= str(qntEntry.get())
    cat= str(categoryCombo.get)
    if not (itemId and itemId.strip()) or not (name and name.strip()) or not (price and price.strip()) or not (qnt or qnt.strip()) or not (cat and cat.strip()):
        messagebox.showwarning("", "pls fill up all fields")
        return
    if(selectedItemId != itemId):
        messagebox.showwarning("","you cant change item id")
        return
    try:
        cursor.connection.ping()
        sql=f"UPDATER stocks SET `name` = {name}, `price` = {price}, `quantity` = {qnt}, `category` = {cat} WHERE `item_id` = '{itemId}' "
        cursor.execute(sql)
        conn.commit()
        conn.close()
        for num in range(0,5):
            setph('',(num))
    except Exeption as err:
        messagebox.showwarning("","error occured ref: " +str(err))
        return
    refreshTable()

def delete():
    try:
        if(my_tree.selection()[0]):
            decision = messagebox.askquestion("","delete the selected data")
            if(decision != 'yes'):
                return
            else:
                selectedItem = my_tree.selection()[0]
                itemId = str(my_tree.item(selectedItem)['values'][0])
                try:
                    cursor.connection.ping()
                    sql = f"DELETE FROM stocks WHERE `item_id` = '{itemId}' "
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("","data has been successfully delted")
                except:
                    messagebox.showinfo("","sorry an error occured")
                refreshTable()
    except:
        messagebox.showwarning("","pls select a data row")

def select():
    try:
        selectedItem = my_tree.selection()[0]
        itemId = str(my_tree.item(selectedItem)['values'][0])
        name = str(my_tree.item(selectedItem)['values'][1])
        price = str(my_tree.item(selectedItem)['values'][2])
        qnt = str(my_tree.item(selectedItem)['values'][3])
        cat = str(my_tree.item(selectedItem)['values'][4])
        setph(itemId,0)
        setph(name,1)
        setph(price,2)
        setph(qnt,3)
        setph(cat,4))
    except:
        messagebox.showwarning("","please selcet a data row")

def find():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    qnt = str(qntEntry.get())
    cat = str(categoryCombo.get)
    cursor.connection.ping()
    if(itemId and itemId.strip()):
        sql=f"SELECT 'item_id', `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `item_id` LIKE '%{itemId}%' "
    elif (name and itemId.strip()):
        sql = f"SELECT 'item_id', `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `name` LIKE '%{name}%' "
    elif (price and itemId.strip()):
        sql = f"SELECT 'item_id', `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `price` LIKE '%{price}%' "
    elif (qnt and itemId.strip()):
        sql = f"SELECT 'item_id', `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `qnt` LIKE '%{qnt}%' "
    elif (cat and itemId.strip()):
        sql = f"SELECT 'item_id', `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `cat` LIKE '%{cat}%' "
    else:
        messagebox.showwarning("","pls fill up one of the fields")
        return
    cursor.execute(sql)
    try:
        result= cursor.fetchall();
        for num in range(0,5):
            setph(result[0][num],(num))
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("","no data found")

def clear():
    for num in range(0,5):
        setph('',(num))

def exportExcel():
    cursor.connection.ping()
    sql = f"SELECT 'item_id', 'item_id', 'name', 'price', 'quantity', 'category', 'date' FROM 'stocks' ORDER BY 'id' DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    date = str(datetime.now())
    date = date.replace('','_')
    date = date.replace(':','-')
    dateFinal = date[0:16]
    with open("stocks_"+dateFinal+".csv",'a',newline='') as f:
        w - csv.writer(f,dialect='excel')
        for record in datarow:
            w.writerow(record)
    print("saved: stocks_"+dateFinal+".csv")
    conn.commit()
    conn.close()
    messagebox.showinfo("","excel file download")



frame =tkinter.Frame(window, bg = "#02577A")
frame.pack()

btnColor = "#196E78"

manageFrame = tkinter.LabelFrame(frame,text="Manage",borderwidth=5)
manageFrame.grid(row=0, column=0,sticky="w",padx=[10,200],pady=20, ipadx=[6])

saveBtn = Button(manageFrame,text="save",width=10, borderwidth=3,bg=btnColor,fg='white', command= save)
updateBtn = Button(manageFrame,text="update",width=10, borderwidth=3,bg=btnColor,fg='white', command= update)
deleteBtn = Button(manageFrame,text="delete",width=10, borderwidth=3,bg=btnColor,fg='white', command= delete)
selectBtn = Button(manageFrame,text="select",width=10, borderwidth=3,bg=btnColor,fg='white', command= select)
findBtn = Button(manageFrame,text="find",width=10, borderwidth=3,bg=btnColor,fg='white', command=find)
clearBtn = Button(manageFrame,text="clear",width=10, borderwidth=3,bg=btnColor,fg='white', command= clear)
exportBtn = Button(manageFrame,text="export excel",width=15, borderwidth=3,bg=btnColor,fg='white',command= exportExcel)

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
selectBtn.grid(row=0,column=3,padx=5,pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=5,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)

entriesFrame = tkinter.LabelFrame(frame,text="form",borderwidth=5)
entriesFrame.grid(row=0, column=0,sticky="w",padx=[10,200],pady=[0,20], ipadx=[6])

itemIdlabel= Label(entriesFrame,text= "ITEM ID", anchor="e", width=10)
namelabel= Label(entriesFrame,text= "name", anchor="e", width=10)
pricelabel= Label(entriesFrame,text= "price", anchor="e", width=10)
qntlabel= Label(entriesFrame,text= "qnt", anchor="e", width=10)
categorylabel= Label(entriesFrame,text= "category", anchor="e", width=10)

itemIdlabel.grid(row=0,column=0,padx=10)
namelabel.grid(row=1,column=0,padx=10)
pricelabel.grid(row=2,column=0,padx=10)
qntlabel.grid(row=3,column=0,padx=10)
categorylabel.grid(row=4,column=0,padx=10)

categoryArray = ['networking tools','computer spare parts', 'repair tools','useful gadgets']

itemIdEntry= Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
nameEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[1])
priceEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[2])
qntEntry= Entry(entriesFrame,width=50, textvariable=placeholderArray[3])
categoryCombo= ttk.Combobox(entriesFrame,width=47, textvariable=placeholderArray[4],values=categoryArray)

itemIdEntry.grid(row=0,column=0,padx=5, pady= 5)
nameEntry.grid(row=1,column=0,padx=5, pady = 5)
priceEntry.grid(row=2,column=0,padx=5, pady = 5)
qntEntry.grid(row=3,column=0,padx=5, pady= 5)
categoryCombo.grid(row=4,column=0,padx=5, pady =5)

generateIdBtn= Button(entriesFrame,text="genereate id",borderwidth=3,bg=btnColor,fg='white',command=generateRand)
generateIdBtn.grid(row=0,column=3,padx=5, pady =5)

style.configure(window)
my_tree['columns']=("Item Id","Name","Price","Quantity","Category","Date")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Item Id", anchor=W,width=70)
my_tree.column("Name", anchor=W,width=100)
my_tree.column("Price", anchor=W,width=100)
my_tree.column("Quantity", anchor=W,width=100)
my_tree.column("Category", anchor=W,width=100)
my_tree.column("Date", anchor=W,width=100)
my_tree.heading("Item Id",text="Irem Id",anchor=W)
my_tree.heading("Name",text="name",anchor=W)
my_tree.heading("Price",text="price",anchor=W)
my_tree.heading("Quantity",text="quantity",anchor=W)
my_tree.heading("Category",text="category",anchor=W)
my_tree.heading("Date",text="date",anchor=W)
my_tree.tag_configure('orow',background="#EEEEEE")
my_tree.pack()

refreshTable()

window.resizable(False, False)
window.mainloop()
