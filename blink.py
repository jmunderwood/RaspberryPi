import RPi.GPIO as GPIO
import time

#setup Pi Mode
GPIO.setmode(GPIO.BCM)

#set pin 4 as output pin
GPIO.setup(4, GPIO.OUT)

blinktime = .5
while True:
	GPIO.output(4, GPIO.HIGH)
	time.sleep(blinktime)
	GPIO.output(4, GPIO.LOW)
	time.sleep(blinktime)
