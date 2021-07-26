"""import serial,time

def calis():
    ser = serial.Serial('COM4', 9600, timeout=1) #here you may add write_timeout=1 to avoid indefinite blocking on failing flush
"""
import urllib.request,time,http.client,cv2

def calistir():
    #print("started")
    urllib.request.urlopen("http://192.168.0.23/forward") # send request to ESP
    time.sleep(1)
    dur()
   



def dur():
    urllib.request.urlopen("http://192.168.0.23/stop")

