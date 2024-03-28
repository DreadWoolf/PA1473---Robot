from Parameters import rotationMotor, pressureSense

def LocationZero():
    while not pressureSense.pressed():
        rotationMotor.run(60)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, operatingSpeed = 60, speed_limit = 60, acceleration_limit = 120):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    print("angle = ", angle)

    if angle == 0:
        LocationZero()
        print("\nGoing back")
    else:
        print("...")
        rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)
