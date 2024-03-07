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

## Orginal is 104, but then some robots do not turn accurate.
## May be because of dust in motors or something else.
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


# Sensor definitions
colorSense = ColorSensor(Port.S2)
pressureSense = TouchSensor(Port.S1)

# distance_sensor = UltrasonicSensor(Port.S4)

"""
Important! The code may not function correctly if the first line from the template is not included.
"""
 

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

    test = 3
    times = 5
    # startcolor = colorSense.color()

    # if (startcolor == "Color.Yellow"):
    #     elevationMotor.reset_angle(0)
    # else:
    #     elevationMotor.run(-60)
    # while True:

    #     rotate(operatingSpeed=60)
    # Run the code for all eternity!

    # armMovement(angleTarget=-32)

    print("the color is: ", colorSense.color())

    while times > 0:
        armMovement(angleTarget=35)  # Move arm up
        test = rotate(operatingSpeed=60, angle=zoneLocation[test])
        print("the color is: ", colorSense.color())
        armMovement(angleTarget=-35, grab_item=True)  # Move arm down and grab
        times -= 1
        armMovement(angleTarget=-45)  # Move arm to initial position






def armMovement(angleTarget, operatingSpeed = 60):
  """
  This function controls the elevation motor and optionally grabs an item.

  Args:
      angleTarget: The target angle for the elevation motor.
      operatingSpeed: The speed at which the motor operates (default: 60).
      grab_item: Boolean flag indicating whether to grab an item after movement (default: False).
  """
  # Existing code for calculating gear ratio and printing starting angle...

  elevationMotor.run_angle(operatingSpeed, angleTarget * multiplyAngle)

  # Add a new argument and conditional statement for grabbing:
  if grab_item:
    grab_item(operating_speed)

  # Print targeted angle and return...








def rotate(operatingSpeed, angle, speed_limit = 60, acceleration_limit = 120):
    smallGear = 12  #Tooths
    bigGear = 36   #Tooths
    multiplyAngle = -(bigGear/smallGear)

    # errorMargin = RobotRegister[RobotIdentity]

    # rotationMotor.control.limits(speed = speed_limit, acceleration = acceleration_limit)

    # angle = 90 * multiplyAngle

    while True:
        if pressureSense.pressed():
            print("Angle ", rotationMotor.angle())
            rotationMotor.reset_angle(0)
            rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)
            print("Changed Angle ", rotationMotor.angle())
            wait(4000)
            return (random.randint(1,3))
        else:
            rotationMotor.run(60)

    # if pressureSense.pressed():
    #     print("Angle ", rotationMotor.angle())
    #     rotationMotor.reset_angle(0)
    #     rotationMotor.run_angle(operatingSpeed, 90 * multiplyAngle)
    #     print("Changed Angle ", rotationMotor.angle())
    #     wait(4000)
    # else:
    #     rotationMotor.run(60)
            


def getColor():
    get_color = 'red'
    return get_color


def grab_item(operating_speed=60, grab_angle=90):
  """
  This function controls the claw motor to grab an item.

  Args:
      operating_speed: The speed at which the motor operates (default: 60).
      grab_angle: The angle to which the claw motor should move to grab (default: 90).
  """
  clawMotor.reset_angle(angle=0)
  clawMotor.run_angle(operating_speed, grab_angle)






## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    main()