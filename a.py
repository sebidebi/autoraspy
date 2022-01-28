import RPi.GPIO as GPIO
import time
fPWM = 50  # Hz (not higher with software PWM)


GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
global pwm1, pwm2
pwm1 = GPIO.PWM(16, fPWM)
pwm1.start(0)
pwm2 = GPIO.PWM(19, fPWM)
pwm2.start(0)

currentstate = 0

def right(value):
    print("Right")
    pwm2.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(value)

right(30)