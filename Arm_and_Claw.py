# from Parameters import *
from Parameters import elevationMotor, clawMotor, Stop


def Pickup(angleTarget:int, openClawsFirst:bool, height:int = 0):
    # if height <= 0:
    clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)


def Place(angleTarget:int, openClawsFirst:bool):
    
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
    elevationMotor.run_angle(operatingSpeed,(angleTarget - height) * multiplyAngle)
    # print("targeted arm angle " , elevationMotor.angle())


def clawMovement(open:bool, calibrate:bool = False):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if calibrate:
        clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=None)
        return


    if open:  # Open.
        # clawMotor.run_until_stalled(-40, then=Stop.BRAKE, duty_limit=None)
        clawMotor.run_angle(60 ,(60) * multiplyAngle)
    else:
        clawMotor.run_until_stalled(60, then=Stop.BRAKE, duty_limit=None)
        # clawMotor.run_angle(60 ,(-60) * multiplyAngle)