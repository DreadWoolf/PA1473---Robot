#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from movement import Place, Pickup, armMovement, clawMovement, rotateBase, Calibrate
from colorAlgorithm import colorSort
import sys as s
from coms import coms, distribute, Connect, sendMessage

from menu import menu, Emenu
zoneSort, zoneHeight = menu()
print(zoneSort)


# Create two threads for each task
thread1 = th.Thread()
thread2 = th.Thread()


Robotrun = True
stopRobot = False

def main():
    global zoneSort
    global zoneHeight
    global Robotrun
    # Robotrun = True
    ev3.speaker.beep()

    print(zoneSort)



    cargo = False
    periodTime = 4000 # 4s (4000)

    armStartAngle = 40 #28 #38 #40 #39  # 40
    packageHeight = 0
    mbox = ''

    comsExists = False
    beltExists = False
    
    Calibrate(armStartAngle)
    
    # run = 0
    # location = 0 # Go to first 1.
    # lastZone = 0
    goToZone = 0
    speed = 400
    
    # startup = False
    running = True
    while running:

        ev3.screen.clear()

        # Check if we have a height on one zone.
        if weHaveHeight[0] >= armStartAngle:
            packageHeight = weHaveHeight[0]
        else:
            packageHeight = armStartAngle
            

        
        ###############################
        #       start coms thread     #
        ###############################
        if  not thread2Alive[0] and ('coms' in zoneSort or 'belt' in zoneSort):
            if 'coms' in zoneSort:
                garbage = 'coms'
                comsExists = True

            if 'belt' in zoneSort:
                beltExists = True
                            

            # Wait for connection, before startup and then start communication Thread.
            mbox = Connect()
            wait(2)
            # Creates thread and declare the target.
            thread2 = th.Thread(target=coms, args=(mbox,))
            thread2Alive[0] = True
            thread2.start()


        # Aptempt to Turn of thread2, if zones is changed.
        elif thread2Alive[0] == True and not ('coms' in zoneSort or 'belt' in zoneSort):
            thread2Alive[0] = False
            comsExists= False
            beltExists= False
            wait(5)
            if thread2Alive:    thread2.join()
        
        # If thread2 is active, send appropiate messages to companion.
        elif comsExists: # and thread2Alive[0] == True:
            zoneMargin = 200
            check = zoneLocation[zoneSort['coms']]

            if send[0] != 'nothing' and rotationMotor.angle() >= check + zoneMargin and rotationMotor.angle() <= check - zoneMargin:
                send[0] = messages[5] # Free
                sendMessage(mbox)
                send[0] = 'nothing'
            # Make sure we are not blocking the coms zone, if no pickup exists.
            elif not 'pickup' in zoneSort:
                pickupzone = zoneSort['coms'] % (zoneSort['coms'] + 1)
                # Var armstartangle before
                armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2)
                rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed)
                # rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)






        # If we have cargo and is not stopped, execute this.
        if cargo and Estop[0] == False: #

            armMovement(pickupzone, angleTarget= armStartAngle,zoneHeight= zoneHeight, operatingspeed= speed/2) # make sure we are at sensor.

            sortZone = 0
            wait(5)  
            sortZone, color = colorSort(zoneSort)
            # make sure we are at free height.
            armMovement(pickupzone, angleTarget= packageHeight,zoneHeight= zoneHeight, operatingspeed= speed/2)



            # clawAngle = clawMotor.angle()

            if sortZone == 'Error' or sortZone == 'nothing':

                # print("Sortzone ", sortZone)

                

                ## Will continue if found nothing, otherwise place the cargo.
                # if sortZone == "Error":
                cAngle = clawMotor.angle()
                if (((cAngle >= -5 ) and  (5 >= cAngle)) or (cAngle <= 5)):
                    try:
                        sortZone = zoneSort[garbage]
                        # I THINK TRASH VARIABLE NEEDS ERRORHANDLING TOO!!!
                        # print(cAngle) 
                        # rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)
                        # Place(goToZone= sortZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                        rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)
                        Place(goToZone= sortZone, angleTarget=-armStartAngle,zoneHeight= zoneHeight , openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                    except NameError:
                        print("idk what to do!")
                        ev3.screen.print("color not supported")
                        running = False
                        #Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
            else:
                ev3.screen.print(str(color) + " to " + str(sortZone))
                
                # We sort to coms zone.
                if comsExists and sortZone == zoneSort['coms']:
                    do = True
                    while do:
                        if distribute[1]: # Collision warning
                            wait(500)
                        elif distribute[0]: # Other robot has already left a package.
                            ev3.screen.print("Error package \nalready there!")
                        else:
                            send[0] = messages[0] # 'occupied'
                            wait(2)
                            sendMessage(mbox) # Send the message
                            wait(10)
                            do = False


                wait(5)

                rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)

                ## Drop of again, if detected random color.
                Place(goToZone= sortZone, angleTarget=-armStartAngle, openClawsFirst=False, zoneHeight =zoneHeight , operatingspeed= speed/2, potentialCargo= cargo)
                # lastZone = location
            
            cargo = False
                # lastZone = location
        else:
            # If receevied = True and Occupied = False.
            if comsExists and distribute[0] == True and distribute[1] == False:
                pickupzone = zoneSort["coms"]
                ### Send info occupied
                send[0] = messages[0] # 'occupied'
                wait(2)
                sendMessage(mbox)
                wait(2)
                armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2) # make sure we are up.
                rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
                Pickup(goToZone= pickupzone, angleTarget= -armStartAngle, zoneHeight=zoneHeight, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo)

            else:
                if 'belt' in zoneSort:
                    pickupzone = zoneSort["belt"] 
                    # maybe higher
                    armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2)
                    rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed)
                    Pickup(goToZone= pickupzone,angleTarget= -armStartAngle, zoneHeight= zoneHeight, openClawsFirst= True, operatingspeed= speed/2, potentialCargo= cargo, belt= True, mbox= mbox)
                    # Pickup(goToZone= pickupzone, 
                    # have that claw always open


                else:
                    pickupzone = zoneSort["pickup"]

                    armMovement(pickupzone, angleTarget= packageHeight,zoneHeight=zoneHeight ,operatingspeed= speed/2) # make sure we are up.
                    rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
                    Pickup(goToZone= pickupzone, angleTarget= -armStartAngle, zoneHeight=zoneHeight, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo)

        # Make sure if we are holding cargo or not.
        clawAngle = clawMotor.angle()
        if clawAngle <= -10:
            cargo = True
        elif clawAngle >= 0 - 4:
            cargo = False
            # make sure the angle is correct.
            clawMotor.reset_angle(0)
            print("Reseted claw angle!")
            wait(500)
    

        # if Robotrun == False:
        #     break
    # Go back to start, if arm is higher than ground level.
    # armMovement(angleTarget= -armStartAngle)
    if stopRobot == True:
        armMovement(goToZone= goToZone,angleTarget= -armStartAngle)
    print("\n\nStopped!")



