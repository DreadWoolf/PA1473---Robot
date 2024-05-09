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
    global mbox
    ev3.speaker.beep()

    print(zoneSort)



    cargo = False

    armStartAngle = 40  # This is preset to be at the sensor height.
    packageHeight = 0

    comsExists = False
    beltExists = False

    
    Calibrate(armStartAngle)
    
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
        if  thread2Alive[0] == False and ('coms' in zoneSort or 'belt' in zoneSort):
            print("Starting thread")
            if 'coms' in zoneSort:
                garbage = 'coms'
                comsExists = True
                notpickupzone = (zoneSort['coms'] + 1) % 3
                rotateBase(zoneLocation[notpickupzone], notpickupzone, packageHeight, operatingSpeed= speed, zoneHeight=zoneHeight)

            else:
                # garbage = None
                comsExists = False


            if 'belt' in zoneSort:
                beltExists = True
            else:
                beltExists = False
            
            # Wait for connection, before startup and then start communication Thread.
            mbox = Connect()
            wait(10)
            # Creates thread and declare the target.

            thread2 = th.Thread(target=coms, args=(mbox, ))
            thread2Alive[0] = True
            thread2.start()


        # Aptempt to Turn of thread2, if zones is changed.
        # elif thread2Alive[0] == True and not ('coms' in zoneSort or 'belt' in zoneSort):
        elif thread2Alive[0] == True and ('coms' not in zoneSort and 'belt' not in zoneSort):
            comsExists= False
            beltExists= False
            wait(5)
            if thread2Alive[0]:
                thread2.join()
                thread2Alive[0] = False

        



        # Make sure if we are holding cargo or not.
        clawAngle = clawMotor.angle()
        if clawAngle <= -10:
            cargo = True
        elif clawAngle >= 0 - 4:
            cargo = False
            # make sure the angle is correct.
            clawMotor.reset_angle(0)
            # print("Reseted claw angle!")
            wait(500)


        
        # If thread2 is active, send appropiate messages to companion.
        if comsExists and cargo == False: # and thread2Alive[0] == True:
            zoneMargin = 20
            check = zoneLocation[zoneSort['coms']]

            # Make sure we are not blocking the coms zone, if no pickup exists.
            if 'pickup' not in zoneSort:
                # Go away from coms zone, to not block.
                pickupzone = (zoneSort['coms'] + 1) % 3

                armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2)
                rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed, zoneHeight=zoneHeight)

            if send[0] == messages[0] and (rotationMotor.angle() >= check + zoneMargin or rotationMotor.angle() <= check - zoneMargin):
                send[0] = messages[5] # Free
                sendMessage(mbox)
                # send[0] = 'nothing'





        # If we have cargo and is not stopped, execute this.
        if cargo and Estop[0] == False: #
            # make sure we are at sensor height.
            armMovement(pickupzone, angleTarget= armStartAngle,zoneHeight= zoneHeight, operatingspeed= speed/2)

            sortZone = 0
            wait(5)  
            sortZone, color = colorSort(zoneSort)

            # make sure we are at free height.
            armMovement(pickupzone, angleTarget= packageHeight,zoneHeight= zoneHeight, operatingspeed= speed/2)




            if sortZone == 'Error' or sortZone == 'nothing':

                ## Will continue if found nothing, otherwise place the cargo.
                cAngle = clawMotor.angle()
                if (((cAngle >= -5 ) and  (5 >= cAngle)) or (cAngle <= 5)):
                    try:
                        # Sort this to our collaborator.
                        sortZone = zoneSort[garbage]
                        sort(sortZone, packageHeight, speed, cargo, comsExists, zoneHeight=zoneHeight)
                        rotAngle = rotationMotor.angle()
                        if  rotAngle <= zoneSort[garbage] + 20 and rotAngle <= zoneSort[garbage] - 20:
                            send[0] = messages[1] # Gift4u
                            sendMessage(mbox)
                        # rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed, zoneHeight=zoneHeight)
                        # Place(goToZone= sortZone, angleTarget=-armStartAngle,zoneHeight= zoneHeight, openClawsFirst=False, operatingspeed= speed/2, potentialCargo= cargo)
                    except NameError:
                        print("idk what to do!")
                        ev3.screen.print("color not supported")
                        running = False
            
            
            else:
                
                # Sort (go to right location etc)
                ev3.screen.print(str(color) + " to " + str(sortZone + 1))
                
                sort(sortZone, armStartAngle, speed, cargo, comsExists, zoneHeight=zoneHeight)
            
            cargo = False

        else: # HERE WE PICK UP STUFF!

            # If receevied = True and Occupied = False.
            if comsExists and distribute[0] == True and distribute[1] == False:
                pickupzone = zoneSort["coms"]
                ### Send info occupied
                send[0] = messages[0] # 'occupied'
                wait(2)
                sendMessage(mbox)
                wait(2)
                armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2) # make sure we are up.
                
                
                rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed, zoneHeight=zoneHeight)
                Pickup(goToZone= pickupzone, angleTarget= -armStartAngle, zoneHeight=zoneHeight, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo, belt=False)

            else: # when we have no collaborator or won't pick up at coms.

                if 'belt' in zoneSort:
                    pickupzone = zoneSort["belt"] 
                    # maybe higher
                    armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2)
                    rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed, zoneHeight=zoneHeight)
                    Pickup(goToZone= pickupzone,angleTarget= -armStartAngle, zoneHeight= zoneHeight, openClawsFirst= True, operatingspeed= speed/2, potentialCargo= cargo, belt= beltExists, mbox= mbox)


                elif 'pickup' in zoneSort:
                    pickupzone = zoneSort["pickup"]

                    armMovement(pickupzone, angleTarget= packageHeight, operatingspeed= speed/2) # make sure we are up.
                    rotateBase(zoneLocation[pickupzone], pickupzone, packageHeight, operatingSpeed= speed, zoneHeight=zoneHeight)
                    Pickup(goToZone= pickupzone, angleTarget= -armStartAngle, zoneHeight=zoneHeight, openClawsFirst= True,  operatingspeed= speed/2, potentialCargo= cargo)
                else:
                    print("Waiting for instructions")
                    wait(500)

    if stopRobot == True:
        armMovement(goToZone= goToZone,angleTarget= -armStartAngle, potentialCargo=True)
    print("\n\nStopped!")


