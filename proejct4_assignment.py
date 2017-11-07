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

# used avoid_obstacle
obstacle_left_speed = 30
obstacle_right_speed = 20

# used isobstacle 
isobstacle_left_speed = 15
isobstacle_right_speed = 5

# used linefound
linefound_left_speed = 15
linefound_right_speed = 8

# project4_assignment
def obstacle_linetracing(distance_value):
    detailTurn(obstacle_left_speed, obstacle_right_speed, 2) #First Right Turn
    while (distance_value < dis): # is obstacle 
        detailTurn(isobstacle_left_speed, isobstacle_right_speed, 2)
    # not obstacle 
    try:	
	go_forward(20, 2) # constance
    finally:
	detailTurn(obstacle_right_speed, obstacle_left_speed, 2) #Last Left Turn
	while not(GPIO_input(leftmostled)) and not(GPIO_input(leftlessled)): # line not found
	    go_forward(10, 2) # constance
	while not(GPIO_input(centerled)) and not (GPIO_input(rightlessled)): # Line Sorting
 	    detailTurn(linefound_left_speed, linefound_right_speed, 2) 


# Distance detector
dis = 15
obstacle = 1


try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
				
	go_forward_any(35)

	if (distance < dis):
            detailTurn(	
	if GPIO.input(leftmostled): # 1
	
	if GPIO.input(leftlessled): # 2

	if GPIO.input(centerled): # 3

	if GPIO.input(rightlessled): # 4

	if GPUO.input(rightmostled): # 5


    print 'Shutdown'            
    pwm_low()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