def EmergencyThread():
    global RobotRun
    global stopRobot
    global zoneSort
    global zoneHeight
    
    
    stopProcess = False
    wait(100)

    while True:
        buttons = ev3.buttons.pressed()
        wait(250) # 250
        if not inMenu[0]:
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

# def btnCheck():

# def collaborate():
#     coms()


# def belt():
#     margin = 20
#     # send[0] = 3
#     reflection = colorSense.reflection()

#     while reflection >= 0 + margin and reflection <= 100 - margin:
#         reflection = colorSense.reflection()
#         send[0] = 'feed'
#         # return False
    
#     send[0] = 'stop' # Send stop feeding
#     # return True




def StopRobot(stopRobot):
    if stopRobot:
        print("stop")
        s.sys.exit()
    # return 0

## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # Create two threads for each task
    thread1 = th.Thread(target=EmergencyThread)

    # thread2 = th.Thread(target=coms, args=mbox)

    # thread3 = th.Thread(target=belt)
    # thread3 = th.Thread(target=main, args=(thread2))


    # Start the threads
    thread1.start()
    # thread3.start()

    # Skicka tråd2 till main
    main()  #thread2)

    # # Wait for both threads to finish
    # thread1.join()
    # thread2.join()

    print(" tasks have started.")

    # main()