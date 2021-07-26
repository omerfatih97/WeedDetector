from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import *
from PIL import Image, ImageTk
import pyodbc
import os

titles=list()
limit_valuesList=list()
fig = plt.figure("Main Screen")

def doldur():
    x = IntVar()
    visibility = [x for line in titles]
    check = CheckButtons(rax, titles, visibility)
    temp = IntVar()
    for temp in range(len(titles)):
        check.set_active(temp)

def goster():
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

    cursor.execute('SELECT val FROM limit_vals')

    for row in cursor:
        son = "" + str(row)
        say = son.find(",")
        limit_valuesList.append(son[1:say])

goster()

desktopUrl = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
img1 =  Image.open(desktopUrl+'/untitled/venv/pics/daricanotu.jpg')
img2 =  Image.open(desktopUrl+'/untitled/venv/pics/devedikeni.jpg')
img3 =  Image.open(desktopUrl+'/untitled/venv/pics/sirken.jpg')
img4 =  Image.open(desktopUrl+'/untitled/venv/pics/yabanimarul.jpg')

plt.subplot(231),plt.imshow(img1),plt.title('Daricanotu',color="Red")
plt.subplot(232),plt.imshow(img2),plt.title('Devedikeni',color="Red")
plt.subplot(233),plt.imshow(img3),plt.title('Sirken',color="Red")
plt.subplot(234),plt.imshow(img4),plt.title('Yabanimarul',color="Red")

picurl=desktopUrl+'/untitled/venv/pics/plus1.png'
image1 =plt.imread(picurl)
plt.suptitle("Main Screen",color="Blue")

rax = plt.axes([0.015, 0.4, 0.1, 0.15])
x1=plt.axes([0.5, 0.21, 0.3, 0.10])
x2=plt.axes([0.5, 0.1, 0.3, 0.10])
x3=plt.axes([0.015, 0.29, 0.1, 0.10])
x4=plt.axes([0.110, 0.57, 0.0, 0.00])
x5=plt.axes([0.015, 0.18, 0.1, 0.05])

x=IntVar()
visibility = [x for line in titles]
check=CheckButtons(rax, titles, visibility)
button1=Button(x1,label="View Detections")
button2=Button(x2,label="Spray Detected Plants")
button3=Button(x3,label="",image=image1)
text_box1 = TextBox(x4, 'Products')
"""button4=Button(x4,label="Ürünler",color="White")
button4.set_active(active=False)"""
button5=Button(x5,label="Delete Product",color="Grey")

temp=IntVar()
for temp in range(len(titles)):
    check.set_active(temp)

selected_value=100
is_choosen=False


def chck_selection():
    for j in range(len(check.get_status())):
        if check.get_status().__getitem__(j)==True:
            global is_choosen
            is_choosen = True
            global selected_value
            if (j>1):
                if int(limit_valuesList[j]) > selected_value:
                    selected_value = int(limit_valuesList[j])
            else:
                selected_value = int(limit_valuesList[j])



def chck_func(label):
    global is_choosen
    is_choosen = False
    index = titles.index(label)
    chck_selection()

def view_Detection(label):
    if is_choosen==True:
        import detectionView as vd
        messagebox.showwarning("Info",""+vd.control())
    else:
        messagebox.showwarning("Error", " Please Choose Product!!! ")


def spray_wildPlant(label):
    if is_choosen==True:
        import weedSpray as deneme
        deneme.set_limit_val(selected_value)
        deneme.choosen_action("insecticide")
    else:
        messagebox.showerror("Error", " Please Choose Product!!! ")

def add_newProductVal(label):
    plt.close("Main Screen")
    import add_Product

def del_Product(label):
    plt.close("Main Screen")
    import deleteValue


check.on_clicked(chck_func)
button1.on_clicked(view_Detection)
button2.on_clicked(spray_wildPlant)
button3.on_clicked(add_newProductVal)
button5.on_clicked(del_Product)

while True:
    plt.show()
    if 0xFF == 13 or 0xFF == 27 or 0xFF == ord('q') or 0xFF == ord('Q'):  # 13 is the Enter Key
        break
