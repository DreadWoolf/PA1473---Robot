# class Robot:
#     def __init__(self):
#         self.zone_colors = {}  # Dictionary to store zone-color mappings

#     def calibrate_zone_color(self, zone, color):
#         self.zone_colors[zone] = color
#         print(f"Zone {zone} calibrated with color {color}")

#     def pick_up_package(self, package):
#         color = self.detect_color(package)
#         for zone, zone_color in self.zone_colors.items():
#             if color == zone_color:
#                 print(f"Robot picked up package {package} from zone {zone}")
#                 return package
#         print("Package doesn't match any calibrated zone color. Ignoring.")

#     def move_to_zone(self, zone):
#         print(f"Robot moved to zone {zone}")

#     def drop_package(self, package, zone):
#         print(f"Robot dropped package {package} in zone {zone}")

#     def detect_color(self, package):
#         # Simulated color detection
#         return "Red"  # Replace with actual color detection logic


# # Example usage
# robot = Robot()

# # Calibrating zones with colors
# robot.calibrate_zone_color("Zone A", "Red")
# robot.calibrate_zone_color("Zone B", "Blue")

# # Picking up packages from zones and dropping them in target zones
# package1 = "Package with Red Color"
# picked_package = robot.pick_up_package(package1)
# if picked_package:
#     robot.move_to_zone("Zone A")
#     robot.drop_package(picked_package, "Zone A")

# package2 = "Package with Green Color"
# picked_package = robot.pick_up_package(package2)
# if picked_package:
#     robot.move_to_zone("Zone B")
#     robot.drop_package(picked_package, "Zone B")


# zones = {
#     1: 'Red',
#     2: 'blue'
# }

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
czones , zonecords = menu()
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
    #Zonesort, zoneHeight = menu()

    zoneSort['pick1'] = 2
    zoneSort['Blue'] = 0
    zoneSort['unSuported'] = 3

    print(zoneSort)


    ### Try to get the fucking arm to go down.
    # elevationMotor.dc(50)
    # wait(5)
    # elevationMotor.stop()


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
            # armMovement(goToZone, angleTarget= armStartAngle) # make sure we are up.

            sortZone = 0
            wait(5)  #2
            sortZone, color = colorSort()
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
                    Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, potentialCargo= cargo)
            else:
                
                wait(5)

                rotateBase(zoneLocation[sortZone], sortZone, armStartAngle, speed)

                ## Drop of again, if detected random color.
                Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, potentialCargo= cargo)
                # lastZone = location
            
            cargo = False
                # lastZone = location
        else: 
            # goToZone = location
            pickupzone = zoneSort["pick1"]
            armMovement(goToZone, angleTarget= armStartAngle) # make sure we are up.
            rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
            Pickup(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= True, potentialCargo= cargo)
            # cargo = True

        clawAngle = clawMotor.angle()
        if clawAngle <= -10:
            cargo = True
        elif clawAngle >= 0 - 4:
            cargo = False
            clawMotor.reset_angle(0)
            print("Reseted claw angle!")
    # running = True
    # while running: #run < times: # times = 2.
    #     # run += 1

    #     if potentialCargo:

    #         sortZone = 0
    #         wait(5)  #2
    #         sortZone, color = colorSort()
    #         print("Sortzone: ", sortZone)
    #         print("Color: ", color)

    #         if sortZone == 'Error' or sortZone == 'nothing':
    #             print("Sortzone ", sortZone)
    #         else:
    #             ev3.screen.print(str(color) + " to: " + str(sortZone))
                    
                
    #             if sortZone == 0:
    #                 rotateBase(angle= zoneLocation[sortZone], goToZone= sortZone,operatingSpeed= speed, armtarget= armStartAngle) # Go to zone '0'.
    #             else:
    #                 # This might not work as intended... (if we want to go to the next zone for example)
    #                 # rotateBase(angle = zoneLocation[sortZone] - zoneLocation[lastZone])
    #                 rotateBase(angle = zoneLocation[sortZone], goToZone= sortZone, operatingSpeed= speed, armtarget=armStartAngle)

    #             # Uppdate the lastZone.
    #             lastZone = sortZone  
    #             # Place(angleTarget= -armStartAngle, openClawsFirst= False)
    #             Place(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= False, potentialCargo= potentialCargo)
    #             # if stopRobot:
    #             #     print("stop")
    #             #     s.sys.exit()
            
    #         potentialCargo = False

    #     else:
    #         # goToZone = location
    #         pickupzone = zoneSort["pick1"]
    #         rotateBase(zoneLocation[pickupzone], pickupzone, armStartAngle, operatingSpeed= speed)
    #         Pickup(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= True, potentialCargo= potentialCargo)
    #         potentialCargo = True
            


        #     location += 1
            
        #     # May not work... maybe needs an 'or' or 'and' like gotozone <zoneamount.
        #     if location == lastZone: ## If we sorted to the zone we wanna go to.
        #         location += 1

        #     goToZone = location
            

        #     # rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
        #     rotateBase(zoneLocation[goToZone], goToZone, armStartAngle)

        #     # if stopRobot:
        #     #     print("stop")
        #     #     s.sys.exit()
        #     # Pickup(angleTarget= -armStartAngle, openClawsFirst= True)
        #     Pickup(goToZone= goToZone, angleTarget= -armStartAngle, openClawsFirst= True)
        #     # if stopRobot:
        #     #     print("stop")
        #     #     s.sys.exit()


        #     lastZone = location

        #     # picked up package true or false.
        #     ######################################
        #     ######################################
        #     ######################################
        #     # Check if we have cargo!
        #     potentialCargo = True
        # print("GoToZone = ", goToZone)


        # if Robotrun == False:
        #     break
    # Go back to start, if arm is higher than ground level.
    # armMovement(angleTarget= -armStartAngle)
    armMovement(goToZone= goToZone,angleTarget= -armStartAngle)
    print("\n\nStopped!")



def testThreading():
    global RobotRun
    global stopRobot
    # global Estop
    
    
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
            # if Estop[0] == False:
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