#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement, clawMovement, rotateBase
# from rotationMotor import rotateBase
from colorAlgorithm import colorSort
import sys as s
# from OImenu import menu

# from threading import Thread, Event
# import threading

from menu import menu, Emenu
# import Parameters as par
#czones , zonecords = menu()
zoneSort, zoneHeight = menu()
# par.zoneSort = czones
# par.zoneHeight = zonecords
# print(par.zoneSort)

# Create two threads for each task
thread1 = th.Thread()
thread2 = th.Thread()
# Event = th.Thread.Event()

Robotrun = True
stopRobot = False


def main():
    global Robotrun
    # Robotrun = True
    ev3.speaker.beep()
    

    #zoneSort['pick1'] = 2
    #zoneSort['Blue'] = 0
    #zoneSort['unSuported'] = 3

    print(zoneSort)



    times = 2  #10
    zoneAmount = 3
    cargo = False
    periodTime = 4000 # 4s (4000)

    armStartAngle = 40 #28 #38 #40 #39  # 40
    
    Calibrate(armStartAngle)
    
    run = 0
    location = 0 # Go to first 1.
    lastZone = 0
    goToZone = 0
    speed = 400
    
    running = True
    while running:
        

        if cargo and Estop[0] == False: #

            sortZone = 0
            wait(5)  #2
            sortZone, color = colorSort(zoneSort)
            print("Sortzone: ", sortZone)
            print("Color: ", color)
            clawAngle = clawMotor.angle()
            print("claw angle: ", clawAngle)

            if sortZone == 'Error' or sortZone == 'nothing':
                print("Sortzone ", sortZone)

                

                ## Will continue if found nothing, otherwise place the cargo.
                # if sortZone == "Error":
                cca = clawMotor.angle()
                if (((cca >= -5 ) and  (5 >= cca)) or (cca <= 5)):
                    tmp = zoneSort['unSuported']
                    print(cca)
                    rotateBase(zoneLocation[tmp], tmp, armStartAngle, speed)
                    Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
            else:
                
                wait(5)

                rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)

                ## Drop of again, if detected random color.
                Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                # lastZone = location
            
            cargo = False
                # lastZone = location
        else: 
            # goToZone = location
            pickupzone = zoneSort["pick1"]
            armMovement(goToZone, angleTarget= armStartAngle, operatingSpeed= speed/2) # make sure we are up.
            rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
            Pickup(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo)

        clawAngle = clawMotor.angle()
        if clawAngle <= -10:
            cargo = True
        elif clawAngle >= 0 - 4:
            cargo = False
            clawMotor.reset_angle(0)
            print("Reseted claw angle!")
    

        # if Robotrun == False:
        #     break
    # Go back to start, if arm is higher than ground level.
    # armMovement(angleTarget= -armStartAngle)
    armMovement(goToZone= goToZone,angleTarget= -armStartAngle)
    print("\n\nStopped!")



def testThreading():
    global RobotRun
    global stopRobot
    
    
    stopProcess = False
    wait(100)

    while True:
        buttons = ev3.buttons.pressed()
        wait(250) # 250
        for button in buttons:
            if str(button) == "Button.CENTER":
                ev3.speaker.beep()
                Estop[0] = True
                elevationMotor.hold()
                clawMotor.hold()
                rotationMotor.hold()
                wait(1000)
                stopProcess = True  # Sätt flaggan till True när knappen trycks
                break  # Avbryt loopen när knappen trycks

        while stopProcess:
            # buttons = ev3.buttons.pressed()

            Emenu()
            wait(2)

            stopProcess = Estop[0]  # Go out from loop if Estop[0] is set to False

            # for button in buttons:
            #     if str(button) == "Button.CENTER":
            #         ev3.speaker.beep()
            #         wait(1000)
            #         stopProcess = False  # Sätt flaggan till True när knappen trycks
            #         Estop[0] = False
            #         # thread2.start()

                    # break  # Avbryt loopen när knappen trycks
    return 0

# def btnCheck():
    

def Calibrate(armStartAngle:int = 40, speed = 60):

    # armMovement(0,1,calibrate=False)
    # elevationMotor.stop()
    # clawMotor.stop()
    # rotationMotor.stop()
    # wait(2000)

    ev3.screen.print("Callibrate arm")
    if elevationMotor.angle() != armStartAngle:
        armMovement(0, armStartAngle, calibrate= True)
        # if stopRobot:
        #     print("stop")
        #     s.sys.exit()

    ev3.screen.print("Callibrate claw")

    clawMovement(0 , armStartAngle, None, calibrate= True)
    # if stopRobot:
    #     print("stop")
    #     s.sys.exit()

    ev3.screen.print("Callibrate rotation")
    rotateBase(angle= 0, goToZone= 0, operatingSpeed= speed, armtarget= armStartAngle)
    
    ev3.screen.clear()
    return 0

def StopRobot(stopRobot):
    if stopRobot:
        print("stop")
        s.sys.exit()
    # return 0

## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # Create two threads for each task
    thread1 = th.Thread(target=testThreading)
    thread2 = th.Thread(target=main)

    # Start the threads
    thread1.start()
    thread2.start()



    # # Wait for both threads to finish
    # thread1.join()
    # thread2.join()

    print("Both tasks have started.")

    # main()