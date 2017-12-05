import RPi.GPIO as GPIO


class trackingModule:
    # ------------------ #
    leftmostled_pin = 16
    leftlessled_pin = 18
    centerled_pin = 22
    rightlessled_pin = 40
    rightmostled_pin = 32
    # ------------------ #

    def pinSetup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.leftmostled_pin, GPIO.IN)
        GPIO.setup(self.leftlessled_pin, GPIO.IN)
        GPIO.setup(self.centerled_pin, GPIO.IN)
        GPIO.setup(self.rightlessled_pin, GPIO.IN)
        GPIO.setup(self.rightmostled_pin, GPIO.IN)

    def setup(self):
        self.pinSetup()

    def lmost(self):
        return GPIO.input(self.leftmostled_pin)

    def lless(self):
        return GPIO.input(self.leftlessled_pin)

    def center(self):
        return GPIO.input(self.centerled_pin)

    def rless(self):
        return GPIO.input(self.rightlessled_pin)

    def rmost(self):
        return GPIO.input(self.rightmostled_pin)

    def isForward(self):
        return (self.lless() == 1 and self.center() == 0 and self.rless() == 1) or (self.lless() == 0 and self.center() == 0 and self.rless() == 0)

    def isSemiLeft(self):
        return self.lless() == 0 and self.center() == 0 and self.rless() == 1

    def isSemiRight(self):
        return self.lless() == 1 and self.center() == 0 and self.rless() == 0

    def isHighPowerLeft(self):
        return self.lless() == 0 and self.center() == 1 and self.rless() == 1

    def isHighPowerRight(self):
        return self.lless() == 1 and self.center() == 1 and self.rless() == 0

    def isNeedLeft(self):
        return self.lmost() == 0 and self.lless() == 0 and self.rmost() == 1

    def isNeedRight(self):
        return self.lmost() == 1 and self.rless() == 0 and self.rmost() == 0

    def isStrongLeft(self):
        return self.lmost() == 0 and self.center() == 1  and self.rmost() == 1

    def isStrongRight(self):
        return self.lmost() == 1 and self.center() == 1 and self.rmost() == 0

    def isAllBlack(self):
        return self.lmost() == 0 and self.lless() == 0 and self.center() == 0 and self.rless() == 0 and self.rmost() == 0

    def isAllWhite(self):
        return self.lmost() == 1 and self.lless() == 1 and self.center() == 1 and self.rless() == 1  and self.rmost() == 1

    def isLeftFoundLine(self):
        return self.lless() == 0 or self.center() == 0

    def isRightFoundLine(self):
        return self.center() == 0 or self.rless() == 0

    def isTrackingModuleDebug(self):
        return "[DEBUG] : LeftMost = ", self.lmost(), " LeftLess = ", self.lless(), " Center = ", self.center(), " RightLess = ", self.rless(), " RightMost = ", self.rmost()