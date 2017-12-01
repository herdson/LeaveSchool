import RPi.GPIO as GPIO
from trackingModule import *
from MotorModule import *

class LineTracingModule:

    # ------------------ #
    started = False
    isRightHand = False
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
                    motor_accurate_set(30, 33)
                elif trModule.isSemiRight():
                    motor_accurate_set(33, 30)
                elif trModule.isForward():
                    motor_accurate_set(30, 30)
                elif trModule.isStop():
                    while trModule.center() == 1:
                        leftPointTurn(30)
                    print("CENTER == 0")
                    stop()

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            pwm_low()

    def stop(self):
        self.started = False