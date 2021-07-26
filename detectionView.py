import cv2
import motor_processes,urllib.request,time
import os
import numpy as np
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
desktop+='/projevid/test_v.mp4'

esik_degeri=180



def control():
    url=0
    cap =cv2.VideoCapture(url) # cv2.VideoCapture(desktop)#('http://192.168.0.11:8080/video')#(desktop)
    while (True):
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()
            frame2 = frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            height, width, channel = frame.shape
            x = int(width / 8)
            y = 1
            cv2.rectangle(frame2, (2 * x, y), (4 * x, y + 120), (0, 255, 0), 2)

            for x in range(2, 120):  # (160,480) :
                for y in range(int(width / 4), int(width / 2)):  # (120,360):
                    r, g, b = frame2[x, y]
                    F = g - 0.5 * r - 0.5 * b
                    if ((F < -10) or (F > 110)) and (
                            r > g):  # (r==0 and g==0 and b==255): #(F > esik_degeri or F < -10) and (r != 255 and g != 255 and b != 255)and (r != 0 and g != 0 and b != 0):
                        frame2[x, y] = [255, 0, 0]

            # Display the resulting frame
            cv2.imshow('Test View Of Detected Weed', frame2)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        except:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return "Process Successfully Done."


"""
        cam = cv2.VideoCapture('C:/Users/Fatih/Desktop/vid/tarla.mp4')
        ret, img = cam.read()
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        height, width, channels = img.shape
        cv2.imshow("test",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break"""



"""

def goruntu_al():
    url = ('http://192.168.0.13:8080/video')

    cam = cv2.VideoCapture(url)
    ret, img = cam.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    height, width, channels = img.shape

    x = 120
    y = 1

    cv2.rectangle(img, (x, y), (x + x, y + 120), (0, 255, 0), 2)
    print(control(img))


while True:

    try:
        #detector()
        goruntu_al()
    except:
        motor_calisma.dur()

    if cv2.waitKey(1) & 0xFF == ord('q'):
     motor_calisma.dur()
     break



import time, sys
import ps_drone
import cv2

drone = ps_drone.Drone()
drone.startup()

drone.reset()
while (drone.getBattery()[0] == -1):
    time.sleep(0.1)

print
"Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1])
drone.useDemoMode(True)

##Setup##
drone.setConfigAllID()
drone.sdVideo()
drone.frontCam()
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:    time.sleep(0.0001)
drone.startVideo()

##Detection##
IMC = drone.VideoImageCount
stop = False

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (800, 800))

while not stop:

    while drone.VideoImageCount == IMC:
        time.sleep(0.01)

    IMC = drone.VideoImageCount
    key = drone.getKey()

    if key:
        stop = True

    img = drone.VideoImage
    resize = cv2.resize(img, (800, 800))
    # out.write(resize)
    cv2.imshow('Drones video', resize)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)

cv2.destroyAllWindows()"""
