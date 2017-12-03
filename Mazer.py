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

trModule = trackingModule()
trModule.setup()

try:
    while True:
        # IR sensor
        Le = trModule.lmost()
        Lc = trModule.lless()
        M = trModule.center()
        Rc = trModule.rless()
        Re = trModule.rmost()
        led = (Le, Lc, M, Rc, Re)
        hled = (Lc, M, Rc)

        #print LeD

        # to forward
        if hled == (1,0,1) and obr == False and obl == False:
            go_forward_any(35)
        # to left
        elif hled == (0,0,1) and obr == False and obl == False:
            mazetracker(40, 55)
        elif hled == (0,1,1) and obr == False and obl == False:
            mazetracker(0, 60)
        # to right
        elif hled == (1,0,0) and obr == False and obl == False:
            mazetracker(55, 40)
        elif hled == (1,1,0) and obr == False and obl == False:
            mazetracker(60, 0)
        elif led == (1,0,0,0,0) or led == (1,1,0,0,0):
            obr = True
            stop()
            go_forward(30, 0.6)
        elif led == (0,0,0,0,1) or led == (0,0,0,1,1):
            obl = True
            stop()
            go_forward(30, 2)

        if hled != (1,1,1) and obr == True:
            rightPointTurn(80, 0.3)
            while hled == (1,1,1):
                rightPointTurn(80, 0.1)
                hled = (Lc, M, Rc)
            
        
     


    print 'Shutdown'            
    pwm_low()


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
