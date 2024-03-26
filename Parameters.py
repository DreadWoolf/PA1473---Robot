#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


import random


# Your code goes here
# Robot definitions
ev3 = EV3Brick()

# Motor definitions
elevationMotor = Motor(Port.B)  #8, 40
clawMotor = Motor(Port.A)
rotationMotor = Motor (Port.C) #12, 36

# Sensor definitions
colorSense = ColorSensor(Port.S2)
pressureSense = TouchSensor(Port.S1)


RobotRegister = {
    'A' : 0,  ## Accurate
    'B' : 19,
    'C' : 0,
    'D' : 0,  ## Accurate
    'E' : 0,
    'F' : 0,
    'G' : 0   ## Accurate
}

RobotIdentity = 'B'
 

zones = {
    0: 'DropOf',
    1: 'red',
    2: 'blue',
    3: 'yellow'
}

errorMargin = RobotRegister[RobotIdentity]

zoneLocation = {
    0: 0,
    1: 90 + errorMargin,
    2: 135 + errorMargin + 2,
    3: 180 + errorMargin + 3
}

zoneHeight = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}