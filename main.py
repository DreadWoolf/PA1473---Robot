#!/usr/bin/env pybricks-micropython
<<<<<<< HEAD
=======
"""# #!/usr/bin/env pybricks-micropython
>>>>>>> f4129f5b6acebd30f863c83f9e0de8352cee4128

# # Pybricks imports
# from pybricks import robotics
# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
# from pybricks.parameters import Port, Stop, Direction, Color
# from pybricks.tools import wait, StopWatch
# from pybricks.robotics import DriveBase


# import random


# # Your code goes here
# # Robot definitions
# ev3 = EV3Brick()

# # Motor definitions
# elevationMotor = Motor(Port.B)  #8, 40
# clawMotor = Motor(Port.A)
# rotationMotor = Motor (Port.C) #12, 36

# # Sensor definitions
# colorSense = ColorSensor(Port.S2)
# pressureSense = TouchSensor(Port.S1)


# RobotRegister = {
#     'A' : 0,  ## Accurate
#     'B' : 19,
#     'C' : 0,
#     'D' : 0,  ## Accurate
#     'E' : 0,
#     'F' : 0,
#     'G' : 0   ## Accurate
# }

# RobotIdentity = 'B'
 

# zones = {
#     0: 'DropOf',
#     1: 'red',
#     2: 'blue',
#     3: 'yellow'
# }

# errorMargin = RobotRegister[RobotIdentity]

# zoneLocation = {
#     0: 0,
#     1: 90 + errorMargin,
#     2: 135 + errorMargin + 2,
#     3: 180 + errorMargin + 3
# }

# zoneHeight = {
#     0: 0,
#     1: 0,
#     2: 0,
#     3: 0
# }"""

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import *

def main():
    ev3.speaker.beep()

    times = 5
    zoneAmount = 3
    
    print("Calibrate arm")
    

<<<<<<< Updated upstream
    Calibrate()
    # zone0Calibration()
    run = 0
    location = 1
    lastZone = 0
    # for i in range(times):
    while run < times:
        run += 1

        goToZone = location

        rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
        if cargo:
            Place(angleTarget= -35, openClawsFirst= False)
            # print("Open claws")
            # clawMovement(open = True)
            # armMovement(angleTarget= -35)

            # print("Grip")
            # clawMovement(open = False)
            # armMovement(angleTarget= 35)
        else:
            Pickup(angleTarget= -35, openClawsFirst= True)

            # print("Open claws")
            # clawMovement(open = True)
            # armMovement(angleTarget= -35)

            # print("Grip")
            # clawMovement(open = False)
            # armMovement(angleTarget= 35)

        print("Check color \nWhere to next= ", location)

        
        cargo = False

        
        if location == 2:
            cargo = True
            print("loc is True")
        
        print("YEEEEEEEEEEEEIIIIII")
        print(location)

        if cargo:
            goToZone = 0
            cargo = False
            # Go to drop of.
        else:
            if location >= zoneAmount:
                location = 0
                goToZone = 0
            else:
                lastZone = location
                location += 1
                goToZone = location

        

        print("GoToZone = ", goToZone)
        # goToZone = 0

        # rotateBase(angle=zoneLocation[goToZone])
        # # zone0Calibration()

        # armMovement(angleTarget= -35)
        # print("Let go")
        # clawMovement(open = True)
        # armMovement(angleTarget= 35)
        # print("Close the empty claws")
        # clawMovement(open = False)
        # # rotateBase(operatingSpeed= 60, angle = zoneLocation[0])

    # Go back to start, if arm is higher than ground level.
    armMovement(angleTarget= -35)

"""
# def Pickup(angleTarget:int, openClawsFirst:bool, height:int):
#     # if height <= 0:
#     clawMovement(open = openClawsFirst) # If openFirst = True will open here.
#     armMovement(angleTarget= angleTarget)
#     clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
#     armMovement(angleTarget= -angleTarget)
#     # else:
#     #     clawMovement(open = openClawsFirst) # If openFirst = True will open here.
#     #     armMovement(angleTarget= angleTarget)

#     # if openClawsFirst == False:
#     #     clawMovement(open=(not openClawsFirst))
=======
def getColor():
    # Get RGB values from the sensor (assuming they are in the range 0-100)
    red, green, blue = colorSense.rgb()
    # Define margin of error
    margin = 6  # Adjust the margin as needed
    # Define colors and their conditions
    colors = [
        ("Red", lambda r, g, b: (r > g + margin or r > g - margin) and (r > b + margin or r > b - margin ) and r > 33 - margin ),
        ("Green", lambda r, g, b: (g > r + margin or g > r - margin) and g > b + margin or g > b - margin and g > 33 - margin ),
        ("Blue", lambda r, g, b: (b > r + margin or b > r - margin) and (b > g + margin or b > g - margin) and b > 33 - margin ),
        #("Greenb", lambda r, g, b: abs(g - b) <= margin and (g > r + margin or g > r - margin) and (b > r + margin or b > r - margin) and g > 33 - margin and b > 33 - margin ),  # Condition for Greenb
        # Add more colors here
        # ("ColorName", lambda r, g, b: <condition>)
    ]
    # Check each color condition
    for color_name, condition in colors:
        if condition(red, green, blue):
            return color_name

    return "None of them"  # Object doesn't match any color predominantly
>>>>>>> Stashed changes


# def Place(angleTarget:int, openClawsFirst:bool):
#     # if openClawsFirst:

#     ## OBS kommer greppa även om håller i något!!!
    
#     clawMovement(open = openClawsFirst) # If openFirst = True will open here.
#     armMovement(angleTarget= angleTarget)
#     clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
#     armMovement(angleTarget= -angleTarget)
#     # if openClawsFirst == False:
#     #     clawMovement(open=(not openClawsFirst))



# def armMovement(angleTarget, operatingSpeed = 60):
#     # Thooths on the gears of the arm.
#     bigGear = 40
#     smallGear = 8
#     multiplyAngle = -(bigGear/smallGear)

#     print("start arm angle " , elevationMotor.angle())
#     elevationMotor.run_angle(operatingSpeed,angleTarget * multiplyAngle)
#     print("targeted arm angle " , elevationMotor.angle())
"""


def Calibrate():
    LocationZero()
    return 0


def LocationZero():
    while not pressureSense.pressed():
        rotationMotor.run(60)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, operatingSpeed = 60, speed_limit = 60, acceleration_limit = 120):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    print("angle = ", angle)

    if angle == 0:
        LocationZero()
        print("Going back")
    else:
        print("...")
        rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)



"""# def clawMovement(open:bool):
#     smallGear = 12  #Tooths for gear moving clockwise. 
#     bigGear = 16   #Tooths for gear moving counter clockwise. 
#     multiplyAngle = -(bigGear/smallGear)

#     if open:
#         clawMotor.run_angle(60 ,(60) * multiplyAngle)
#     # wait(4000)
#     else:
#         clawMotor.run_angle(60 ,(-60) * multiplyAngle)
#     return 0"""


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # armMovement(angleTarget= -35 * 2)
    # for i in range(3):
    #     clawMovement()
    main()