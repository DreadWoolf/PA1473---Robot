#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

# import datetime
import random
import sys as s
import threading as th
# from threading import Thread #, Event
#from threading import Thread, Event

# Lock for synchronization
# lock = th._thread.allocate_lock()

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

# robot = DriveBase(clawMotor, rotationMotor)

RobotRegister = {
    'A' : 0,
    'B' : 19,  ## Accurate
    'C' : 0,
    'D' : 0,  
    'E' : 5,
    'F' : 0,
    'G' : 18
}

RobotIdentity = 'E'
 

# zoneSort = {
#     0: 'DropOf',
#     1: 'Red',
#     2: 'Blue',
#     3: 'Yellow'
# }

zoneSort = {
    'pick1'     :   0,
    'Green'     :   1,
    'Yellow'    :   2,
    'Blue'      :   3,
    # 'red':4,
    'pick2'     :   4,
    'coms'      :   5,
    }


errorMargin = RobotRegister[RobotIdentity]

# zoneLocation = {
#     0: 0,
#     1: 90 + errorMargin,
#     2: 135 + errorMargin + 2,
#     3: 180 + errorMargin + 3
# }

# Depending on the installation of the robot, either "Right" or "Left".
# From Robots perspective.
oriontation = "Right"

rightOriented = {
    0: 0,
    1: 45 + errorMargin - 2, # 0
    2: 90 + errorMargin, #+ 2,
    3: 180 + errorMargin + 5#3
}

leftOriented = {
    0: 0,
    1: 90 + errorMargin,
    2: 135 + errorMargin + 2,
    3: 180 + errorMargin + 3
}

if oriontation == "Left":
    zoneLocation = leftOriented
elif oriontation == "Right":
    zoneLocation = rightOriented
else:
    print("Error, with setup")
    exit()


zoneHeight = {
    0: 0,
    1: 0,
    2: 20,
    3: 0
}


Estop = [False]
restart = [False]




tstamps = {}
ctime = []


def wtii(ctime, tstamps):
    stopwatch = StopWatch()
    temp=True
    if (len(ctime) != 0) and (len(tstamps)!=0):    
        # Define the number of days in each month
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while temp:
            # Get the time passed in seconds since the last update
            Timepast = stopwatch.time() // 1000

            # Calculate the new minutes, hours, and days
            ctime[4] += Timepast // 60  # Add the minutes
            if  Timepast // 60 == 1:   
                stopwatch.reset()
            ctime[3] += ctime[4] // 60  # Add the hours
            ctime[2] += ctime[3] // 24  # Add the days

            # Reset the minutes, hours, and days if they exceed their limits
            ctime[4] %= 60
            ctime[3] %= 24

            # Check if it's a leap year
            if ctime[0] % 4 == 0 and (ctime[0] % 100 != 0 or ctime[0] % 400 == 0):
                month_days[1] = 29
            else:
                month_days[1] = 28

            # Update the month and year if the days exceed their limit
            if ctime[2] > month_days[ctime[1] - 1]:
                ctime[2] -= month_days[ctime[1] - 1]  # Subtract the number of days in the current month
                ctime[1] += 1  # Increment the month
                if ctime[1] > 12:  # If the month exceeds 12, increment the year and reset the month to 1
                    ctime[1] = 1
                    ctime[0] += 1

            print(ctime)




# from threading import Thread
# import time

# def task1():
#     for i in range(5):
#         ev3.speak.beep()
#         time.sleep(1)

# def task2():
#     for i in range(5):
#         print("Task 2 executing...")
#         time.sleep(1)

# if __name__ == "__main__":
#     # Create two threads for each task
#     thread1 = Thread(target=task1)
#     thread2 = Thread(target=task2)

#     # Start the threads
#     thread1.start()
#     thread2.start()

#     # Wait for both threads to finish
#     thread1.join()
#     thread2.join()

#     print("Both tasks are completed.")
