import time as t
import sys
import Adafruit_DHT
import RPi.GPIO as rp
rp.setwarnings(False)
rp.setmode(rp.BOARD)
out_pins=[7,19,23,33,35,37]
IN_pins=[21,29,31]
for i in pins:
    rp.setup(i,rp.OUT)
for i in pins:
    rp.setup(i,rp.IN)

def ultrasonic():
    rp.output(19,1)
    t.sleep(0.0001)
    rp.output(19,0)
    while(rp.input(21)==0):
        pass
    st1=t.time()
    while(rp.input(21)==0):
        pass
    stop1=t.time()
    t1=st1-stop1

    rp.output(23,1)
    t.sleep(0.0001)
    rp.output(23,0)
    while(rp.input(29)==0):
        pass
    st2=t.time()
    while(rp.input(29)==0):
        pass
    stop2=t.time()
    t2=st2-stop2

    if(t1-t2>0):
        temp()
        ldr()
        
    elif(t1-t2<0):
        rp.output(33,0)
        rp.output(35,0)
        

def temp():

    while (True):
        humidity,temperature=Adafruit_DHT.read_retry(11,4)
        print('TEMPERATURE: {0:0.1f}C '.format(temperature))
    if(temperature>25):
        rp.output(35,1)

ultrasonic()


def ldr():
    if(rp.input(31)==1):
        rp.output(33,1)
        
