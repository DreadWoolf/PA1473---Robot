#!/usr/bin/env pybricks-micropython

# from Parameters import *
from Parameters import elevationMotor, clawMotor, Stop, Estop
# from Emergencystop import emergencyStop
from rotationMotor import rotateBase
# from Arm_and_Claw import armMovement, clawMovement


def emergencyStop(gotoZone:int, angletarget:int, duringCallibration = False):
    global Estop
    global restart

    while(Estop):
        elevationMotor.hold()
        clawMotor.hold()
        rotationMotor.hold()
        wait(1000)
        # if Estop == False:
        if restart:
            s.sys.exit()

    rotateBase(zoneLocation[gotoZone],80, duringCallibration)
    armMovement(angletarget, zoneHeight[gotoZone], 80, duringCallibration)
    clawMovement(False, calibrate= True)

def Pickup(angleTarget:int, openClawsFirst:bool = True, height:int = 0):
    # if height <= 0:
    clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)


def Place(angleTarget:int, openClawsFirst:bool = False):
    
    # If openFirst = True will open first.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)
    clawMovement(open= (openClawsFirst)) # If not open first will grip here.




def armMovement(angleTarget: int, height:int = 0, operatingSpeed = 60, calibrate:bool = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)
    global Estop


    if calibrate:
        # print("start arm angle " , elevationMotor.angle())
        elevationMotor.run_target(speed = 40, target_angle = angleTarget * multiplyAngle)
        return

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
    if Estop == True: emergencyStop()



def clawMovement(open:bool, calibrate:bool = False):
    global Estop
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if calibrate:
        # clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=None)
        clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=80)
        clawMotor.reset_angle(0)
        return


    if open:  # Open.
        # clawMotor.run_until_stalled(-40, then=Stop.BRAKE, duty_limit=None)
        clawMotor.run_angle(60 ,(60) * multiplyAngle)
    else:
        clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=80)
        # clawMotor.run_angle(60 ,(-60) * multiplyAngle)

    if Estop == True: emergencyStop()


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

