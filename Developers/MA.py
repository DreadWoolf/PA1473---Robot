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
colorSense = ColorSensor(Port.S2)
pressureSense = TouchSensor(Port.S1)
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



def manual_movment():
    ###########################
    ##### reset function ######
    ###########################
    rotationMotor.reset_angle(0)
    elevationMotor.reset_angle(0)
    horangle = 0 
    verangle = 0
    temp=True

    #elevationMotor.run_angle(60,90*multiplyAngle)

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

def getColor():
    # Get RGB values from the sensor (assuming they are in the range 0-100)
    fcolor = colorSense.color()
    dis = 3
    aos = 3
    Tred, Tgreen, Tblue, Tref = 0,0,0,0
    for i in range(aos):   
        red, green, blue = colorSense.rgb()
        ref = colorSense.reflection()
        Tref += ref
        Tred += red
        Tgreen += green
        Tblue += blue
    Tred = Tred//aos
    Tgreen = Tgreen//aos
    Tblue = Tblue//aos
    Tref = Tref//aos
    Tred, Tgreen, Tblue = dis*Tred, dis*Tgreen, dis*Tblue
    # Define margin of error
    margin = 15  # Adjust the margin as needed
    lmargin = 5
    # Define colors and their conditions
    colors = [
        ("Red", lambda r, g, b ,re: (r > g + margin and r > g - margin) and (r > b + margin and r > b - margin ) and (r > (margin - lmargin)*dis) and  (50+lmargin>=re>=50-lmargin)),
        ("Green", lambda r, g, b ,re: (g > r + margin and g > r - margin) and (g > b + margin and g > b - margin) and (g > (margin - lmargin)*dis) or  fcolor=="Color.GREEN"),
        ("Blue", lambda r, g, b, re: (b > r + margin and b > r - margin) and (b > g + margin and b > g - margin) and (b > (margin - lmargin)*dis)),
        ("Yellow", lambda r, g, b, re:(abs(g - r) <= margin) and (g > b + margin and g > b - margin) and (r > b + margin and r > b - margin ) or fcolor =="Color.YELLOW"),
        ("Greenb", lambda r, g, b, re: abs(g - b) <= margin and (g > r + margin or g > r - margin) and (b > r + margin or b > r - margin) and g > (margin-lmargin)*dis and b > (margin-lmargin)*dis ),  # Condition for Greenb
        ("nothing", lambda r, g, b, re: ((margin)>=r>=0) and ((margin)>=g>=0) and ((margin)>=b>=0))
        # Add more colors here
        # ("ColorName", lambda r, g, b: <condition>)
    ]
    
    # Check each color condition
    for color_name, condition in colors:
        if condition(Tred, Tgreen, Tblue, Tref):
            print(color_name)
            print(Tred,Tgreen,Tblue)
            return color_name
        
    return "unknown item"  # Object doesn't match any color predominantly

while True:
    getColor()
