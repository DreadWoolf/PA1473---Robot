#!/usr/bin/env pybricks-micropython
'''#!/usr/bin/env pybricks-micropython

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
    print(yeah)
    for button in yeah:
        combos = [str(obj) for obj in yeah]
        button_str = str(button)
        if button_str == "Button.UP":
            elevationMotor.run_angle(60,-10)
        if button_str == "Button.DOWN":
            elevationMotor.run_angle(60,10)
        # elif button_str == "Button.CENTER":
        #     horangle = rotationMotor.angle() 
        #     verangle = elevationMotor.angle()
        #     rotationMotor.run_target(60,-horangle)
        #     elevationMotor.run_target(60,-verangle)
        #     temp=False 
        if button_str == "Button.LEFT":
            rotationMotor.run_angle(60,-10)
        if button_str == "Button.RIGHT":
            rotationMotor.run_angle(60,10)
        if combos == ["Button.RIGHT", "Button.LEFT"] or combos == ["Button.LEFT", "Button.RIGHT"] :
           clawMotor.run_angle(10,-10)
        if combos == ["Button.UP", "Button.DOWN"] or combos == ["Button.DOWN", "Button.UP"] :
           clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None)  


    print("hor angle ===",horangle)
    print ("rael hor angle ===",rotationMotor.angle() )
    print("ver angle ===",verangle)
    print("real ver angle ===", elevationMotor.angle())'''

#------------^^----------buttons------------^^-----------------------------
'''
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
elevationMotor.run_angle(-30,(60) * multiplyAngle)
#print(clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None))

#clawMotor.run_angle(60 ,(60) * multiplyAngle)
#print(clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None))
# print(elevationMotor.run_until_stalled(30, then=Stop.BRAKE, duty_limit=None))'''
#-------------^^-------------stall------------------^^--------------------------------------
'''
# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import random
ev3 = EV3Brick()

ev3.screen.print("\n\n      :D ")
yeah = ev3.buttons.pressed()

def assign_colors():
    ev3.screen.clear()
    ev3.screen.print("Assign colors to zones:\n")
    for i in range(1, 5):
        zone_color = input("Enter color for zone " + str(i) + " (red, blue, yellow, green): ").lower()
        if zone_color == "red":
            ev3.screen.print("Zone " + str(i) + ": Red\n")
        elif zone_color == "blue":
            ev3.screen.print("Zone " + str(i) + ": Blue\n")
        elif zone_color == "yellow":
            ev3.screen.print("Zone " + str(i) + ": Yellow\n")
        elif zone_color == "green":
            ev3.screen.print("Zone " + str(i) + ": Green\n")
        else:
            ev3.screen.print("Invalid color for zone " + str(i) + ". Please enter red, blue, yellow, or green.\n")

# Call the function to assign colors
assign_colors()
'''
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import random
zoneSort = {
    'red'       : 0,
    'green'     : 1,
    'blue'      : 2,
    'yellow'   : 3
}    
ev3 = EV3Brick()
def menu():
    colors = ["Red","Yellow", "Green","Blue"]
    if len(colors) == 0:
        return zoneSort
    current_index=0
    temp = True
    ev3.screen.print(colors[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(colors)
                ev3.screen.print(colors[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(colors)
                ev3.screen.print(colors[current_index])
            
            if str(button) == "Button.CENTER":
                ev3.screen.clear()
                chosen = colors.pop(current_index)
                print("Colors:", colors)
                print("popped:", chosen)
                chosen_zone = zoneSort[chosen.lower()] 
                #ev3.screen.print("you chose ",choicelist[current_index])
                #temp=False

            print(zoneSort)   


print(menu())
