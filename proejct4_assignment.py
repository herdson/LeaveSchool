######################################################################
### Date Unknown
### Purpose: Detect black line and tracking it.
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
# import TrackingModule() method
# =======================================================================
from trackingModule import *

# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
speed = 50

# turn fine right when car's direction is left
lspeed1 = 8
rspeed1 = 15

# turn fine left when car's direction is right
lspeed2 = 15
rspeed2 = 8

# used avoid_obstacle
obstacle_left_speed = 10
obstacle_right_speed = 50

# used isobstacle 
isobstacle_left_speed = 15
isobstacle_right_speed = 5

# used linefound
linefound_left_speed = 15
linefound_right_speed = 8

# Distance detector
dis = 15
isPosition = 0

# =======================================================================
# Define LineTracing Function
# =======================================================================
def obstacle_linetracing(distance_value):
    detailTurn(obstacle_left_speed, obstacle_right_speed, 1) #First Right Turn
    print("Enter 2")
    while (getDistance() < dis): # is obstacle 
        detailTurn(isobstacle_left_speed, isobstacle_right_speed, 1)
        print("Enter 1")
    detailTurn(obstacle_right_speed, obstacle_left_speed, 0.85) #First Left Turn
    print("Enter 3") # not obstacle 
    try:
        go_forward(30, 2) # constance
    except Exception:
        print("Detected Error")
    else:
        print("No Problem")
    finally:
        detailTurn(obstacle_right_speed, obstacle_left_speed, 1) # Second Left Turn
        detailTurn(obstacle_left_speed, obstacle_right_speed, 0.85) # Second Right Turn
        while getLeftmostled() or getLeftlessled(): # line found
            go_forward(10, 2) # constance
        while getCenterled() or getRightlessled(): # Line Sorting
            detailTurn(linefound_left_speed, linefound_right_speed, 2)
    print("obstacle avoid Success")

def goLineTracing(lspeed1, rspeed1, lspeed2, rspeed2):
    if not(getLeftlessled()) or not(getLeftmostled()):
        go_forward_fine(lspeed1, rspeed1)
    elif not(getRightlessled()) or not(getRightmostled()):
        go_forward_fine(lspeed2, rspeed2)
    else:
        go_forward_any(speed)

def AllWhitespace():
    try:
        detailTurn(linefound_right_speed, linefound_left_speed, 2) #Left line searching
        if getLeftmostled():
            global isPosition
            # ------------------------------------------------------- #
            detailTurn(linefound_left_speed, linefound_right_speed, 2) #Right line searching
            isPosition = True
    except Exception:
        print("Detected Error")
    else:
        print("No Problem")
    finally:
        while getLeftlessled() or getRightlessled(): #line found
            go_forward(10, 2)
        while getLeftlessled() or getCenterled() or getRightlessled(): # Line Sorting
            if not(isPosition):
                detailTurn(linefound_left_speed, linefound_right_speed, 2)  # rightLine Sorting
            else:
                detailTurn(linefound_right_speed, linefound_left_speed, 2)  # leftLine Sorting
        print("Line Finding Success")

try:
    while True:
        # Checking line
        # print("leftmostled  detects black line(0) or white ground(1): " + str(getLeftmostled()))
        # print("leftlessled  detects black line(0) or white ground(1): " + str(getLeftlessled()))
        # print("centerled    detects black line(0) or white ground(1): " + str(getCenterled()))
        # print("rightlessled detects black line(0) or white ground(1): " + str(getRightlessled()))
        # print("rightmostled detects black line(0) or white ground(1): " + str(getRightmostled()))

        # ultra sensor replies the distance back
        distance = getDistance()
        #goLineTracing(lspeed1,rspeed1, lspeed2, rspeed2)

        print(distance)
        
        if distance < dis: #obstacle found
            stop()
            obstacle_linetracing(distance)

        #if getLeftmostled() and getCenterled() and getRightmostled(): #reading sensor - All White
        #    stop()
        #    AllWhitespace()

    print ("Shutdown")
    pwm_low()

# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
