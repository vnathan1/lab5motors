# Basic code for servo control using manual PWM
# Set PWM period = 20 ms
# 1 ms ON = full CW = 5% duty cycle
# 2 ms ON = full CCW = 10% duty cycle

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 24
GPIO.setup(pwmPin, GPIO.OUT)

# set min & max % duty cycles (5 and 10 are default values, but play
# around to find optimum values for your motor)
dcMin = 2
dcMax = 12

pwm = GPIO.PWM(pwmPin, 40) # PWM object at 50 Hz (20 ms period)
pwm.start(0)

pwm.ChangeDutyCycle(dcMax)
time.sleep(0.5)
pwm.ChangeDutyCycle(dcMin)
time.sleep(0.5)
GPIO.cleanup()