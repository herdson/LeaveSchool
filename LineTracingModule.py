import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
    isDEBUG_START = False
    isPassing_Func = False
    isTurnPass = False
    # ------------------ #
    trackLeftValue = [20, 60]
    trackRightValue = [60, 20]
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

                self.LineTracing(trModule, True)

                if trModule.isNeedLeft():
                    motor_stop()
                    sleep(1)
                    print("isLeft")
                    self.Turn(trModule, True, False)  # Left-Turn, not U-Turn
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                elif trModule.isNeedRight():
                    motor_stop()
                    sleep(1)
                    print("isRight")
                    self.Turn(trModule, False, False)  # not Left-Turn, not U-Turn
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                elif trModule.isAllBlack():
                    if not self.isRightHand:
                        self.Turn(trModule, True, False) #Left-Turn, not U-Turn
                        print("AllBlack_LEFT")
                    else:
                        self.Turn(trModule, False, False) #not Left-Turn, not U-Turn
                        print("AllBlack_RIGHT")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                elif trModule.isAllWhite():
                    self.Turn(trModule, False, True) #not Left-Turn, U-Turn
                    print("U-Turn")
                    if self.isDEBUG_START:
                        self.isPassing_Func = True

                #if self.isDEBUG_START and not self.isPassing_Func:
                    #isDebug
                print(trModule.isTrackingModuleDebug())
                self.isPassing_Func = False
                #    motor_stop()
                #    break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            pwm_low()

    def LineTracing(self, trModule, GoFoward):
        if GoFoward:
            if trModule.isForward():
                motor_accurate_set(35, 35)
                print("isFoward")
                if self.isDEBUG_START:
                    self.isPassing_Func = True

        # Maintain line tracing
        sleep(0.05)

        if trModule.isSemiLeft():
            motor_accurate_set(40, 55)
            print("isSemiLeft")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        if trModule.isHighPowerLeft():
            motor_accurate_set(0, 60)
            print("isHighPowerLeft")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        if trModule.isSemiRight():
            motor_accurate_set(55, 40)
            print("isSemiRight")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        if trModule.isHighPowerRight():
            motor_accurate_set(60, 0)
            print("isHighPowerRight")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        if trModule.isStrongLeft():
            motor_accurate_set(0, 70)
            print("isStrongLeft")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        if trModule.isStrongRight():
            motor_accurate_set(70, 0)
            print("isStrongRight")
            if self.isDEBUG_START:
                self.isPassing_Func = True

        # Maintain line tracing
        sleep(0.012)

    def Turn(self, trModule, isLeftTurn, isUTurn):
        try:
            # Slightly forward
            while True:
                motor_accurate_set(35, 35)
                sleep(0.7)
                if trModule.isAllWhite():
                    motor_stop()
                    break
                elif trModule.isForward or trModule.isSemiLeft or trModule.isSemiRight: # Middle line exists.
                    motor_stop()
                    if self.isRightHand and isLeftTurn: #RightHand method, left rotation.
                        self.isTurnPass = True
                        break
                    elif not self.isRightHand and not isLeftTurn: #LeftHand method, right rotation
                        self.isTurnPass = True
                        break
                    else:
                        continue

            # Inertia movement prevention
            sleep(1)

            # Rotate until sensor finds line
            if not self.isTurnPass:
                while True:
                    if not isUTurn:
                        if isLeftTurn:
                            leftPointTurn(self.trackLeftValue[0], self.trackLeftValue[1])
                            print("LeftTurn Working")
                            sleep(0.15)
                            if trModule.isLeftFoundLine():
                                motor_stop()
                                break
                        else:
                            rightPointTurn(self.trackRightValue[0], self.trackRightValue[1])
                            print("RightTurn Working")
                            sleep(0.15)
                            if trModule.isRightFoundLine():
                                motor_stop()
                                break
                    else:
                        rightSwingTurn(50)
                        sleep(0.3)
                        if trModule.isRightFoundLine():
                            motor_stop()
                            break
                        print("U-Turn Working")
                    self.Inertia_prevention()

                # unit center alignment
                self.LineTracing(trModule, False)
                self.isTurnPass = False
        except Exception as e:
            print("(Turn) An error occurred while running the program.")
            print(e)

    def Inertia_prevention(self):
        motor_stop()
        sleep(0.3)

    def stop(self):
        self.started = False