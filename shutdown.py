import RPi.GPIO as GPIO
import os

#setup Pi Mode
GPIO.setmode(GPIO.BCM)

#set pin 26 as input pin
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(26, GPIO.FALLING)
	os.system("sudo shutdown -h now")
except:
	pass

GPIO.cleanup()
