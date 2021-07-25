import cv2
import numpy as np
from tkinter import messagebox
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.widgets import CheckButtons,Button
import pyodbc

titles=list()
fig = plt.figure("Delete Product")
plt.suptitle("Products",color="Blue")

size = fig.get_figwidth(), fig.get_figheight()
fig.dpi = 120
fig.set_size_inches(200/fig.dpi, 300/fig.dpi)

def show_func():
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-U81B5K2;"
                          "Database=product_vals;"
                          "Trusted_Connection=yes;")

    cursor = conn.cursor()
    cursor.execute('SELECT name FROM limit_vals')

    for row in cursor:
        son=""+str(row)
        say=son.find(" ")
        titles.append(son[2:say])


show_func()

def db_bag():
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-U81B5K2;"
                          "Database=product_vals;"
                          "Trusted_Connection=yes;")


    komut ="INSERT INTO limit_vals (name, val) Values ('"+ text_box1.text + "' , "+ text_box2.text + ");";
    cursor = conn.cursor()
    cursor.execute(komut)
    conn.commit()


rax = plt.axes([0.15, 0.7, 0.7, 0.20])
x1=plt.axes([0.15, 0.18, 0.7, 0.08])

x=IntVar()
visibility = [x for line in titles]
check=CheckButtons(rax, titles, visibility)
button1=Button(x1,label="Delete Seletected Value",color="Grey")

temp=IntVar()
for temp in range(len(titles)):
    check.set_active(temp)

def db_sil():
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-U81B5K2;"
                          "Database=product_vals;"
                          "Trusted_Connection=yes;")

    try:
        for i in range(len(check.get_status())):
            if check.get_status().__getitem__(i) == True:
                komut = "Delete from limit_vals where name= ('" + titles[i] + "');";
                cursor = conn.cursor()
                cursor.execute(komut)
                conn.commit()
        messagebox.showinfo("Info","Value Successfully Deleted...")

    except:
        messagebox.showinfo("Info", "Error Occured.")


def calis_1(label):
    db_sil()
    plt.close("Delete Product")
    import main_screen


button1.on_clicked(calis_1)

plt.show()