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
from spider import *

# =======================================================================
# import TurnModule() method
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
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================

# used avoid_obstacle
obstacle_left_speed = 45
obstacle_right_speed = 2

# used isobstacle 
isobstacle_left_speed = 15
isobstacle_right_speed = 5

# Distance detector
dis = 8
isPosition = 0


def avoidobstacle():
    rightPointTurn(80, 0.3)
    stop()
    print "enter 1"
    go_forward(80, 0.4)
    leftPointTurn(80, 0.3)
    stop()
    print "enter 2"
    go_forward(80, 0.4)
    leftPointTurn(80, 0.3)
    stop()
    print "enter 3"
    stop()
    sleep(5)

def obstacle_linetracing(distance_value):
    try:
        trackline_time(obstacle_left_speed, obstacle_right_speed, 1) #First Right Turn
        print("Enter 2")
        while (getDistance() < dis): # is obstacle 
           trackline_time(isobstacle_left_speed, isobstacle_right_speed, 1)
           print("Enter 1")
    
        trackline_time(obstacle_right_speed, obstacle_left_speed, 0.3) #First Left Turn
        print("Enter 3") # not obstacle
	stop()
	print("Enter 4")

        go_forward(40, 1.2) # constance
    except Exception:
        print("Detected Error")
    else:
        print("No Problem")
    finally:
        trackline_time(obstacle_right_speed, obstacle_left_speed, 0.8) # Second Left Turn
	print("Enter 5")
	trackline_time(obstacle_left_speed, obstacle_right_speed, 0.5) # Second Right Turn
	print("Enter 6")
    print("obstacle avoid Success")

try:
    while True:
        #ultra sensor replies the distance back
        distance = getDistance()
       
	# IR sensor
        Le = getLeftmostled()
        Lc = getLeftlessled()
        M = getCenterled()
        Rc = getRightlessled()
        Re = getRightmostled()
       
	# obstacle found
        if distance < dis:
            stop()
            avoidobstacle()

        # when the distance is above the dis, moving object forwards
        if (M == 0) and (Lc == 1) and (Rc == 1):
            go_forward_any(30)
            print "FORWARD"
            #print('Obstacle counted ', obstacle)
        # Follow black line
        elif (Le == 0) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 1):
            trackline(8, 65)
            print "LEFT"

        elif (Le == 1) and (Lc == 0) and (M == 0) and (Rc == 1) and (Re == 1):
            trackline(25, 32)
            print "Semi LEFT"

        elif (Le == 0) and (Lc == 0) and (M == 1) and (Rc == 1) and (Re == 1):
            trackline(21, 29)
            print "Track RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 0) and (Rc == 0) and (Re == 1):
            trackline(32, 25)
            print "Semi RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 0) and (Re == 0):
            trackline(29, 21)
            print "Track RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 0):
            trackline(60, 7)
            print "RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 1):
            stop()
            print "FAILED RIGHT search line"
            sleep(0.7)
            leftSwingTurn(30, 0.3)
	    #if (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 1):
	    #	print "FAILED LEFT search line"
		#sleep(1.2)
		#rightSwingTurn(30, 0.6)
        elif (Le == 0) and (Lc == 0) and (M == 0) and (Rc == 0) and (Re == 0):
            stop()
            pwm_low()     

	print("Le = ", Le, "Lc = ", Lc, "M = ", M, "Rc = ", Rc, "Re = ", Re)

    print 'Shutdown'            
    pwm_low()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
