#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement, clawMovement, rotateBase
# from rotationMotor import rotateBase
from colorAlgorithm import colorSort
import sys as s
# from menu import menu

# from threading import Thread, Event
# import threading

# from menu import menu
# import Parameters as par
# czones , zonecords = menu()
# par.zoneSort = czones
# par.zoneHeight = zonecords
# print(par.zoneSort)

# Create two threads for each task
thread1 = th.Thread()
thread2 = th.Thread()
# Event = th.Thread.Event()

Robotrun = True
stopRobot = False

# Event for synchronization
# event = th.Event()

def main():
    global Robotrun
    # Robotrun = True
    ev3.speaker.beep()

    times = 2  #10
    zoneAmount = 3
    potentialCargo = False
    periodTime = 4000 # 4s (4000)

    armStartAngle = 40#28 #38 #40 #39  # 40
    
    Calibrate(armStartAngle)
    
    run = 0
    location = 0 # Go to first 1.
    lastZone = 0
    goToZone = 0
    
    running = True
    while running: #run < times: # times = 2.
        # run += 1

        if potentialCargo:

            sortZone = 0
            wait(5)  #2
            sortZone, color = colorSort()
            print("Sortzone: ", sortZone)
            print("Color: ", color)

            if sortZone == 'Error' or sortZone == 'nothing':
                print("Sortzone ", sortZone)

                ## Will continue if found nothing, otherwise place the cargo.
                if sortZone == "Error":
                    
                    ev3.speaker.beep()
                    wait(4)
                    ev3.speaker.beep()

                    ### print error on robot.
                    ev3.screen.print('Error "color" 404')
                    wait(1000)

                    ## Drop of again, if detected random color.
                    Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False)
                    # lastZone = location

                lastZone = location
            else:
                wait(100)
                ######################################
                ######################################
                ######################################
                # Make sure this works...
                if sortZone == lastZone:
                    ### Screen print 
                    ev3.screen.print("Package at right location")
                else:
                    ev3.screen.print(str(color) + " to: " + str(sortZone))
                    
                
                if sortZone == 0:
                    rotateBase(angle= zoneLocation[sortZone], goToZone= sortZone, armtarget= armStartAngle) # Go to zone '0'.
                else:
                    # This might not work as intended... (if we want to go to the next zone for example)
                    # rotateBase(angle = zoneLocation[sortZone] - zoneLocation[lastZone])
                    rotateBase(angle = zoneLocation[sortZone], goToZone= sortZone, armtarget=armStartAngle)

                # Uppdate the lastZone.
                lastZone = sortZone  
                # Place(angleTarget= -armStartAngle, openClawsFirst= False)
                Place(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= False)
                # if stopRobot:
                #     print("stop")
                #     s.sys.exit()
            
            potentialCargo = False

        elif location >= zoneAmount:  # + 1
            location = 0
            goToZone = 0
            lastZone = 0
            rotateBase(angle= 0, goToZone=goToZone, armtarget= armStartAngle)
            # if stopRobot:
            #     print("stop")
            #     s.sys.exit()
            if RobotRun:
                print("\n\n Reset and sleep")
                wait(periodTime)  # 4000
                ev3.speaker.beep()
                run += 1
            else:
                running = False
        else:

            location += 1
            
            # May not work... maybe needs an 'or' or 'and' like gotozone <zoneamount.
            if location == lastZone: ## If we sorted to the zone we wanna go to.
                location += 1

            goToZone = location
            

            # rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
            rotateBase(zoneLocation[goToZone], goToZone, armStartAngle)

            # if stopRobot:
            #     print("stop")
            #     s.sys.exit()
            # Pickup(angleTarget= -armStartAngle, openClawsFirst= True)
            Pickup(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= True)
            # if stopRobot:
            #     print("stop")
            #     s.sys.exit()


            lastZone = location

            # picked up package true or false.
            ######################################
            ######################################
            ######################################
            # Check if we have cargo!
            potentialCargo = True
        print("GoToZone = ", goToZone)


        # if Robotrun == False:
        #     break
    # Go back to start, if arm is higher than ground level.
    # armMovement(angleTarget= -armStartAngle)
    armMovement(goToZone= goToZone,angleTarget= -armStartAngle)
    print("\n\nStopped!")



def testThreading():
    global RobotRun
    global stopRobot
    global Estop
    
    
    stopProcess = False

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
            buttons = ev3.buttons.pressed()

            
            # print("Estop: ", Estop[0])
            # elevationMotor.stop()
            # clawMotor.stop()
            # rotationMotor.stop()

            for button in buttons:
                if str(button) == "Button.CENTER":
                    ev3.speaker.beep()
                    wait(1000)
                    stopProcess = False  # Sätt flaggan till True när knappen trycks
                    Estop[0] = False
                    # thread2.start()

                    # break  # Avbryt loopen när knappen trycks
    return 0

# def btnCheck():
    

def Calibrate(armStartAngle:int = 40):
    # armMovement(0, armStartAngle, calibrate= True)

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
    rotateBase(angle= 0, goToZone= 0, armtarget= armStartAngle)
    
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