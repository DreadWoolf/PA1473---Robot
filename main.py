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


def main():
    ev3.speaker.beep()

    times = 5

    print("Calibrate arm")
    armMovement(angleTarget=35)
    calibrate()

    for i in range(times):
        goToZone = random.randint(1,3)
        rotateBase(operatingSpeed= 60, angle = zoneLocation[goToZone])
        print("Open claws")
        clawMovement(open = True)
        armMovement(angleTarget= -35)

        print("Grip")
        clawMovement(open = False)
        armMovement(angleTarget= 35)

        print("Check color")
        # run target, might be better.
        calibrate()

        armMovement(angleTarget= -35)
        print("Let go")
        clawMovement(open = True)
        armMovement(angleTarget= 35)
        print("Close the empty claws")
        clawMovement(open = False)
        # rotateBase(operatingSpeed= 60, angle = zoneLocation[0])

    # Go back to start.
    armMovement(angleTarget= -35)
    



def armMovement(angleTarget, operatingSpeed = 60):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)

    print("start arm angle " , elevationMotor.angle())
    elevationMotor.run_angle(operatingSpeed,angleTarget * multiplyAngle)
    print("targeted arm angle " , elevationMotor.angle())



def calibrate():
    while not pressureSense.pressed():
        rotationMotor.run(60)
    
    rotationMotor.reset_angle(0)


def rotateBase(operatingSpeed, angle, speed_limit = 60, acceleration_limit = 120):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)
    return 0


# def getColor():
#     get_color = 'red'
#     return get_color


def clawMovement(open:bool):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if open:
        clawMotor.run_angle(60 ,(60) * multiplyAngle)
    # wait(4000)
    else:
        clawMotor.run_angle(60 ,(-60) * multiplyAngle)
    return 0


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # armMovement(angleTarget= -35 * 2)
    # for i in range(3):
    #     clawMovement()
    main()