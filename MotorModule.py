# import GPIO library
import RPi.GPIO as GPIO
from time import sleep

# set GPIO warnings as False
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# Set the motor's true / false value to go forward.
# =======================================================================
forward0 = True
forward1 = False

# =======================================================================
# Set the motor's true / false value to go opposite.
# =======================================================================
backward0 = not forward0
backward1 = not forward1

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print("Config Error")


def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        print("Config Error")


# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

def motor_accurate_set(left_speed, right_speed):
    # set the two motor to go forward
    leftmotor(forward0)
    rightmotor(forward0)

    # set the left and two motor pwm to be ready to move
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the two motor to go backward
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)

def motor_accurate_set_time(left_speed, right_speed, running_time):
    # set the two motor to go forward
    leftmotor(forward0)
    rightmotor(forward0)

    # set the left and two motor pwm to be ready to move
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the two motor to go backward
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)

    sleep(running_time)

def leftPointTurn(left_speed, right_speed):
    # set the left motor to go backward and right motor to go forward
    leftmotor(backward0)
    rightmotor(forward0)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the two motor to go backward
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)

def rightPointTurn(left_speed, right_speed):
    # set the left motor to go backward and right motor to go forward
    leftmotor(forward0)
    rightmotor(backward0)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the two motor to go backward
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)

def leftSwingTurn(speed):
    # set the right motor to go fowrard
    rightmotor(forward0)

    # set the two motor pwm to be ready to stop
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)

def rightSwingTurn(speed):
    # set the right motor to go fowrard
    leftmotor(forward0)

    # set the two motor pwm to be ready to stop
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.LOW)

    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(0)

# =======================================================================
# define the stop module
# =======================================================================

def motor_stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)

def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)

def pwm_low():
    motor_stop()
    GPIO.cleanup()