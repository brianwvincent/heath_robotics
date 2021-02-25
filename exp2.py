#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

for ii in range(10):

    wait(500)
    ev3.speaker.beep()

# wait(2000)

# lft_whl = Motor(Port.A)
# rt_whl = Motor(Port.B)
# arm = Motor(Port.C)

# whl_dm = 51 # 2 inch
# axl_tk = 127


# # program start here
# robot = DriveBase(lft_whl, rt_whl, whl_dm, axl_tk)

# robot.straight(25)

# robot.turn(90)

# robot.straight(-25)