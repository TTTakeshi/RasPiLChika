import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # BCM:GPIO論理番号指定
GPIO.setup(2,GPIO.OUT)
for iLoop in range(3):
    GPIO.output(2,True)     # GPIO2←ON
    time.sleep(2)
    GPIO.output(2,False)    # GPIO2←OFF
    time.sleep(2)
GPIO.cleanup()