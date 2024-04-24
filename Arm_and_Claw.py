#!/usr/bin/env pybricks-micropython

from Parameters import *
from colorAlgorithm import colorSort
# from Parameters import elevationMotor, clawMotor, Stop, Estop
# from Emergencystop import emergencyStop
# from rotationMotor import rotateBase


def emergencyStop(gotoZone:int, angletarget:int, duringCallibration = False, potentialCargo = False):
    global Estop
    global restart
    print("Emergency stop works")
    print("angle", clawMotor.angle())
    while(Estop[0] == True):
        elevationMotor.hold()
        clawMotor.hold()
        rotationMotor.hold()
        wait(1000)
        # if Estop == False:
        # if restart:
        #     s.sys.exit()
    print("gotozone ", gotoZone)
    print("angletarget ", angletarget)
    print("callibrate ", duringCallibration)
    
    #########################################
    #   Make checks for current position    #
    #########################################

    # if potentialCargo == True:
    
    if clawMotor.angle() > 0 + 8 and clawMotor.angle() < 0 - 8:
        print("Holding something")
        clawMovement(gotoZone, angleTarget= angletarget, open= False, calibrate= True)
        ## Cargo.
        sort(gotoZone, angletarget, duringCallibration = False, potentialCargo = False)
        ev3.speaker.beep()
        wait(5)
        ev3.speaker.beep()
        wait(5)
        ev3.speaker.beep()
        # clawMotor.angle()
    else:
        armMovement(gotoZone, zoneHeight[gotoZone], angletarget, calibrate = duringCallibration)
        rotateBase(zoneLocation[gotoZone], gotoZone, angletarget, calibrate = duringCallibration)
                
    # if 


def sort(gotoZone:int, angletarget:int, duringCallibration = False, potentialCargo = False):
    sortZone = 0
    armMovement(gotoZone, zoneHeight[gotoZone], 40, calibrate = duringCallibration)
    wait(5)  #2
    sortZone, color = colorSort()
    print("Sortzone: ", sortZone)
    print("Color: ", color)

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
            Place(goToZone= gotoZone, angleTarget=-angletarget, openClawsFirst=False)
            # lastZone = location


def Pickup(goToZone, angleTarget:int, openClawsFirst:bool = True, height:int = 0, potentialCargo= False):
    # if height <= 0:
    while not Estop[0]:
        clawMovement(goToZone, angleTarget, open = openClawsFirst) # If openFirst = True will open here.
        wait(2)
        if Estop[0]: break
        armMovement(goToZone, angleTarget= angleTarget)
        wait(2)
        if Estop[0]: break
        clawMovement(goToZone, angleTarget, open= (not openClawsFirst)) # If not open first will grip here.
        if Estop[0]: break
        wait(2)
        armMovement(goToZone, angleTarget= -angleTarget)
        break


def Place(goToZone, angleTarget:int, openClawsFirst:bool = False, potentialCargo = True):
    
    # If openFirst = True will open first.
    while not Estop[0]:
        armMovement(goToZone, angleTarget= angleTarget, potentialCargo = potentialCargo)
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget, open= (not openClawsFirst)) # If not open first will grip here.
        if Estop[0]: break
        wait(2)
        armMovement(goToZone, angleTarget= -angleTarget, potentialCargo = potentialCargo)
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget, open= (openClawsFirst)) # If not open first will grip here.
        break




def armMovement(goToZone, angleTarget: int, height:int = 0, operatingSpeed = 120, calibrate:bool = False, potentialCargo = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)
    # global Estop

    # print("Estop  ... ", Estop)

    if calibrate:
        # print("start arm angle " , elevationMotor.angle())
        elevationMotor.run_target(speed = 60, target_angle = angleTarget * multiplyAngle)
        # return
    elif potentialCargo:
        elevationMotor.run_until_stalled(operatingSpeed, then=Stop.HOLD, duty_limit=20)
        # elevationMotor.run_stall(operatingSpeed,(angleTarget - height) * multiplyAngle)
    else:
        ######################################
        ######################################
        ######################################
        #           Här @subhi               #
        # Bör dock vara klart för hantering om vilken höjd.
        #           (angleTarget - height)   #
        ######################################
        ######################################
        ######################################
        
        elevationMotor.run_target(operatingSpeed,(angleTarget - height) * multiplyAngle)
    # print("targeted arm angle " , elevationMotor.angle())

    # Check if the event is set
    # if Event.is_set():
    #     # Process the updated global variable
    #     print("Thread 2: Global variable (Estop):", Estop)
    #     # Clear the event
    #     Event.clear()
    test(goToZone, angleTarget, calibrate)
    

def test(goToZone, angleTarget, calibrate, potentialCargo = False):
    # print("Estop is: ", Estop[0])
    if Estop[0] == True:
        emergencyStop(goToZone, angleTarget, calibrate, potentialCargo)
    return


def clawMovement(goToZone, angleTarget, open:bool, calibrate:bool = False, operatingspeed = 100):
    # global Estop
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if calibrate:
        clawMotor.run_until_stalled(operatingspeed, then=Stop.HOLD, duty_limit=50)
        if not Estop[0]:
            clawMotor.reset_angle(0)
    else:
        if open:  # Open.
            clawMotor.run_angle(operatingspeed ,(60) * multiplyAngle)
        else:
            clawMotor.run_until_stalled(operatingspeed, then=Stop.HOLD, duty_limit=50)

    test(goToZone, angleTarget, calibrate, potentialCargo = False)

    # if Estop[0] == True:
    #     emergencyStop(goToZone, angleTarget, calibrate)
    # if semaphore.acquire() or Estop == True:
    #     # Event.clear()
    #     emergencyStop(goToZone, angleTarget, calibrate)




def LocationZero(speed = 60):
    while Estop[0] == False and not pressureSense.pressed():
        rotationMotor.run(speed)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, goToZone, armtarget, operatingSpeed = 60, speed_limit = 120, acceleration_limit = 120, calibrate = False, potentialCargo = False):
    # global Estop
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    # print("angle = ", angle)

    if angle == 0 or calibrate == True:
        LocationZero(operatingSpeed)
    else:
        # rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)
        rotationMotor.run_target(operatingSpeed,(angle) * multiplyAngle)
    
    # test(goToZone, armtarget, calibrate)

    test(goToZone, armtarget, calibrate)
    # if Estop[0] == True:
    #     emergencyStop(goToZone, armtarget, calibrate)
    # if semaphore.acquire() or Estop == True:
    # # if Estop == True:
    #     emergencyStop(goToZone, armtarget, calibrate)
    #     print("Estop, ", Estop)


if __name__ == "__main__":
    angletrget = 40
    print("Calibrate")
    armMovement(angletrget, calibrate=True)
    clawMovement(True, calibrate=True)  # Calibrate
    
    print("Pickup")
    Pickup(-angletrget)
    print("Place")
    Place(-angletrget)
    
    print("Stopping")
    armMovement(-angletrget)

