import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
    isUTurn = False
    # ------------------ #
    isLeftValue = [30, 15]
    isRightValue = [15, 30]
    isDefaultLine = [32, 30]
    # ------------------ #

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

                if trModule.isSemiLeft():
                    motor_accurate_set(self.isDefaultLine[1], self.isDefaultLine[0])
                    print("isSemiLeft")

                elif trModule.isSemiRight():
                    motor_accurate_set(self.isDefaultLine[0], self.isDefaultLine[1])
                    print("isSemiRight")

                elif trModule.isHighPowerLeft():
                    motor_accurate_set(self.isDefaultLine[1], self.isDefaultLine[0] + 2)
                    print("isHighPowerLeft")

                elif trModule.isHighPowerRight():
                    motor_accurate_set(self.isDefaultLine[0] + 2, self.isDefaultLine[1] + 2)
                    print("isHighPowerRight")

                elif trModule.isNeedLeft():
                    self.Turn(trModule, True, False)  # Left-Turn, not U-Turn
                    print("isLeft")

                elif trModule.isNeedRight():
                    self.Turn(trModule, False, False)  # not Left-Turn, not U-Turn
                    print("isRight")

                elif trModule.isForward():
                    motor_accurate_set(30, 30)
                    print("isFoward")

                elif trModule.isAllBlack():
                    if not self.isRightHand:
                        self.Turn(trModule, True, False) #Left-Turn, not U-Turn
                        print("AllBlack_LEFT")
                    else:
                        self.Turn(trModule, False, False) #not Left-Turn, not U-Turn
                        print("AllBlack_RIGHT")

                elif trModule.isAllWhite():
                    self.Turn(trModule, False, True) #not Left-Turn, U-Turn
                    print("U-Turn")

                else:
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
                motor_accurate_set(25, 25)

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
                    else:
                        if trModule.isRightFoundLine():
                            motor_stop()
                            break
                        rightPointTurn_time(self.isRightValue[0], self.isRightValue[1], 0.3)
                    self.Inertia_prevention()
                else:
                    if trModule.isRightFoundLine():
                        motor_stop()
                        break
                    rightSwingTurn_time(30, 0.6)
                    self.Inertia_prevention()
        except Exception as e:
            print("(Turn) An error occurred while running the program.")
            print(e)

    def Inertia_prevention(self):
        motor_stop()
        sleep(0.3)

    def stop(self):
        self.started = False