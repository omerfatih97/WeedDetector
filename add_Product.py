import cv2
import numpy as np
import os
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox,Button
import pyodbc


fig = plt.figure("Add New Product")
size = fig.get_figwidth(), fig.get_figheight()
fig.dpi = 120
fig.set_size_inches(600/fig.dpi, 300/fig.dpi)


agbox = plt.axes([0.35, 0.55, 0.4, 0.075])
ekranbox = plt.axes([0.77, 0.55, 0.2, 0.075])
abbox = plt.axes([0.35, 0.7, 0.4, 0.075])
x1=plt.axes([0.4, 0.3, 0.2, 0.10])
x2=plt.axes([0.2, 0.3, 0.4, 0.10])

picurl = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
picurl+='/untitled/venv/pics/plus1.png'
image1 =plt.imread(picurl)


button1=Button(x1,label="Add")
button2=Button(x2,label="",image=image1)
button3=Button(ekranbox,label="Value Finder")
text_box1 = TextBox(abbox, 'Product Name :')
text_box2 = TextBox(agbox, 'Limit Value ( 0-255 ) :')

def db_bag():
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-U81B5K2;"
                          "Database=product_vals;"
                          "Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM limit_vals')

    for row in cursor:
        son = "" + str(row)
        say = son.find(",")
        top_kayit=int(son[1:say])

    if( top_kayit == 10 ) :
        sonuc=messagebox.askquestion("Warning","Cannot add more than 10 value. Please delete one then try again..."
                                       "\n\n Click 'Yes' if you want to redirect to delete value page!!!")
        if(sonuc=="yes"):
            plt.close("Add New Product")
            import deleteValue as ks
            ks.plt.show(block = False)
        else:
            plt.close("Add New Product")
            import main_screen
    else:
        komut ="INSERT INTO limit_vals (name, val) Values ('"+ text_box1.text + "' , "+ text_box2.text + ");";
        cursor = conn.cursor()
        cursor.execute(komut)
        conn.commit()


def hata_mesaj(hata,deger):
    if(messagebox.showwarning("Info",hata)=="ok" and deger==1):
        plt.close("Add New Product")
        import main_screen


def add_val(label):
    if(text_box1.text != "" and text_box2.text != "" and float(text_box2.text) >= 0 ):
        db_bag()
        hata_mesaj("Process Done.",1)
    else:
        if(text_box1.text=="" or text_box2.text == "" ):
            hata_mesaj(" Please fill the blank areas...",0)
        elif( float(text_box2.text) < 0 ):
            hata_mesaj(" You cannot add minus value!",0)

def calis_2(label):
    while True:

        try:
            cam = cv2.VideoCapture(0)
            ret, img = cam.read()
            #height, width, channels = img.shape
            cv2.imshow("Test", img)
        except:
            print("Error!!")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def detector(label):
    url = 0 #('http://192.168.0.13:8080/video')
    cap = cv2.VideoCapture(url)

    while True:
        # Get webcam images
        ret, frame = cap.read()

        # Get height and width of webcam frame
        #height, width, channels  = frame.shape
        width=480
        height=360
        ortax=int(width / 2)
        ortay=int(height / 2)

        # Draw rectangular window for our region of interest
        cv2.rectangle(frame, (ortax-20, 240), (ortax-10, 240), (0, 255, 0), 2)
        cv2.rectangle(frame, (ortax+10, 240), (ortax+20, 240), (0, 255, 0), 2)

        cv2.rectangle(frame, (ortax, ortay-20), (ortax, ortay-10), (0, 255, 0), 2)
        cv2.rectangle(frame, (ortax, ortay + 20), (ortax, ortay + 10), (0, 255, 0), 2)

        cv2.circle(frame,(ortax,ortay),2,(0, 255, 0))

        r, g, b = frame[ortax,ortay]
        F = g - 0.5 * r - 0.5 * b
        deger="Value="+str(F)
        cv2.putText(frame, deger, (1, height-5), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

        cv2.imshow('Value Finder (For Close The Screen: Press Esc, Q veya Enter)', frame)
        bas = cv2.waitKey(1) % 256

        if bas==13 or bas==27 or bas == ord('q') or bas == ord('Q'):  # 13 is the Enter Key
            if(F>0):
                text_box2.set_val(str(F))
            break
    cap.release()
    cv2.destroyAllWindows()


button1.on_clicked(add_val)
button2.on_clicked(add_val)
button3.on_clicked(detector)

plt.show()