#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()






# Write your program here.

# for ii in range(10):

#     wait(1000)
ev3.speaker.beep()

while True:

    pressed_btn = ev3.buttons.pressed()
    print(pressed_btn)
    ev3.screen.print("btn: {}".format(pressed_btn))

    if pressed_btn == [Button.UP]:
        ev3.speaker.say("Jayden, how are you today?")        
    elif pressed_btn == [Button.DOWN]:
        ev3.speaker.say("Fuck you jayden")
    elif pressed_btn == [Button.LEFT]:
        ev3.speaker.say("jayden, you're a piece of shit")
    elif pressed_btn == [Button.RIGHT]:
        ev3.speaker.say("I'M AWESOME")

    wait(10)

# ev3.speaker.set_speech_options(voice='f4')

# ev3.screen.load_image(ImageFile.ANGRY)


# for ii in range(20):
#     ev3.light.on(Color.RED)

#     wait(500)

#     ev3.light.off()

#     wait(500)


# print(ImageFile('ANGRY'))
# Image.draw_image(0,0, 'ANGRY')

# img = Image('angry')
# Image.empty()
# img.load_image('angry.png')
# img.draw_image(0,0, 'angry.png')





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