import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin = 20
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 100)
pwm.start(100)
time.sleep(0.5)


for x in range(100,0,-1):
  pwm.ChangeDutyCycle(x)
  time.sleep(0.02)








