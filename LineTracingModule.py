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
    isLeftValue = [30, 15]
    isRightValue = [15, 30]
    isDefaultLine = [22, 20]
    # ------------------ #
    distance_Val = 0

    def setup(self, trModule):
        GPIO.setwarnings(False)
        pwm_setup()
        self.started = True
        self.loop(trModule)

    def loop(self, trModule, utModule):
        try:
            while True:
                if not self.started:
                    break

                distance_Val = utModule.getDistance()
                self.isPassing_Func = False

                if trModule.isMediumPowerLeft():
                    motor_accurate_set(self.isDefaultLine[1], self.isDefaultLine[0] + 6)
                    print("isMediumPowerLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isMediumPowerRight():
                    motor_accurate_set(self.isDefaultLine[0] + 6, self.isDefaultLine[1])
                    print("isMediumPowerRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerLeft():
                    motor_accurate_set(self.isDefaultLine[1], self.isDefaultLine[0] + 4)
                    print("isHighPowerLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isHighPowerRight():
                    motor_accurate_set(self.isDefaultLine[0] + 4, self.isDefaultLine[1])
                    print("isHighPowerRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isSemiLeft():
                    motor_accurate_set(self.isDefaultLine[1], self.isDefaultLine[0])
                    print("isSemiLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isSemiRight():
                    motor_accurate_set(self.isDefaultLine[0], self.isDefaultLine[1])
                    print("isSemiRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isNeedLeft():
                    self.Turn(trModule, True, False)  # Left-Turn, not U-Turn
                    print("isLeft")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isNeedRight():
                    self.Turn(trModule, False, False)  # not Left-Turn, not U-Turn
                    print("isRight")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                if trModule.isForward():
                    motor_accurate_set(30, 30)
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

                if self.isDEBUG_START and self.isPassing_Func:
                    #isDebug
                    print(trModule.isTrackingModuleDebug())
                    motor_stop()
                    break

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
                motor_accurate_set(40, 40)

            # Inertia movement prevention
            sleep(2)

            # Rotate until sensor finds line
            while True:
                if not isUTurn:
                    if isLeftTurn:
                        if trModule.isLeftFoundLine():
                            motor_stop()
                            break
                        leftPointTurn_time(self.isLeftValue[0], self.isLeftValue[1], 0.3)
                        print("LeftTurn Working")
                    else:
                        if trModule.isRightFoundLine():
                            motor_stop()
                            break
                        rightPointTurn_time(self.isRightValue[0], self.isRightValue[1], 0.3)
                        print("RightTurn Working")
                    self.Inertia_prevention()
                else:
                    if trModule.isRightFoundLine():
                        motor_stop()
                        break
                    rightSwingTurn_time(50, 0.6)
                    print("U-Turn Working")
                    self.Inertia_prevention()
        except Exception as e:
            print("(Turn) An error occurred while running the program.")
            print(e)

    def Inertia_prevention(self):
        motor_stop()
        sleep(0.3)

    def stop(self):
        self.started = False