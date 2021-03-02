#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S4)

ev3 = EV3Brick()
ev3.speaker.beep()

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=51, axle_track=127)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 10
WHITE = 95
threshold = (BLACK + WHITE) / 2


# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = -40

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2

# go straight 2'
def go_straight():
    robot.straight(610)

    robot.turn(180)

    robot.straight(610)

# Start following the line endlessly.
def line_follow():

    while True:
        
        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold    
        
        # Calculate the turn rate.
        turn_rate = -1 * PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)

while True:

    pressed_btn = ev3.buttons.pressed()

    if pressed_btn == [Button.UP]:
        
        ev3.speaker.say("Let's do this fucking thing!  Its line following time.")    
        line_follow()
        break  

    if pressed_btn == [Button.DOWN]:
        
        ev3.speaker.say("Yeah bro, I'm totally straight")    

        robot.settings(straight_speed=100)
        go_straight()
        break    

    wait(10)
