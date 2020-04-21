import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

MotorOne_enable = 22
MotorOne_1 = 16
MotorOne_2 = 22

GPIO.setup(MotorOne_enable, GPIO.OUT)
GPIO.setup(MotorOne_1, GPIO.OUT)
GPIO.setup(MotorOne_2, GPIO.OUT)

PWM = GPIO.PWM(MotorOne_enable, 100)
PWM.start(100)

GPIO.output(MotorOne_enable.HIGH)
GPIO.output(MotorOne_1.LOW)
GPIO.output(MotorOne_2.HIGH)

sleep(5)