#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxClient, TextMailbox, BluetoothMailboxServer


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




#########################################
#            zone parameters            #
#########################################
RobotRegister = {
    'A' : 0,
    'B' : 19,  ## Accurate
    'C' : 15,
    'D' : 0,  
    'E' : 5,
    'F' : 0,
    'G' : 18
}

RobotIdentity = 'C'
 

zoneSort = {
    'pickup'     :   2,
    'Green'     :   1,
    'Blue'      :   0,
    'coms'      :  3
    }

zoneHeight = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}


errorMargin = RobotRegister[RobotIdentity]

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


#################################
#         Menu parameters      #
#################################
inMenu = [False]




#################################
#           Belt                #
#################################
beltRotation = ''
bReflectionMargin = 4



#################################
#       Stop and Emergency      #
#################################
Estop = [False]
restart = [False]



#################################
#     Communication parameter   #
#################################
collaborators = ['A', 'B', 'C', 'D']
collaborator = 'D'

# The server must be started before the client!
me = ['server']
# This is the name of the remote EV3 or PC we are connecting to.
SERVERID = 'ev3dev-' + collaborator
# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

messages = ['occupied', 'gift4u', 'feed', 'stop', 'emergency', 'free']
# 0 send nothing, 1 for occupied, 2 for gift4u, 3 feed, 4 stop, 5 free.
send = ['nothing']

# Coms thread.
thread2Alive = [False]



#################################
#           Work Time           #
#################################

tstamps = {}
ctime = []
stopwatch = StopWatch()
stopwatch.reset()
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
            for time in tstamps.items():
                print (time)





def stimes(tstamps):
    if len(ctime)!=0:
        itstime = [False]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Get the time passed in seconds since the last update
        secpast = stopwatch.time() // 1000

        # Calculate the new minutes, hours, and days
        ctime[4] += secpast // 60  # Add the minutes
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
        for i in tstamps:
            if tstamps[i][0][0]==ctime[0] and tstamps[i][0][1] == ctime[1] and tstamps[i][0][2] == ctime[2]:
                if ((tstamps[i][0][3] <= ctime[3] <= tstamps[i][1][3]) and (tstamps[i][0][4] <= ctime[4] <= tstamps[i][1][4])):
                    itstime[0]=True
                    return itstime[0], secpast , ctime
        itstime[0]=False
        return itstime[0], secpast, ctime

###################################hight########################
weHaveHeight = [0]
# wehaveheight = [False, packageheight]

