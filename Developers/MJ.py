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


def work_hours():
    temp=True
    ev3.screen.clear()
    amount = 0
    aoi = 0
    ev3.screen.print("how many time\nstamps do you want: ", amount)
    while temp == True:
        buttons = ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            button_str=str(button)
            if button_str == "Button.UP":
                ev3.screen.clear()
                amount += 1
                ev3.screen.print("how many time\nstamps do you want: ", amount)
            if button_str == "Button.DOWN":        
                if amount >= 1:
                    ev3.screen.clear()
                    amount -= 1
                    ev3.screen.print("how many time\nstamps do you want: ", amount)
            if button_str == "Button.CENTER":
                ev3.screen.clear()
                aoi= amount 
                ev3.screen.print("you chosse this amout\nof time stamps: ", amount)
                wait(500)
                temp= False
    temp = True
    year=[0,0,0,0]
    ev3.screen.clear()
    ev3.screen.print("you chosse this amout\nof time stamps: ")
    counter = 0
    for i in year:
        counter += 1
        while temp == True:
            buttons = ev3.buttons.pressed()
            wait(250)
            for button in buttons:
                button_str=str(button)

                if button_str == "Button.UP":
                    ev3.screen.clear()
                    i+=1
                    ev3.screen.print( counter ,"number of the year: " , i )
                if button_str == "Button.DOWN":  
                    ev3.screen.clear()
                    i-=1
                    ev3.screen.print( counter ,"number of the year: " , i )
                if button_str == "Button.CENTER":
                    ev3.screen.clear()
                    ev3.screen.print( counter ,"number of the year: " , i )
                    year[counter-1] = i
    year_str = ''.join(map(str, year))
    int_year = int(year_str)
    

                






## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    main()

