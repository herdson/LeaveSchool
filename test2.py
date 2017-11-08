######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import getDistance

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *

# =======================================================================
# import trackingModule
# =======================================================================
from trackingModule import *

# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()


# =======================================================================
# Define LineTracing Function
# =======================================================================
def goLineTracing(lspeed1, rspeed1, lspeed2, rspeed2):
    if getCenterled() == 0:
        go_forward_any(speed)

    elif getLeftlessled() == 0 or getLeftmostled() == 0:
        go_forward_fine(lspeed1, rspeed1)

    elif getRightlessled() == 0 or getRightmostled() == 0:
        go_forward_fine(lspeed2, rspeed2)

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
speed = 50

# turn fine right when car's direction is left
lspeed1 = 50
rspeed1 = 50

# turn fine left when car's direction is right
lspeed2 = 50
rspeed2 = 50

try:
    while True:

        goLineTracing(lspeed1, rspeed1, lspeed2, rspeed2)

# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
