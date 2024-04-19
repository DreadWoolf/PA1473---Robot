from Parameters import rotationMotor, pressureSense, Estop
# from Arm_and_Claw import emergencyStop

def LocationZero(speed = 60):
    while not pressureSense.pressed():
        rotationMotor.run(speed)
    
    rotationMotor.reset_angle(0)


def rotateBase(angle, operatingSpeed = 60, speed_limit = 60, acceleration_limit = 120, callibrate = False):
    smallGear = 12  #Tooths for gear moving clockwise. 
    bigGear = 36   #Tooths for gear moving counter clockwise. 
    multiplyAngle = -(bigGear/smallGear)

    # print("angle = ", angle)

    if angle == 0 or callibrate == True:
        LocationZero()
        # print("\nGoing back")
    else:
        # rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)
        rotationMotor.run_target(operatingSpeed,(angle) * multiplyAngle)
    
    if Estop == True: emergencyStop()

        
