#!/usr/bin/env pybricks-micropython

from Parameters import *
# from Parameters import elevationMotor, clawMotor, Stop, Estop
# from Emergencystop import emergencyStop
# from rotationMotor import rotateBase


def emergencyStop(gotoZone:int, angletarget:int, duringCallibration = False):
    global Estop
    global restart
    print("test")
    while(Estop[0] == True):
        elevationMotor.hold()
        clawMotor.hold()
        rotationMotor.hold()
        print("Emergency stop works")
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



    rotateBase(zoneLocation[gotoZone], gotoZone, angletarget, calibrate = duringCallibration)
    armMovement(gotoZone, zoneHeight[gotoZone], angletarget, calibrate = duringCallibration)
    clawMovement(gotoZone, angleTarget= angletarget, open= False, calibrate= True)

def Pickup(goToZone, angleTarget:int, openClawsFirst:bool = True, height:int = 0):
    # if height <= 0:
    clawMovement(goToZone, angleTarget, open = openClawsFirst) # If openFirst = True will open here.
    armMovement(goToZone, angleTarget= angleTarget)
    clawMovement(goToZone, angleTarget, open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(goToZone, angleTarget= -angleTarget)


def Place(goToZone, angleTarget:int, openClawsFirst:bool = False):
    
    # If openFirst = True will open first.
    armMovement(goToZone, angleTarget= angleTarget)
    clawMovement(goToZone, angleTarget, open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(goToZone, angleTarget, angleTarget= -angleTarget)
    clawMovement(goToZone, angleTarget, open= (openClawsFirst)) # If not open first will grip here.




def armMovement(goToZone, angleTarget: int, height:int = 0, operatingSpeed = 60, calibrate:bool = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)
    global Estop

    print("Estop  ... ", Estop)

    if calibrate:
        # print("start arm angle " , elevationMotor.angle())
        elevationMotor.run_target(speed = 40, target_angle = angleTarget * multiplyAngle)
        # return
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
        # elevationMotor.run_angle(operatingSpeed,(angleTarget - height) * multiplyAngle)
        elevationMotor.run_target(operatingSpeed,(angleTarget - height) * multiplyAngle)
    # print("targeted arm angle " , elevationMotor.angle())

    # Check if the event is set
    # if Event.is_set():
    #     # Process the updated global variable
    #     print("Thread 2: Global variable (Estop):", Estop)
    #     # Clear the event
    #     Event.clear()
    test(goToZone, angleTarget, calibrate)
    

def test(goToZone, angleTarget, calibrate):
    print("Estop is: ", Estop[0])
    if Estop[0] == True:
        emergencyStop(goToZone, angleTarget, calibrate)
    return


def clawMovement(goToZone, angleTarget, open:bool, calibrate:bool = False):
    global Estop
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if calibrate:
        # clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=None)
        clawMotor.run_until_stalled(60, then=Stop.HOLD, duty_limit=30)
        if not Estop:
            clawMotor.reset_angle(0)
    else:
        if open:  # Open.
            # clawMotor.run_until_stalled(-40, then=Stop.BRAKE, duty_limit=None)
            clawMotor.run_angle(60 ,(60) * multiplyAngle)
        else:
            # clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=30)
            clawMotor.run_until_stalled(60, then=Stop.HOLD, duty_limit=30)
            # clawMotor.run_angle(60 ,(-60) * multiplyAngle)

    test(goToZone, angleTarget, calibrate)

    # if Estop[0] == True:
    #     emergencyStop(goToZone, angleTarget, calibrate)
    # if semaphore.acquire() or Estop == True:
    #     # Event.clear()
    #     emergencyStop(goToZone, angleTarget, calibrate)




def LocationZero(speed = 60):
    while not pressureSense.pressed():
        rotationMotor.run(speed)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, goToZone, armtarget, operatingSpeed = 60, speed_limit = 120, acceleration_limit = 120, calibrate = False, potentialCargo = False):
    global Estop
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    # print("angle = ", angle)

    if angle == 0 or calibrate == True:
        LocationZero()
        # print("\nGoing back")
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

