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
'''from pybricks import robotics
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
def colorzones():
    counter = 0
    colors = ["Red","Yellow", "Green","Blue"]
    current_index=0
    temp = True
    ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            if len(colors) == 0:
                ev3.screen.print("done!")
                temp = False
                return zoneSort
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(colors)
                ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(colors)
                ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
            
            if str(button) == "Button.CENTER":
                counter += 1
                ev3.screen.clear()
                chosen = colors.pop(current_index % len(colors))
                print("Colors:", colors)
                print("popped:", chosen)
                zoneSort[chosen.lower()] = counter
                #chosen_zone = zoneSort[chosen.lower()] 
                #ev3.screen.print("you chose ",choicelist[current_index])
                #temp=False

            print(zoneSort)   
theend = colorzones()
print("OKAY STOP")
print(theend)'''
#-----------------^---------------colorzones------------^------------
'''from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
ev3.speaker.set_volume(100)
color = "A person who thinks all the time Has nothing to think about except thoughts So... he loses touch with reality And lives in a world of illusions By thoughts I mean specifically, Chatter in the skull Perpetual and compulsive repetition of words, of reckoning and calculating I'm not saying that thinking is bad Like everybody else It's useful in moderation A good servant, but a bad master And all civilized peoples Have increasingly become crazy and self destructive Because through excessive thinking The have lost touch with reality That to say... We confuse signs With the real world... This is the beginning of meditation Most of us would have Rather money than tangible wealth And a great occasion is somehow spoiled for us unless photographed And to read about it the next day in the newspaper Is oddly more fun for us than the original event This is a disaster... For as a result of confusing the real world of nature with mere signs We are destroying nature We are so tied up in our minds that we've lost our senses Time to wake up What is reality? Obviously... no one can say Because it isn't words It isn't material, that's just an idea Reality is... The point cannot be explained in words Im not trying to put you down It's an expression of you as you are One must live... We need to survive to go on... We must go on."
ev3.speaker.say("The color is " + color)'''
#-------------^^------voice---^^------------
