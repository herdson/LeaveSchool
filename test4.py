######################################################################
### Date: 2017/10/5
### file name: go_any.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to go forward or backward without time limit
######################################################################

# import GPIO library
import RPi.GPIO as GPIO
from time import sleep

from trackingModule import *

# set GPIO warnings as False
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# =======================================================================
# REVERSE function to control the direction of motor in reverse
# =======================================================================
def REVERSE(x):
    if x == True:
        return False
    elif x == False:
        return True


# =======================================================================
# Set the motor's true / false value to go forward.
# =======================================================================
forward0 = True
forward1 = False

# =======================================================================
# Set the motor's true / false value to go opposite.
# =======================================================================
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print
        'Config Error'


def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)


# student assignment (3)

# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  object to go forward without any limitation of running_time
# =======================================================================

def go_forward_fine(lspeed, rspeed):
    # set the left motor to go forward
    leftmotor(forward0)

    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightmotor(forward0)

    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(lspeed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(rspeed)


def go_forward_any(speed):
    # set the left motor to go forward
    leftmotor(forward0)

    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightmotor(forward0)

    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)


# student assignment (4)

# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  object to go backward without any limitation of running_time
# =======================================================================

def go_backward_any(speed):
    # set the left motor to go backward
    leftmotor(backward0)

    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go backward
    rightmotor(backward0)

    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go backward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)


# student assignment (5)

# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  object to go forward with the limitation of running_time
# =======================================================================

def go_forward(speed, running_time):
    # set the left motor to go forward
    leftmotor(forward0)

    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightmotor(forward0)

    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)


# student assignment (6)


# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  object to go backward with the limitation of running_time
# =======================================================================

def go_backward(speed, running_time):
    # set the left motor to go backward
    leftmotor(backward0)

    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go backward
    rightmotor(backward0)

    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go backward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)

    # set the running time of the left motor to go backward
    sleep(running_time)


# student assignment (7)


# =======================================================================
# define the stop module
# =======================================================================
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()


def goLineTracing(speed, lspeed1, rspeed1, lspeed2, rspeed2):
    if getCenterled() == 0:
        go_forward_any(speed)

    elif getLeftlessled() == 0 or getLeftmostled() == 0:
        go_forward_fine(lspeed1, rspeed1)

    elif getRightlessled() == 0 or getRightmostled() == 0:
        go_forward_fine(lspeed2, rspeed2)

speed = 30

    # turn fine right when car's direction is left
lspeed1 = 20
rspeed1 = 30

    # turn fine left when car's direction is right
lspeed2 = 30
rspeed2 = 20


# Test Module Function (Main)
if __name__ == "__main__":
    try:
        goLineTracing(speed,lspeed1, rspeed1, lspeed2, rspeed2)


    # when the Ctrl+C key has been pressed,
    # the moving object will be stopped
    except KeyboardInterrupt:
        pwm_low()

