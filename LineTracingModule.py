import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = True
    isDEBUG_START = False
    isPassing_Func = False
    isTurnPass = False
    # ------------------ #
    trackLeftValue = [20, 60]
    trackRightValue = [60, 20]
    isLeftValue = [50, 70]
    isRightValue = [70, 50]
    isDefaultLine = [25, 25]

    # ------------------ #
    distance_Val = 0

    def setup(self, trModule):
        GPIO.setwarnings(False)
        pwm_setup()
        self.started = True
        self.loop(trModule)

    def loop(self, trModule):
        try:
            while True:
                if not self.started:
                    break

                self.isPassing_Func = False

		
		if trModule.isForward():
                    motor_accurate_set(35, 35)
                    print("isFoward")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True
	
		sleep(0.05)
		motor_stop()

                if trModule.isSemiLeft():
                    motor_accurate_set(30, 45)
                    print("isSemiLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerLeft():
                    motor_accurate_set(0, 60)
                    print("isHighPowerLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isSemiRight():
                    motor_accurate_set(45, 30)
                    print("isSemiRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerRight():
                    motor_accurate_set(60, 0)
                    print("isHighPowerRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func= True

		sleep(0.012)

                if trModule.isNeedLeft():
                    motor_stop()
                    sleep(2)
                    print("isLeft")
                    self.Turn(trModule, True, False)  # Left-Turn, not U-Turn
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isNeedRight():
                    motor_stop()
                    sleep(2)
                    print("isRight")
                    self.Turn(trModule, False, False)  # not Left-Turn, not U-Turn
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isStrongLeft():
                  #  motor_stop()
                  #  sleep(2)
		    motor_accurate_set(0, 70)
		    sleep(0.015)
                    print("isStrongLeft")
                  #  # ------------------ #
                  #  while True:
                  #      if trModule.rmost() == 0:
                  #          break
                  #      leftPointTurn(25, 25)
		  #	sleep(0.05)
                  #  # ------------------ #
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isStrongRight():
                  #  motor_stop()
                  #  sleep(2)
		    motor_accurate_set(70, 0)
		    sleep(0.015)
                    print("isStrongRight")
                  #  # ------------------ #
                  #  while True:
                  #      if trModule.lmost() == 0:
                  #          break
                  #      rightSwingTurn(20)
                  #  # ------------------ #
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isAllBlack():
                    if not self.isRightHand:
                        self.Turn(trModule, True, False) #Left-Turn, not U-Turn
                        print("AllBlack_LEFT")
                    else:
                        self.Turn(trModule, False, False) #not Left-Turn, not U-Turn
                        print("AllBlack_RIGHT")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isAllWhite():
                    self.Turn(trModule, False, True) #not Left-Turn, U-Turn
                    print("U-Turn")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                #if self.isDEBUG_START and not self.isPassing_Func:
               #    #isDebug
                print(trModule.isTrackingModuleDebug())
                #    motor_stop()
                #    break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            pwm_low()

    def Turn(self, trModule, isLeftTurn, isUTurn):
        try:
	    if not isUTurn:
                # Slightly forward
                while True:
		    motor_accurate_set(30, 30)
		    sleep(0.8)
                    if trModule.isAllWhite():
                        motor_stop()
                        break
		    elif not trModule.isAllWhite():
			motor_stop()
			if not self.isRightHand and not isLeftTurn:
			    self.isTurnPass = True
			break

	    print(self.isTurnPass)
		
            if not self.isTurnPass:
                # Inertia movement prevention
		sleep(1)
		print("pass1")
                # Rotate until sensor finds line
                while True:
                    if not isUTurn:
                        if isLeftTurn:
                            if trModule.isLeftFoundLine():
                                motor_stop()
                                break
                            leftSwingTurn(self.isLeftValue[1])
                            sleep(0.15)
			    print("LeftTurn Working")
                        else:
                            if trModule.isRightFoundLine():
                                motor_stop()
                                break
                            rightSwingTurn(self.isRightValue[0])
                            sleep(0.15)
			    print("RightTurn Working")
                    else:
                        if trModule.isRightFoundLine():
                            motor_stop()
                            break
                        rightSwingTurn(50)
		        sleep(0.3)
                        print("U-Turn Working")
                    self.Inertia_prevention()
	    self.isTurnPass = False
        except Exception as e:
            print("(Turn) An error occurred while running the program.")
            print(e)

    def Inertia_prevention(self):
        motor_stop()
        sleep(0.3)

    def stop(self):
        self.started = False
