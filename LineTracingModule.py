import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
    isTurnEnd = False
    isDEBUG_START = False
    isPassing_Func = False
    # ------------------ #
    isLeftValue = [50, 50]
    isRightValue = [50, 50]
    isDefaultLine = [35, 35]
    # ------------------ #
    distance_Val = 0

    def setup(self, trModule, utModule):
        GPIO.setwarnings(False)
        pwm_setup()
        self.started = True
        self.loop(trModule, utModule)

    def loop(self, trModule, utModule):
        try:
            while True:
                if not self.started:
                    break

                #distance_Val = utModule.getDistance()
                self.isPassing_Func = False

                if trModule.isSemiLeft():
                    motor_stop()
                    motor_accurate_set_time(self.isDefaultLine[0], self.isDefaultLine[1] + 5, 0.1)
                    print("isSemiLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isSemiRight():
                    motor_stop()
                    motor_accurate_set_time(self.isDefaultLine[0] + 5, self.isDefaultLine[1], 0.1)
                    print("isSemiRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerLeft():
                    motor_stop()
                    motor_accurate_set_time(self.isDefaultLine[0], self.isDefaultLine[1] + 20, 0.1)
                    print("isHighPowerLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerRight():
                    motor_stop()
                    motor_accurate_set_time(self.isDefaultLine[0] + 20, self.isDefaultLine[1], 0.1)
                    print("isHighPowerRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isStrongLeft():
                    motor_stop()
                    # ------------------ #
                    while True:
                        if trModule.rmost() == 0:
                            break
                        leftSwingTurn_time(30, 0.1)
                    # ------------------ #
                    print("isStrongLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if self.isTurnEnd:
                    if trModule.isStrongRight():
                        motor_stop()
                        # ------------------ #
                        while True:
                            if trModule.lmost() == 0:
                                break
                            rightSwingTurn_time(30, 0.1)
                        # ------------------ #
                        print("isStrongRight")
                        if self.isDEBUG_START:
                            self.isPassing_Func = True

                    if trModule.isNeedLeft():
                        motor_stop()
                        self.Turn(trModule, True, False)  # Left-Turn, not U-Turn
                        print("isLeft")
                        if self.isDEBUG_START:
                            self.isPassing_Func = True
                        self.isTurnEnd = False

                if trModule.isNeedRight():
                    motor_stop()
                    self.Turn(trModule, False, False)  # not Left-Turn, not U-Turn
                    print("isRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isForward():
                    motor_stop()
                    motor_accurate_set(35, 35)
                    print("isFoward")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isAllBlack():
                    motor_stop()
                    if not self.isRightHand:
                        self.Turn(trModule, True, False) #Left-Turn, not U-Turn
                        print("AllBlack_LEFT")
                    else:
                        self.Turn(trModule, False, False) #not Left-Turn, not U-Turn
                        print("AllBlack_RIGHT")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isAllWhite():
                    motor_stop()
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
                motor_accurate_set_time(30, 30, 0.3)

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