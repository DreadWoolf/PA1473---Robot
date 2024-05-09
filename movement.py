#!/usr/bin/env pybricks-micropython

from Parameters import *
from colorAlgorithm import colorSort
from coms import sendMessage


def Calibrate(armStartAngle:int = 40, speed = 60):

    # Check if we have a height on one zone.
    if weHaveHeight[0] >= armStartAngle:
        packageHeight = weHaveHeight[0]
    else:
        packageHeight = armStartAngle


    ev3.screen.print("Callibrate arm")
    if elevationMotor.angle() != packageHeight:
        armMovement(0, packageHeight ,calibrate= True)

    ev3.screen.print("Callibrate claw")

    clawMovement(0 , packageHeight, None, calibrate= True)
    
    ev3.screen.print("Callibrate rotation")
    rotateBase(angle= 0, goToZone= 0, operatingSpeed= speed, armtarget= packageHeight, calibrate= True)
    
    ev3.screen.clear()

def emergencyStop(gotoZone:int, angletarget:int, duringCallibration = False, potentialCargo = False, zoneHeight :dict = {}):
    global Estop
    global restart

    while(Estop[0] == True):
        elevationMotor.hold()
        clawMotor.hold()
        rotationMotor.hold()
        wait(1000)
    
    # Some checks.
    # print("gotozone ", gotoZone)
    # print("angletarget ", angletarget)
    # print("callibrate ", duringCallibration)

    clawAngle = clawMotor.angle()
    if duringCallibration:
        Calibrate()
    if clawAngle <= -10:
        armMovement(gotoZone, angletarget, zoneHeight= zoneHeight, potentialCargo=True)
        
    
            
    

# This is for if we have belt, to send signals for feeding material.
def Belt(mbox):
    margin = bReflectionMargin
    reflection = colorSense.reflection()
    send[0] = messages[2]  # Feed
    
    wait(2)
    send[0] = messages[2]  # Feed
    wait(250)
    sendMessage(mbox) # send the message.

    # wait here untill we see a cargo in front of us.
    while colorSense.reflection() <= 0 + margin:
        reflection = colorSense.reflection()

    # smal wait, so the package is at the right position.
    wait(300)
    send[0] = messages[3] # Send stop feeding
    wait(10)
    sendMessage(mbox)
    wait(20)



# Pick up algorithm.
def Pickup(goToZone, angleTarget:int, openClawsFirst:bool = True, zoneHeight:dict = {}, operatingspeed = 100, potentialCargo= False, belt = False, mbox=''):
    # This is for emergency stop.
    while not Estop[0]:
        clawMovement(goToZone, angleTarget,zoneHeight= zoneHeight ,open = openClawsFirst, operatingspeed= operatingspeed) # If openFirst = True will open here.
        wait(2)
        if Estop[0]: break

        if belt == True:  # wait here if we have belt.
            print("belt in pickup")
            Belt(mbox)
        
        armMovement(goToZone, angleTarget= angleTarget, zoneHeight= zoneHeight, operatingspeed= operatingspeed, pickingup = True)
        wait(2)
        if Estop[0]: break
        clawMovement(goToZone, angleTarget,zoneHeight= zoneHeight, open= (not openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        wait(2)
        if Estop[0]: break
        armMovement(goToZone, angleTarget= -angleTarget,zoneHeight= zoneHeight, operatingspeed= operatingspeed)
        wait(2)
        break


# Place alogorithm.
def Place(goToZone, angleTarget:int, openClawsFirst:bool = False, zoneHeight:dict = {}, operatingspeed = 100, potentialCargo = True):
    
    # This is for emergency stop.
    while not Estop[0]:
        wait(2)
        armMovement(goToZone, angleTarget= angleTarget, zoneHeight= zoneHeight, operatingspeed= operatingspeed, potentialCargo = potentialCargo)
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget,zoneHeight= zoneHeight, open= (not openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        if Estop[0]: break
        wait(2)

        armMovement(goToZone, angleTarget= -angleTarget, zoneHeight= zoneHeight, operatingspeed= operatingspeed, potentialCargo = not potentialCargo)
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget,zoneHeight= zoneHeight, open= (openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        wait(2)
        break




def armMovement(goToZone, angleTarget: int, zoneHeight:dict = {}, operatingspeed = 100, calibrate:bool = False, potentialCargo = False, pickingup = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)

    
    # Check so we don't divide by zero and so we have the actual height of the zone.
    if len(zoneHeight) > 0 and zoneHeight[goToZone] != 0:
        height = zoneHeight[goToZone]/multiplyAngle
    else:
        height = 0

    # During callibration.
    if calibrate:
        elevationMotor.run_target(operatingspeed, target_angle = angleTarget * multiplyAngle)
    
    elif potentialCargo and angleTarget <= 40 * multiplyAngle - 5 and angleTarget >= 40 * multiplyAngle + 5 and height == 0:
        elevationMotor.run_until_stalled(operatingspeed, then=Stop.HOLD, duty_limit=10) #20
    
    elif height != 0 and (pickingup == True or potentialCargo == True or not (abs(elevationMotor.angle()) >= abs(height) + 10 and abs(elevationMotor.angle()) >= abs(height) - 10)):
        elevationMotor.run_target(operatingspeed,(height) * multiplyAngle)
    else:
        elevationMotor.run_target(operatingspeed,(angleTarget) * multiplyAngle)


    
    if Estop[0] == True:  emergencyStop(goToZone, angleTarget, calibrate, potentialCargo, zoneHeight=zoneHeight)
    


def clawMovement(goToZone, angleTarget, open:bool, zoneHeight:dict = {}, calibrate:bool = False, operatingspeed = 120): #100 before
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


    if Estop[0] == True: emergencyStop(goToZone, angleTarget, calibrate, zoneHeight= zoneHeight)




def LocationZero(speed = 60):
    while Estop[0] == False and not pressureSense.pressed():
        rotationMotor.run(speed)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, goToZone, armtarget, operatingSpeed = 60, speed_limit = 120, acceleration_limit = 120, calibrate = False, potentialCargo = False, zoneHeight:dict = {}):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)


    if angle == 0 or calibrate == True:
        LocationZero(operatingSpeed)
    else:
        rotationMotor.run_target(operatingSpeed,(angle) * multiplyAngle)
    


    if Estop[0] == True: emergencyStop(goToZone, armtarget, calibrate, potentialCargo, zoneHeight= zoneHeight)



if __name__ == "__main__":
    armStartAngle = 50
    goToZone = 0
    potentialcargo = True
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)

    print("Calibrate")
        # rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)

    elevationMotor.run_angle(60, armStartAngle * multiplyAngle)
    elevationMotor.reset_angle(40 * multiplyAngle)

    print("do stuff")
    wait(2000)
    armMovement(2, armStartAngle)
    # armMovement(0, armStartAngle, calibrate=True)
    # clawMovement(0, armStartAngle, open= (False)) # If not open first will grip here.
    # clawMovement(0, armStartAngle, open= (True)) # If not open first will grip here.

    # clawMovement(True, calibrate=True)  # Calibrate
    # Place(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, potentialCargo= potentialcargo)

    # Pickup(goToZone= goToZone, angleTarget=-armStartAngle, openClawsFirst=False, potentialCargo= potentialcargo)

    # print("Pickup")
    # Pickup(-angletrget)
    # print("Place")
    # Place(-angletrget)
    
    # print("Stopping")
    # armMovement(-angletrget)

