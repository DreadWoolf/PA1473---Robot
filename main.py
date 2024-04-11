#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement, clawMovement
from rotationMotor import rotateBase
from colorAlgorithm import colorSort
from menu import menu

from threading import Thread
# import threading



# Create two threads for each task
thread1 = Thread()
thread2 = Thread()

Robotrun = True

def main():
    ev3.speaker.beep()

    times = 2  #10
    zoneAmount = 3
    potentialCargo = False
    periodTime = 4000 # 4s (4000)

    armStartAngle = 50#39  # 40
    
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

            if sortZone == 'Error' or sortZone == 'nothing':
                print("Sortzone ", sortZone)

                ## Will continue if found nothing, otherwise place the cargo.
                if sortZone == "nothing":
                    
                    ev3.speaker.beep()
                    wait(4)
                    ev3.speaker.beep()

                    ### print error on robot.
                    ev3.screen.print('Error "color" 404')
                    wait(1000)

                    ## Drop of again, if detected random color.
                    Place(angleTarget=-armStartAngle, openClawsFirst=False)

                    lastZone = location

            else:
                wait(100)
                ######################################
                ######################################
                ######################################
                # Make sure this works...
                if sortZone == lastZone:
                    ### Screen print 
                    ev3.screen.print(str(color) + " to: " + str(sortZone))
                else:
                    ev3.screen.print("Package at right location")
                    
                
                if sortZone == 0:
                    rotateBase(angle= zoneLocation[sortZone]) # Go to zone '0'.
                else:
                    # This might not work as intended... (if we want to go to the next zone for example)
                    rotateBase(angle = zoneLocation[sortZone] - zoneLocation[lastZone])
                # Uppdate the lastZone.
                Place(angleTarget= -armStartAngle, openClawsFirst= False)
                lastZone = sortZone  # 0
            
            potentialCargo = False

        elif location >= zoneAmount:  # + 1
            location = 0
            goToZone = 0
            lastZone = 0
            rotateBase(angle= 0)
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
            

            rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
            Pickup(angleTarget= -armStartAngle, openClawsFirst= True)

            lastZone = location

            # picked up package true or false.
            ######################################
            ######################################
            ######################################
            # Check if we have cargo!
            potentialCargo = True
        print("GoToZone = ", goToZone)

    # Go back to start, if arm is higher than ground level.
    armMovement(angleTarget= -armStartAngle)
    print("\n\nStopped!")


def stop_thread(thread):
    """Stoppa en tråd omedelbart."""
    import ctypes
    if not thread.is_alive():
        return

    # Identifiera operativsystemet
    if hasattr(ctypes, 'pthread_kill'):
        # För Unix-baserade system
        tid = thread.ident
        ctypes.pthread_kill(tid, 9)
    elif hasattr(ctypes, 'WinDLL'):
        # För Windows-system
        kernel32 = ctypes.WinDLL('kernel32')
        handle = thread._Thread__handle
        kernel32.TerminateThread(handle, 0)


def testThreading():
    global RobotRun
    global thread2
    global elevationMotor
    global clawMotor
    global rotationMotor

    for i in range(10):
        ev3.speaker.beep()
        wait(1200)
    

    
    ev3.speak("bröö") #xD
    # elevationMotor.stop()
    # clawMotor.stop()
    # rotationMotor.stop()

    # stop_thread(thread2)

    # stop_timer = threading.Timer(5, thread.cancel)
    # stop_timer.start()
    # wait(1000)
    # menu()
    # # for i in range(5):
    # #     # ev3.speaker.beep()
    # #     wait(1000)
    # #     # thread2
    RobotRun = False
    ev3.speaker.beep()
    print("trying to stop now.")

    # Motor.stop()
    return 0

def Calibrate(armStartAngle:int = 40):

    ev3.screen.print("Callibrate arm")
    if elevationMotor.angle() != armStartAngle:
        armMovement(armStartAngle, calibrate= True)

    ev3.screen.print("Callibrate claw")

    clawMovement(None, calibrate= True)

    ev3.screen.print("Callibrate rotation")
    rotateBase(angle= 0)
    ev3.screen.clear()
    return 0



## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # Create two threads for each task
    thread1 = Thread(target=testThreading)
    thread2 = Thread(target=main)

    # Start the threads
    thread1.start()
    thread2.start()



    # # Wait for both threads to finish
    # thread1.join()
    # thread2.join()

    print("Both tasks have started.")

    # main()