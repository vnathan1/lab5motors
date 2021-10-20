import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin = 20
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 100)
pwm.start(0)

for x in range(100,-1,-1) 
  pwm.ChangeDutyCycle(1)
  time.sleep(0.02)








