#!/usr/bin/env pybricks-micropython

from Parameters import *
from colorAlgorithm import colorSort
# from Parameters import elevationMotor, clawMotor, Stop, Estop
# from Emergencystop import emergencyStop
# from rotationMotor import rotateBase


def Calibrate(armStartAngle:int = 40, speed = 60):

    # armMovement(0,1,calibrate=False)
    # elevationMotor.stop()
    # clawMotor.stop()
    # rotationMotor.stop()
    # wait(2000)

    ev3.screen.print("Callibrate arm")
    if elevationMotor.angle() != armStartAngle:
        armMovement(0, armStartAngle, calibrate= True, )
        # if stopRobot:
        #     print("stop")
        #     s.sys.exit()

    ev3.screen.print("Callibrate claw")

    clawMovement(0 , armStartAngle, None, calibrate= True)
    # if stopRobot:
    #     print("stop")
    #     s.sys.exit()

    ev3.screen.print("Callibrate rotation")
    rotateBase(angle= 0, goToZone= 0, operatingSpeed= speed, armtarget= armStartAngle, calibrate= True)
    
    ev3.screen.clear()
    return 0

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

    clawAngle = clawMotor.angle()
    if duringCallibration:
        Calibrate()
    if clawAngle <= -10:
        ## Might not work since it is pick up... (but place wouldn't either)
        # Pickup(gotoZone,angletarget, openClawsFirst=False, potentialCargo= True)
        armMovement(gotoZone, angletarget, potentialCargo=True)
            
    

def Pickup(goToZone, angleTarget:int, openClawsFirst:bool = True, zoneHeight:dict = {}, operatingspeed = 100, potentialCargo= False):
    # if height <= 0:
    while not Estop[0]:
        clawMovement(goToZone, angleTarget, open = openClawsFirst, operatingspeed= operatingspeed) # If openFirst = True will open here.
        wait(2)
        if Estop[0]: break
        armMovement(goToZone, angleTarget= angleTarget, zoneHeight= zoneHeight, operatingspeed= operatingspeed, pickingup = True)
        wait(2)
        if Estop[0]: break
        clawMovement(goToZone, angleTarget, open= (not openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        wait(2)
        if Estop[0]: break
        armMovement(goToZone, angleTarget= -angleTarget, operatingspeed= operatingspeed)
        wait(2)
        break


def Place(goToZone, angleTarget:int, openClawsFirst:bool = False, operatingspeed = 100, potentialCargo = True):
    
    # If openFirst = True will open first.
    while not Estop[0]:
        # armMovement(goToZone, angleTarget= -angleTarget) # make sure we are up.
        # if Estop[0]: break
        wait(2)
        armMovement(goToZone, angleTarget= angleTarget, operatingspeed= operatingspeed, potentialCargo = potentialCargo)
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget, open= (not openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        if Estop[0]: break
        wait(2)

        armMovement(goToZone, angleTarget= -angleTarget, operatingspeed= operatingspeed, potentialCargo = not potentialCargo)
        # ev3.speaker.beep()
        # wait(500)
        # ev3.speaker.beep()
        if Estop[0]: break
        wait(2)
        clawMovement(goToZone, angleTarget, open= (openClawsFirst), operatingspeed= operatingspeed) # If not open first will grip here.
        wait(2)
        break




def armMovement(goToZone, angleTarget: int, zoneHeight:dict = {}, operatingspeed = 100, calibrate:bool = False, potentialCargo = False, pickingup = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)
    # global Estop

    # print("Estop  ... ", Estop)
    # height = zoneHeight[goToZone]
    print("in armmovement")
    print(zoneHeight)
    print("gotozone ", goToZone)
    print("angletarget ", angleTarget)
    print("")
    # print("Fucking Height is: ", height)
    # print("angletarget is: ", angleTarget)
    # test = (abs(angleTarget) - height)
    # print("Test is: ", test)
    # testpositive = abs(test)
    # tmp = (testpositive) 
    # print("tmp is: ", tmp)
    # print("angle for motor: ", tmp * multiplyAngle)

    if calibrate:
        # print("start arm angle " , elevationMotor.angle())
        elevationMotor.run_target(operatingspeed, target_angle = angleTarget * multiplyAngle)
        # return
    elif potentialCargo and angleTarget <= 40 * multiplyAngle - 5 and angleTarget >= 40 * multiplyAngle + 5:
        elevationMotor.run_until_stalled(operatingspeed, then=Stop.HOLD, duty_limit=10) #20
        # elevationMotor.run_stall(operatingSpeed,(angleTarget - height) * multiplyAngle)
    elif pickingup == True:
        height = zoneHeight[goToZone]/multiplyAngle
        # print(zoneHeight)
        # print("Fucking Height is: ", height)
        # print("angletarget is: ", angleTarget)
        # test = (abs(angleTarget) - (height))
        # print("Test is: ", test)
        # testpositive = abs(test)
        # tmp = (testpositive) 
        # print("tmp is: ", tmp)
        # print("angle for motor: ", tmp * multiplyAngle)
        
        # elevationMotor.run_target(operatingspeed,(angleTarget - height) * multiplyAngle)
        elevationMotor.run_target(operatingspeed,(height) * multiplyAngle)
    else:
        # elevationMotor.run_target(operatingspeed,(angleTarget - height) * multiplyAngle)
        elevationMotor.run_target(operatingspeed,(angleTarget) * multiplyAngle)
    # print("targeted arm angle " , elevationMotor.angle())

    # Check if the event is set
    # if Event.is_set():
    #     # Process the updated global variable
    #     print("Thread 2: Global variable (Estop):", Estop)
    #     # Clear the event
    #     Event.clear()
    testForEmergency(goToZone, angleTarget, calibrate)
    

def testForEmergency(goToZone, angleTarget, calibrate, potentialCargo = False):
    # print("Estop is: ", Estop[0])
    if Estop[0] == True:
        emergencyStop(goToZone, angleTarget, calibrate, potentialCargo)
    return


def clawMovement(goToZone, angleTarget, open:bool, calibrate:bool = False, operatingspeed = 120): #100 before
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

    testForEmergency(goToZone, angleTarget, calibrate, potentialCargo = False)

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

    testForEmergency(goToZone, armtarget, calibrate)
    # if Estop[0] == True:
    #     emergencyStop(goToZone, armtarget, calibrate)
    # if semaphore.acquire() or Estop == True:
    # # if Estop == True:
    #     emergencyStop(goToZone, armtarget, calibrate)
    #     print("Estop, ", Estop)


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

