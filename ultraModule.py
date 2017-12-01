import RPi.GPIO as GPIO  # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

class ultraModule:
    trig = 33
    echo = 31
    distance_value = 0
    started = True

    #  ultrasonic sensor setting
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    def getDistance(self):
        GPIO.output(self.trig, False)
        time.sleep(0.01)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        return distance

    def setup(self):
        self.loop(self)

    def loop(self):
        try:
            while True:
                if not(self.started):
                    break
                self.distance_value = self.getDistance(self)
        except KeyboardInterrupt:
            self.stop(self)

    def stop(self):
        self.started = False

    def getDistance_Value(self):
        return self.distance_value