# Our emergency thread, that will be running in the background and listen.
def EmergencyThread():
    global RobotRun
    global stopRobot
    global zoneSort
    global zoneHeight
    global mbox
    
    
    stopProcess = False
    wait(100)

    while True:
        buttons = ev3.buttons.pressed()
        wait(250) # 250
        # Make sure we are not in menue.
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
                    if mbox != '':
                        send[0] = messages[3]
                        sendMessage(mbox)
                    break  # Avbryt loopen när knappen trycks

            while stopProcess:

                zoneSort, zoneHeight = Emenu(zoneSort, zoneHeight)
                wait(2)

                stopProcess = Estop[0]  # Go out from loop if Estop[0] is set to False
                



def sort(sortZone, armStartAngle, speed, cargo, comsExists, zoneHeight= {}):
    global zoneSort
    

    # We sort to coms zone.
    if comsExists and sortZone == zoneSort['coms']:
        do = True
        while do:
            if distribute[1]: # Collision warning, wait for collaborator to finish.
                wait(500)
            elif distribute[0]: # Other robot has already left a package.
                ev3.screen.print("Error package \nalready there!")
                wait(2000)
            else:
                send[0] = messages[0] # set message to 'occupied'
                wait(2)
                sendMessage(mbox) # Send the message
                wait(10)
                do = False


    wait(5)

    rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed, zoneHeight=zoneHeight)

    ## Drop of again, if detected random color.
    Place(goToZone= sortZone, angleTarget=-armStartAngle, openClawsFirst=False, zoneHeight =zoneHeight, operatingspeed= speed/2, potentialCargo= cargo)
    distribute[0] = False  # Set receeved to false, we are done.

    return 0



def StopRobot(stopRobot):
    if stopRobot:
        print("stop")
        s.sys.exit()


## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # Create a thread for each task
    thread1 = th.Thread(target=EmergencyThread)


    # Start the Emergency thread.
    thread1.start()

    main()
