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
    'E' : 10,
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
    'green'     :   1,
    'blue'      :   2,
    'yellow'    :   3,
    # 'red':4,
    'pick2'     :   5
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
    1: 45 + errorMargin,
    2: 90 + errorMargin + 2,
    3: 180 + errorMargin + 3
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
    2: 0,
    3: 0
}


Estop = [False]
restart = [False]










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
