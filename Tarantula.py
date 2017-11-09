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

# Distance detector
dis = 15
obstacle = 1

#Set turn value
SwingPr = 90
SwingTr = 0.55
SwingPl = 90
SwingTl = 0.37
PointPr = 90
PointTr = 0.41
PointPl = 90
PointTl = 0.19




try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        # IR sensor
        Le = getLeftmostled()
        Lc = getLeftlessled()
        M = getCenterled()
        Rc = getRightlessled()
        Re = getRightmostled()

        #print('distance= ', distance)
        #print Le, Lc, M, Rc, Re

        # when the distance is above the dis, moving object forwards
        if (M == 0) and (Lc == 1) and (Rc == 1):
            go_forward_any(27)
            #print('Obstacle counted ', obstacle)
            #print "FORWARD"
        # Follow black line
        elif (Le == 0) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 1):
            trackline(20, 37)
            print "LEFT"

        elif (Le == 1) and (Lc == 0) and (M == 0) and (Rc == 1) and (Re == 1):
            trackline(23, 35)
            print "Semi LEFT"

        elif (Le == 0) and (Lc == 0) and (M == 1) and (Rc == 1) and (Re == 1):
            trackline(26, 33)
            print "Track RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 0) and (Rc == 0) and (Re == 1):
            trackline(35, 25)
            print "Semi RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 0) and (Re == 0):
            trackline(33, 26)
            print "Track RIGHT"

        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc == 1) and (Re == 0):
            trackline(37, 20)
            print "RIGHT"
        elif (Le == 1) and (Lc == 1) and (M == 1) and (Rc ==1) and (Re == 1):
            stop()
            print "FAILED search line"
            sleep(1.2)
            leftSwingTurn(30, 0.3)


    print 'Shutdown'            
    pwm_low()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
