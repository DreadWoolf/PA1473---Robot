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

    while temp:
        buttons = ev3.buttons.pressed()
        print(buttons)
        for button in buttons:
            button_str = str(button)
            if button_str == "Button.UP":
                elevationMotor.run_angle(60,-10)
            if button_str == "Button.DOWN":
                elevationMotor.run_angle(60,10)
            if button_str == "Button.CENTER":
                horangle = rotationMotor.angle() 
                verangle = elevationMotor.angle()
                rotationMotor.run_angle(60,-horangle)
                elevationMotor.run_angle(60,-verangle)
                temp=False 
            if button_str == "Button.LEFT":
                rotationMotor.run_angle(60,-10)
            if button_str == "Button.RIGHT":
                rotationMotor.run_angle(60,10)

def getColor():
    # Get RGB values from the sensor (assuming they are in the range 0-100)
    fcolor = colorSense.color()
    dis = 2
    aos = 2
    Tred, Tgreen, Tblue, Tref = 0,0,0,0
    for i in range(aos):   
        red, green, blue = colorSense.rgb()
        ref = colorSense.reflection()
        Tref += ref
        Tred += red
        Tgreen += green
        Tblue += blue
        wait(10)
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
        ("Yellow", lambda r, g, b, re:(abs(g - (r/2)) <= margin) and (g > b + margin and g > b - margin) and (r > b + margin and r > b - margin ) or fcolor =="Color.YELLOW"),
        ("Green", lambda r, g, b, re: abs(g - b) <= margin and (g > r + margin or g > r - margin) and (b > r + margin or b > r - margin) and g > (margin-lmargin)*dis and b > (margin-lmargin)*dis ),  # Condition for Greenb
        ("nothing", lambda r, g, b, re: ((margin)>=r>=0) and ((margin)>=g>=0) and ((margin)>=b>=0))
        # Add more colors here
        # ("ColorName", lambda r, g, b: <condition>)
    ]
    
    # Check each color condition
    for color_name, condition in colors:
        if condition(Tred, Tgreen, Tblue, Tref):
            return color_name
        
    return "unknown item"  # Object doesn't match any color predominantly

def menu():
    choicelist = ["start_code","zonecolor_selection", "zone_hight", "set_origin"]
    current_index=0
    temp=True
    
    ev3.screen.print(choicelist[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(choicelist)
                ev3.screen.print(choicelist[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(choicelist)
                ev3.screen.print(choicelist[current_index])
            
            if str(button) == "Button.CENTER":
                ev3.screen.clear()
                ev3.screen.print("you chose ",choicelist[current_index])
                if choicelist[current_index] == "zone_hight":
                    zonecords = zone_hight()
                    print(zonecords)
                if choicelist[current_index] == "set_origin":
                    origin = set_origin()
                    print(origin)

def zone_hight():
    zonenum = [1,2,3]
    zonecords = {"1":[],
                 "2":[],
                 "3":[]
                 }
    rotationMotor.reset_angle(0)
    elevationMotor.reset_angle(0)
    horangle = 0 
    verangle = 0
    temp=True
    for num in zonenum:
        temp=True
        ev3.screen.clear()
        ev3.screen.print("chose the location \n of zone: ",num)
        while temp:
            buttons = ev3.buttons.pressed()
            wait(250)
            for button in buttons:
                button_str = str(button)
                if button_str == "Button.UP":
                    elevationMotor.run_angle(60,-10)
                if button_str == "Button.DOWN":
                    elevationMotor.run_angle(60,10)
                elif button_str == "Button.CENTER":
                    horangle = rotationMotor.angle() 
                    verangle = elevationMotor.angle()
                    zonecords[str(num)] =[horangle,verangle]
                    if num == 3:
                        return zonecords
                    temp=False
                if button_str == "Button.LEFT":
                    rotationMotor.run_angle(60,-10)
                if button_str == "Button.RIGHT":
                    rotationMotor.run_angle(60,10)
def set_origin():
    origin=[]
    temp=True
    while temp:
        buttons = ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            button_str = str(button)
            if button_str == "Button.UP":
                elevationMotor.run_angle(60,-10)
            if button_str == "Button.DOWN":
                elevationMotor.run_angle(60,10)
            elif button_str == "Button.CENTER":
                horangle = rotationMotor.angle() 
                verangle = elevationMotor.angle()
                origin = [horangle,verangle]
                return origin
            if button_str == "Button.LEFT":
                rotationMotor.run_angle(60,-10)
            if button_str == "Button.RIGHT":
                rotationMotor.run_angle(60,10)
