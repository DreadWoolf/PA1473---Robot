from Parameters import *


def Pickup(angleTarget:int, openClawsFirst:bool, height:int):
    # if height <= 0:
    clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)
    # else:
    #     clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    #     armMovement(angleTarget= angleTarget)

    # if openClawsFirst == False:
    #     clawMovement(open=(not openClawsFirst))


def Place(angleTarget:int, openClawsFirst:bool):
    
    # clawMovement(open = openClawsFirst) # If openFirst = True will open here.
    armMovement(angleTarget= angleTarget)
    clawMovement(open= (not openClawsFirst)) # If not open first will grip here.
    armMovement(angleTarget= -angleTarget)
    # if openClawsFirst == False:
    #     clawMovement(open=(not openClawsFirst))



def armMovement(angleTarget, operatingSpeed = 60):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)

    print("start arm angle " , elevationMotor.angle())
    elevationMotor.run_angle(operatingSpeed,angleTarget * multiplyAngle)
    print("targeted arm angle " , elevationMotor.angle())


def clawMovement(open:bool):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 16   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    if open:
        clawMotor.run_angle(60 ,(60) * multiplyAngle)
    # wait(4000)
    else:
        clawMotor.run_angle(60 ,(-60) * multiplyAngle)
    return 0