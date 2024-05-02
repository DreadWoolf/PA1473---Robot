#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from movement import Place, Pickup, armMovement, clawMovement, rotateBase, Calibrate
from colorAlgorithm import colorSort
import sys as s
from coms import coms, distribute

from menu import menu, Emenu
zoneSort, zoneHeight = menu()
print(zoneSort)

# if 'coms' in zoneSort:
#     garbage = 'coms'
# for key in zoneSort:
#     if key == 'coms':
#         garbage = 'coms'
        
# par.zoneSort = czones
# par.zoneHeight = zonecords
# print(par.zoneSort)

# Create two threads for each task
thread1 = th.Thread()
thread2 = th.Thread()
# thread3 = th.Thread()
# Event = th.Thread.Event()

Robotrun = True
stopRobot = False

def main(thread2:th.Thread):
    global zoneSort
    global zoneHeight
    global Robotrun
    # Robotrun = True
    ev3.speaker.beep()
    
    if 'coms' in zoneSort:
        garbage = 'coms'
        thread2.start()

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
                    try:
                        sortZone = zoneSort[garbage]
                        # I THINK TRASH VARIABLE NEEDS ERRORHANDLING TOO!!!
                        print(cca)
                        rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)
                        Place(goToZone= sortZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                    except NameError:
                        print("idk what to do!")
                        ev3.screen.print("color not supported")
                        running = False
                        #Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
            else:
                ev3.screen.print(str(color) + " to " + str(sortZone))
                
                wait(5)

                rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)

                ## Drop of again, if detected random color.
                Place(goToZone= sortZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                # lastZone = location
            
            cargo = False
                # lastZone = location
        else:
            if distribute[0] == True:
                pickupzone = zoneSort["coms"]
                ### Send info occupied
                send[0] = 0
            else:
                pickupzone = zoneSort["pickup"]
            # goToZone = location
            armMovement(pickupzone, angleTarget= armStartAngle, operatingspeed= speed/2) # make sure we are up.
            rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
            Pickup(goToZone= pickupzone, angleTarget= -armStartAngle, zoneHeight=zoneHeight, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo)

        clawAngle = clawMotor.angle()
        if clawAngle <= -10:
            cargo = True
        elif clawAngle >= 0 - 4:
            cargo = False
            clawMotor.reset_angle(0)
            print("Reseted claw angle!")
            wait(500)
    

        # if Robotrun == False:
        #     break
    # Go back to start, if arm is higher than ground level.
    # armMovement(angleTarget= -armStartAngle)
    armMovement(goToZone= goToZone,angleTarget= -armStartAngle)
    print("\n\nStopped!")



def testThreading():
    global RobotRun
    global stopRobot
    global zoneSort
    global zoneHeight
    
    
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

            zoneSort, zoneHeight = Emenu(zoneSort, zoneHeight)
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

def collaborate():
    coms()



def StopRobot(stopRobot):
    if stopRobot:
        print("stop")
        s.sys.exit()
    # return 0

## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # Create two threads for each task
    thread1 = th.Thread(target=testThreading)
    thread2 = th.Thread(target=collaborate)
    # thread3 = th.Thread(target=main, args=(thread2))


    # Start the threads
    thread1.start()
    # thread3.start()

    # Skicka tråd2 till main
    main(thread2)

    # # Wait for both threads to finish
    # thread1.join()
    # thread2.join()

    print(" tasks have started.")

    # main()