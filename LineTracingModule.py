import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
    isUTurn = False
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
                    motor_accurate_set(30, 32)
                    print("isSemiLeft")

                elif trModule.isSemiRight():
                    motor_accurate_set(32, 30)
                    print("isSemiRight")

                elif trModule.isNeedLeft():
                    # Slightly forward
                    motor_accurate_set_time(30, 30, 1)
                    while trModule.lless() == 1:
                        leftPointTurn(10)
                    print("isLeft")
                    motor_stop()

                elif trModule.isNeedRight():
                    # Slightly forward
                    motor_accurate_set_time(30, 30, 1)
                    while trModule.lless() == 1:
                        rightPointTurn(10)
                    print("isRight")
                    motor_stop()

                elif trModule.isForward():
                    motor_accurate_set(30, 30)
                    print("isFoward")

                elif trModule.isAllBlack():
                    # Slightly forward
                    motor_accurate_set_time(30, 30, 1)
                    if not self.isRightHand:
                        while trModule.lless() == 1:
                            leftPointTurn(20)
                        print("AllBlack_LEFT")
                    else:
                        while trModule.rless() == 1:
                            rightPointTurn(20)
                        print("AllBlack_RIGHT")
                    motor_stop()

                elif trModule.isAllWhite():
                    # Slightly forward
                    motor_accurate_set_time(30, 30, 1)
                    while trModule.lless() == 1:
                        rightSwingTurn(20)
                    print("U-Turn")
                    motor_stop()

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            pwm_low()

    def stop(self):
        self.started = False