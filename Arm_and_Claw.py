# from Parameters import *
from Parameters import elevationMotor, clawMotor
# from Arm_and_Claw import *


def Pickup(angleTarget:int, openClawsFirst:bool, height:int = 0):
    # if height <= 0:
    clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)


def Place(angleTarget:int, openClawsFirst:bool):
    
    # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)



def armMovement(angleTarget: int, height:int = 0, operatingSpeed = 60):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)

    print("start arm angle " , elevationMotor.angle())
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
    print("targeted arm angle " , elevationMotor.angle())


def clawMovement(open:bool):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if open:
        clawMotor.run_angle(60 ,(60) * multiplyAngle)
    else:
        clawMotor.run_angle(60 ,(-60) * multiplyAngle)