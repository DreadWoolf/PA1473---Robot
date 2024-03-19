#!/usr/bin/env pybricks-micropython

from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
ev3 = EV3Brick()
clawMotor = Motor(Port.A)
if __name__ == "__main__":

    
    ev3.speaker.beep()
    

    ev3.speaker.beep()
    clawMotor.run(500)
    ev3.speaker.beep()
    wait(3000)
    ev3.speaker.beep()
    clawMotor.run(-500)
    ev3.speaker.beep()
