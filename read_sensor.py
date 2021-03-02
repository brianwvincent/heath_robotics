#!/usr/bin/env pybricks-micropython
import math
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
clr_sens = ColorSensor(Port.S4)

while True:

    # clr = clr_sens.color()
    # amb = clr_sens.ambient()
    # ref = clr_sens.reflection()
    rgb = clr_sens.rgb()

    rgb_mag = math.sqrt(rgb[0]**2 + rgb[1]**2 + rgb[2]**2)

    ev3.screen.print("rgb: {}".format(rgb_mag))

    # print('color: {}, ambient: {}, reflection: {}, rgb: {}'.format(clr, amb, ref, rgb_mag))
    
    wait(250)
