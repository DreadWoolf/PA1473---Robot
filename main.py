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

    rotate()









def rotate():

    rotationMotor.turn(20)
    return 0



    # wait(calibrationTime)

#     BackgroundRef = right_light.reflection() # Calibrate background reflection.
#     print("Background: ", BackgroundRef)
#     ev3.speaker.beep()
#     wait(calibrationTime)

#     tapeRef = right_light.reflection()  # Calibrate tape reflection.
#     print("Tape: ", tapeRef)
#     ev3.speaker.beep()


#     wait(calibrationTime)
#     ev3.speaker.beep()

#     threshold = (tapeRef + BackgroundRef) / 2

#     ## Auto calibrate proportional_gain.
#     PROPORTIONAL_GAIN = k * (BackgroundRef-tapeRef) + m
#     print("porportional gain: ", PROPORTIONAL_GAIN)


#     FindThePath(BackgroundRef, tapeRef)


#     while True:
#         ## If the line is lost, atempt to find it again.
#         if right_light.reflection() == 0 or left_light.reflection() == 0:
#             print("Lost the line!")
#             robot.stop()
#             FindThePath(BackgroundRef, tapeRef)

        
#         deviation = right_light.reflection() - threshold
#         speed = CruiseControl(speed, startspeed)
#         turn_rate = PROPORTIONAL_GAIN * deviation

#         ## uppdate the traveled distance.
#         distance =  robot.distance()


#         FoundPark = FindParking(BackgroundRef, threshold)

#         if FoundPark == True:
#             ## To overcome the tape.
#             if shouldpark == True and tmpDistance + 50 < distance:
#                     # Check if all the parkings is found, if not store if it's empty or not.
#                     if len(parkSpace) < parkAmount:
#                         tmpBool = checkParkEmpty()
#                         parkSpace.append(tmpBool)
#                         # Print the found parking and if it's empty or not with "true" or "False".
#                         ev3.screen.print("Park", len(parkSpace), tmpBool)
#                     else:
#                         ## first 0, second 1 with rest from modulu.
#                         if parkSpace[currentParking % parkAmount] == True:
#                             print(currentParking)
#                             # Check if we are on lap 2 or more.
#                             if currentParking >= parkAmount and currentParking % parkAmount == 0:
#                                 ev3.speaker.beep()

#                             park(parkDepth)
#                         else:
#                             ev3.speaker.beep()

#                         ev3.screen.print("Current park: " + str(parkSpace[currentParking % parkAmount]))
#                         currentParking += 1
#                         ev3.screen.print("Next park: " + str(parkSpace[currentParking % parkAmount]))

#                     shouldpark = False
#                     tmpDistance = 0
#             elif tmpDistance + 50 < distance:
#                     print("second park line")
#                     tmpDistance = distance
#                     shouldpark = True

#         if distance - tmpDistance > parklength:
#             tmpDistance = 0
#             shouldpark = False


#         robot.drive(speed, turn_rate)




# def CruiseControl(speed:int, startspeed:int):
#     ## Distances is in mm.
#     if distance_sensor.distance() < 80:
#         speed = 0
#         ev3.speaker.beep()
#     elif distance_sensor.distance() < 200 and speed > 0:
#         speed = speed - 0.1
#     elif distance_sensor.distance() > 200 and speed < startspeed:
#         speed = speed + 0.1

#     return speed


# def FindParking(background:int, threshold:int):
#     if left_light.reflection() < background - threshold:
#         return True
#     else:
#         return False


# def checkParkEmpty():
#     turnRight = 90
#     turnLeft = -90
#     robot.turn(turnLeft)
#     if distance_sensor.distance() < 200:
#         robot.turn(turnRight)
#         return False
#     robot.turn(turnRight)
#     return True
    


# def park(parkDepth:int):
#     parkTime = 5000 # 5s
#     turnLeft = -90

#     robot.turn(90)
#     robot.straight(-parkDepth)
#     wait(parkTime)

#     while distance_sensor.distance() < 100:
#         wait(10)
    
#     robot.straight(parkDepth)
#     robot.turn(turnLeft)



# def FindThePath(background:int, tape:int):
#     onTheLine = False
#     tempspeed = 0.0
#     while(onTheLine == False):
        
#         if left_light.reflection() == 0 or right_light.reflection() == 0 or distance_sensor.distance() < 100:
#             DcDrive(0,0)
#             print("Found obstacle")
#             robot.straight(-100)
#             robot.turn(180)
#             tempspeed = tempspeed/2
#             robot.stop()
#             wait(10)
#         elif right_light.reflection() > tape * 0.8 and right_light.reflection() < tape * 1.2: 
            
#             onTheLine = True
#             DcDrive(0,0)
#             print("Found the line!")

#         DcDrive(tempspeed, 40)

#         if tempspeed < 40:
#             tempspeed += 0.01  #0.001


# def DcDrive(left_pow:int, right_pow:int):
#     left_motor.dc(left_pow)
#     right_motor.dc(right_pow)


# def getReflection(light_reflection):
#     get_reflection = light_reflection
#     return get_reflection


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    main()

