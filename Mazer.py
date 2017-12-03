######################################################################
### Date Unknown
### Purpose: Destroy the maze
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
# import TurnModule() method
# =======================================================================
from spider import *

# =======================================================================
# import trackingModule() method
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

obr = False
obl = False


try:
    while True:
        # IR sensor
        Le = getLeftmostled()
        Lc = getLeftlessled()
        M = getCenterled()
        Rc = getRightlessled()
        Re = getRightmostled()
        LeD = (Le, Lc, M, Rc, Re)

        #print Le, Lc, M, Rc, Re

        # when the distance is above the dis, moving object forwards
        if obr == True and (LeD == (1,0,0,0,0) or LeD == (1,1,0,0,0)):
            go_forward(40,0.5)
            LeD = (Le, Lc, M, Rc, Re)
        elif obr == True and (LeD == (1,1,0,1,1) or LeD == (1,0,0,1,1) or LeD == (1,1,0,0,1)):
            obr = False
            rightSwingTurn(80,0.3)
            LeD = (Le, Lc, M, Rc, Re)
            while LeD != (1,1,0,1,1) or LeD != (1,0,0,1,1) or LeD != (1,1,0,0,1) :
                rightPointTurn(80, 0.1)
                LeD = (Le, Lc, M, Rc, Re)

        if obl == True and (LeD == (0,0,0,0,1) or LeD == (0,0,0,1,1)):
            go_forward(40,0.5)
            LeD = (Le, Lc, M, Rc, Re)
        elif obl == True and (LeD == (1,1,0,1,1) or LeD == (1,0,0,1,1) or LeD == (1,1,0,0,1)):
            obl = False
            leftSwingTurn(80,0.3)
            LeD = (Le, Lc, M, Rc, Re)
            while LeD != (1,1,0,1,1) or LeD != (1,0,0,1,1) or LeD != (1,1,0,0,1) :
                leftPointTurn(80, 0.1)
                LeD = (Le, Lc, M, Rc, Re)



        if LeD == (1,1,0,1,1):
            go_forward_any(33)
            #print "FORWARD"
        # Focus to black line

        if LeD == (1,0,0,1,1):
            mazetracker(60, 20)
        elif LeD == (1,1,0,0,1):
            mazetracker(20, 60)

        if (LeD == (1,0,0,0,0)) or (LeD == (1,1,0,0,0)):
            obr = True
            rightSwingTurn(80,0.3)
        elif (LeD == (0,0,0,0,1)) or (LeD == (0,0,0,1,1)):
            obl = True
            leftSwingTurn(80, 0.3)
        


    print 'Shutdown'            
    pwm_low()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
