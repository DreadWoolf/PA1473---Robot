#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
elevationMotor = Motor(Port.B) 
clawMotor = Motor(Port.A)
rotationMotor = Motor (Port.C) 
smallGear = 12  #Tooths for gear moving clockwise. 
bigGear = 16   #Tooths for gear moving counter clockwise.
# smallGear = 12  #Tooths for gear moving clockwise. 
# bigGear = 36   #Tooths for gear moving counter clockwise. 
multiplyAngle = -(bigGear/smallGear)
#elevationMotor.run_angle(60,(60) * multiplyAngle)
print(clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None))

clawMotor.run_angle(60 ,(60) * multiplyAngle)
print(clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None))
# print(elevationMotor.run_until_stalled(30, then=Stop.BRAKE, duty_limit=None))
