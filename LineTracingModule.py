import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
    isDEBUG_START = False
    isPassing_Func = False
    # ------------------ #
    trackLeftValue = [20, 60]
    trackRightValue = [60, 20]
    isLeftValue = [50, 50]
    isRightValue = [50, 50]
    isDefaultLine = [35, 35]

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

                #distance_Val = utModule.getDistance()
                self.isPassing_Func = False

                if trModule.isSemiLeft():
                    motor_accurate_set(self.trackLeftValue[0] + 20, self.trackLeftValue[1] - 5)
                    print("isSemiLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isSemiRight():
                    motor_accurate_set(self.trackRightValue[0] - 5 , self.trackRightValue[1] + 20)
                    print("isSemiRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerLeft():
                    motor_accurate_set(self.trackLeftValue[0], self.trackLeftValue[1])
                    print("isHighPowerLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerRight():
                    motor_accurate_set(self.trackRightValue[0] , self.trackRightValue[1])
                    print("isHighPowerRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

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
                    motor_stop()
                    sleep(2)
                    print("isStrongLeft")
                    # ------------------ #
                    while True:
                        if trModule.rmost() == 0:
                            break
                        leftSwingTurn_time(30, 0.1)
                    # ------------------ #
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isStrongRight():
                    motor_stop()
                    sleep(2)
                    print("isStrongRight")
                    # ------------------ #
                    while True:
                        if trModule.lmost() == 0:
                            break
                        rightSwingTurn_time(30, 0.1)
                    # ------------------ #
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isForward():
                    motor_accurate_set(35, 35)
                    print("isFoward")
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
            # Slightly forward
            while True:
                if trModule.isAllWhite():
                    motor_stop()
                    break
                motor_accurate_set_time(30, 30, 1)

            # Inertia movement prevention
            sleep(2)

            # Rotate until sensor finds line
            while True:
                if not isUTurn:
                    if isLeftTurn:
                        if trModule.isLeftFoundLine():
                            motor_stop()
                            break
                        leftPointTurn_time(self.isLeftValue[0], self.isLeftValue[1], 0.1)
                        print("LeftTurn Working")
                    else:
                        if trModule.isRightFoundLine():
                            motor_stop()
                            break
                        rightPointTurn_time(self.isRightValue[0], self.isRightValue[1], 0.1)
                        print("RightTurn Working")
                    self.Inertia_prevention()
                else:
                    if trModule.isRightFoundLine():
                        motor_stop()
                        break
                    rightSwingTurn_time(50, 0.6)
                    print("U-Turn Working")
                    self.Inertia_prevention()
                self.isTurnEnd = True
        except Exception as e:
            print("(Turn) An error occurred while running the program.")
            print(e)

    def Inertia_prevention(self):
        motor_stop()
        sleep(0.3)

    def stop(self):
        self.started = False