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
    'A' : 0,
    'B' : 19, ## Accurate
    'C' : 0,
    'D' : 0,  
    'E' : 0,
    'F' : 0,
    'G' : 0
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
        armMovement(angleTarget= -35)

        print("Grip")
        armMovement(angleTarget= 35)
        print("Check color")
        
        calibrate()
        
        armMovement(angleTarget= -35)
        print("Let go")
        
        armMovement(angleTarget= 35)
        print("Close the empty claws")
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


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # armMovement(angleTarget=-35)
    main()