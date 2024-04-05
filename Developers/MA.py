#!/usr/bin/env pybricks-micropython

# Pybricks imports
import os
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
rotationMotor = Motor (Port.C) #12, 36
clawMotor = Motor(Port.A)

def clear_terminal():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')




###########################
##### reset function ######
###########################
rotationMotor.reset_angle(0)
elevationMotor.reset_angle(0)
horangle = 0 
verangle = 0
temp=True
smallGear = 12  #Tooths for gear moving clockwise. 
bigGear = 16   #Tooths for gear moving counter clockwise. 
multiplyAngle = -(bigGear/smallGear)

#elevationMotor.run_angle(60,90*multiplyAngle)

while temp:
    yeah = ev3.buttons.pressed()
    combos = [str(obj) for obj in yeah]
    print(yeah)
    for button in yeah:
        button_str = str(button)
        if button_str == "Button.UP":
            elevationMotor.run_angle(60,-10)
        elif button_str == "Button.DOWN":
            elevationMotor.run_angle(60,10)
        elif button_str == "Button.CENTER":
            horangle = rotationMotor.angle() 
            verangle = elevationMotor.angle()
            rotationMotor.run_target(60,-horangle)
            elevationMotor.run_target(60,-verangle)
            temp=False 
        elif button_str == "Button.LEFT":
            rotationMotor.run_angle(60,-10)
        elif button_str == "Button.RIGHT":
            rotationMotor.run_angle(60,10)
        # if "Button.RIGHT" in combos and "Button.LEFT" in combos:
        #     clawMotor.run_angle(60, (60) * multiplyAngle)    
        # elif "Button.UP" in combos and "Button.DOWN" in combos:
        #     clawMotor.run_angle(-60, (60) * multiplyAngle)
        # if combos == ["Button.RIGHT", "Button.LEFT"] or combos == ["Button.LEFT", "Button.RIGHT"] :
        #    clawMotor.run_angle(60 ,(60) * multiplyAngle)
        # if combos == ["Button.UP", "Button.DOWN"] or combos == ["Button.DOWN", "Button.UP"] :
        #    clawMotor.run_angle(-60 ,(60) * multiplyAngle)
#        if button_str == "Button.LEFT" and button_str == "Button.RIGHT":
#            clawMotor.run_angle(60 ,(60) * multiplyAngle)

    print("hor angle ===",horangle)
    print ("real hor angle ===",rotationMotor.angle() )
    print("ver angle ===",verangle)
    print("real ver angle ===", elevationMotor.angle())


