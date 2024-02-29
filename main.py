#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase




# Your code goes here
# Robot definitions
ev3 = EV3Brick()

# Motor definitions
elevationMotor = Motor(Port.B)
clawMotor = Motor(Port.A)
rotationMotor = Motor (Port.C)
# robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=robotAxletrack[RobotIdentity])

# Sensor definitions
colorSense = ColorSensor(Port.S2)
pressureSense = TouchSensor(Port.S1)

# distance_sensor = UltrasonicSensor(Port.S4)

"""
Important! The code may not function correctly if the first line from the template is not included.
"""
 

def main():
    speed = startspeed = 50
    tmpDistance = 0

    calibrationTime = 5000 # 5s #2000

    parkAmount = 5  # 3
    parklength = 230    ##200
    parkDepth =  200    ##100
    currentParking = parkAmount
    parkSpace = []
    shouldpark = False
    
    ## k and m is for an equation for calibration of proportional_gain.
    k = -0.5
    m = 18
    PROPORTIONAL_GAIN = 3.5

    ev3.speaker.beep()


    # elevationMotor.control.limits(speed=60, acceleration=120)


    # Run the code for all eternity!
    while True:
        rotate(speed = 60)










def rotate(speed, speed_limit = 60, acceleration_limit = 120):
    smallGear = 12  #Tooths
    bigGear = 36   #Tooths
    multiplyAngle = (bigGear/smallGear)

    rotationMotor.control.limits(speed=speed_limit, acceleration=acceleration_limit)
    # angle = 90 * multiplyAngle

    
    if pressureSense.pressed():
        print("Angle ", rotationMotor.angle())
        rotationMotor.reset_angle(0)
        rotationMotor.run_angle(speed,-90 * multiplyAngle)
        print("Changed Angle ", rotationMotor.angle())
        wait(4000)
    else:
        rotationMotor.run(60)




# class SortingRobot:
#     def __init__(self, zone, color):
#         self.zone = zone
#         self.color = color

#     def write(self, zone):
#         print(zone)

#     def rotate(self, speed):
#         rotate(speed)


# zones = {
#     1: 'Red',
#     2: 'blue'
# }

# color = 'red'
# robot = SortingRobot(zones, color)
# SortingRobot.write()



def getColor():
    get_color = 'red'
    return get_color


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    main()

