#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import datetime



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




def get_user_input(prompt, min_value, max_value):
    """
    Get user input using buttons and limit the value between min_value and max_value.
    """
    btn = ev3.Button()
    display = ev3.Display()
    value = min_value

    while True:
        display.clear()
        display.text_pixels(prompt, x=0, y=0, font='courB14')
        display.text_pixels(str(value), x=0, y=20, font='courB14')
        if btn.up:
            value = min(max_value, value + 1)
        elif btn.down:
            value = max(min_value, value - 1)
        elif btn.enter:
            break

    return value

def get_month_days(year, month):
    """
    Get the number of days in a given month and year.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        # Leap year check
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 0

def work_times():
    # Phase 1: Choose the number of time stamps (limit between 1 and 99)
    aots = get_user_input("How many time\nstamps do you want:", 1, 99)

    # Initialize an empty dictionary to store time stamps
    timestamps = {}

    # Phase 2: Choose the year (limit between 2024 and 2100)
    year = get_user_input("Enter the year:", 2024, 2100)

    # Phase 3: Choose the month (limited between 1 and 12)
    month = get_user_input("Enter the month (1-12):", 1, 12)

    # Phase 4: Choose the day (limited between 1 and the number of days in the chosen month)
    days_in_month = get_month_days(year, month)
    day = get_user_input(f"Enter the day (1-{days_in_month}):", 1, days_in_month)

    # Phase 5: Choose the starting hour (limited between 1 and 24)
    start_hour = get_user_input("Enter the starting hour (1-24):", 1, 24)

    # Phase 6: Choose the starting minute (limited between 0 and 59)
    start_min = get_user_input("Enter the starting minute (0-59):", 0, 59)

    # Phase 7: Choose the ending hour (limited between 1 and 24)
    end_hour = get_user_input("Enter the ending hour (1-24):", 1, 24)

    # Phase 8: Choose the ending minute (limited between 0 and 59)
    end_min = get_user_input("Enter the ending minute (0-59):", 0, 59)

    # Create start_date and end_date strings
    start_date = f"{year}-{month:02d}-{day:02d} {start_hour:02d}:{start_min:02d}"
    end_date = f"{year}-{month:02d}-{day:02d} {end_hour:02d}:{end_min:02d}"

    # Check if start_date is before end_date
    if start_date < end_date:
        # Store the time stamps in the dictionary
        timestamps[aots] = [start_date, end_date]
        print("Time stamps:")
        for key, value in timestamps.items():
            print(f"{key}: {value}")
    else:
        print("Invalid time range. Start date must be before end date.")

# Call the work_times function
work_times()




# def work_hoursOLD():
#     temp=True
#     ev3.screen.clear()
#     amount = 0
#     aoi = 0
#     ev3.screen.print("how many time\nstamps do you want: ", amount)
#     while temp == True:
#         buttons = ev3.buttons.pressed()
#         wait(250)
#         for button in buttons:
#             button_str=str(button)
#             if button_str == "Button.UP":
#                 ev3.screen.clear()
#                 amount += 1
#                 ev3.screen.print("how many time\nstamps do you want: ", amount)
#             if button_str == "Button.DOWN":        
#                 if amount < 1:
#                     ev3.screen.clear()
#                     amount = 0
#                     ev3.screen.print("how many time\nstamps do you want: ", amount)
#                 else:
#                     ev3.screen.clear()
#                     amount -= 1
#                     ev3.screen.print("how many time\nstamps do you want: ", amount)
#             if button_str == "Button.CENTER":
#                 ev3.screen.clear()
#                 aoi= amount 
#                 ev3.screen.print("you chosse this amout\nof time stamps: ", amount)
#                 wait(500)
#                 temp= False
#     dates = {}
#     for t in range(aoi):
#         temp = True
#         year=[0,0,0,0]
#         ev3.screen.clear()
#         ev3.screen.print("chosse what year: ")
#         counter = 0
#         for i in year:
#             counter += 1
#             while temp == True:
#                 buttons = ev3.buttons.pressed()
#                 wait(250)
#                 for button in buttons:
#                     button_str=str(button)

#                     if button_str == "Button.UP":
#                         ev3.screen.clear()
#                         i+=1
#                         ev3.screen.print( counter ,"number of the year: " , i )
#                     if button_str == "Button.DOWN":  
#                         ev3.screen.clear()
#                         i-=1
#                         ev3.screen.print( counter ,"number of the year: " , i )
#                     if button_str == "Button.CENTER":
#                         ev3.screen.clear()
#                         ev3.screen.print( counter ,"number of the year: " , i )
#                         year[counter-1] = i
#         if year[0]==0:
#             year[0]=2
#         year_str = ''.join(map(str, year))
#         int_year = int(year_str)
#         temp = True
#         month=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what month: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print("the month: " , i )
#                 if button_str == "Button.DOWN":  
#                     if i<1:
#                         ev3.screen.clear()
#                         i=0
#                         ev3.screen.print( "the month: " , i )
#                     else:
#                         ev3.screen.clear()
#                         i-=1
#                         ev3.screen.print( "the month: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( "the month: " , i )
#                     month=i
#                     if month == 0 :
#                         month = 1
#         temp = True
#         day=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what day: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print("the day: " , i )
#                 if button_str == "Button.DOWN":  
#                     if i<1:
#                         ev3.screen.clear()
#                         i=0
#                         ev3.screen.print( "the day: " , i )
#                     else:
#                         ev3.screen.clear()
#                         i-=1
#                         ev3.screen.print( "the day: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( "the day: " , i )
#                     day=i
#                     if day ==0:
#                         day = 1
#         temp = True
#         start_hour=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what hour: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print( counter ,"number of \nthe start hour: " , i )
#                 if button_str == "Button.DOWN":  
#                     ev3.screen.clear()
#                     i-=1
#                     ev3.screen.print( counter ,"number of \nthe start hour: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( counter ,"number of \nthe start hour: " , i )
#                     start_hour = i
#         temp = True
#         start_min=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what min: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                 if button_str == "Button.DOWN":  
#                     ev3.screen.clear()
#                     i-=1
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                     start_min = i
#         temp = True
#         end_hour=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what end hour: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print( counter ,"number of \nthe end hour: " , i )
#                 if button_str == "Button.DOWN":  
#                     ev3.screen.clear()
#                     i-=1
#                     ev3.screen.print( counter ,"number of \nthe end hour: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( counter ,"number of \nthe start hour: " , i )
#                     end_hour = i
#         temp = True
#         end_min=0
#         ev3.screen.clear()
#         ev3.screen.print("chosse what min: ")
#         while temp == True:
#             buttons = ev3.buttons.pressed()
#             wait(250)
#             for button in buttons:
#                 button_str=str(button)
#                 if button_str == "Button.UP":
#                     ev3.screen.clear()
#                     i+=1
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                 if button_str == "Button.DOWN":  
#                     ev3.screen.clear()
#                     i-=1
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                 if button_str == "Button.CENTER":
#                     ev3.screen.clear()
#                     ev3.screen.print( counter ,"number of \nthe start min: " , i )
#                     end_min = i
#         startdate = datetime.datetime(int_year,month,day,start_hour,start_min)
#         enddate=datetime.datetime(int_year,month,day,end_hour,end_min)
#         now= datetime.datetime.now()
#         if startdate>enddate and enddate>now and startdate>=now:
#             dates[t]=[startdate,enddate]
#     print(dates)

work_hours()

# ## Checks if this is the running script, and not imported from somewhere!
# if __name__ == "__main__":
#     main()

