import cv2
import motor_processes

limit_val=110
def set_limit_val(val):
    global limit_val
    limit_val = int(val)


def control(img):
        count=0
        for x in range(0, 120):  # (160,480) :
            for y in range(120, 240):  # (120,360):
                r, g, b = img[x, y]
                F = g - 0.5 * r - 0.5 * b
                if (F > limit_val or F < -10) and (r != 255 and g != 255 and b != 255):
                   img[x,y]=(0, 255, 255)
        cv2.imshow("test",img)


def insecticide(img):
    count = 0
    for x in range(2, 120):  # (160,480) :
        for y in range(int(width / 4), int(width / 2)):  # (120,360):
            r, g, b = img[x, y]
            F = g - 0.5 * r - 0.5 * b
            if (count == 0):
                if ((F < -10) or (F > 110)) and (
                        r > g):#if (F > limit_val or F < -10) and (r != 255 and g != 255 and b != 255):
                    count += 1
                    #print("started")
                    motor_processes.start_motor()
            else:
                #print("stopped")
                motor_processes.stop_motor()
                return count


def taken_view(selection):
    url =0 #"C:/Users/Fatih/Desktop/projevid/test_v.mp4"#('http://192.168.1.103:8080/video')

    cam = cv2.VideoCapture(url) #('C:/Users/Fatih/Desktop/vid/tarla.mp4')

    ret, img = cam.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    height, width, channels = img.shape

    x = int(width / 8)
    y = 1
    cv2.rectangle(img, (2 * x, y), (4 * x, y + 120), (0, 255, 0), 2)

    if(selection=="view"):
        control(img)
    else:
        print(insecticide(img))


def choosen_action(proccess):
    while True:
        try:
            taken_view(proccess)

        except:
            print("Error!!!")
            motor_processes.stop_motor()

        if cv2.waitKey(1) & 0xFF == ord('q'):
         print("Process Stopped!!!")
         if (proccess != "view"):
            motor_processes.stop_motor()
         break
