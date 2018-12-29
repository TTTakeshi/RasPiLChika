import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(2,GPIO.OUT)
for iLoop in range(3):
    GPIO.output(2,True)   
    time.sleep(2)
    GPIO.output(2,False)   
    time.sleep(2)
GPIO.cleanup()