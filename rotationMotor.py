def main():
    def rotate(speed, speed_limit = 60, acceleration_limit = 120):
        smallGear = 12  #Tooths
        bigGear = 36   #Tooths
        multiplyAngle = (bigGear/smallGear)

        rotationMotor.control.limits(speed=speed, acceleration=acceleration_limit)
        # angle = 90 * multiplyAngle

        
        if pressureSense.pressed():
            print("Angle ", rotationMotor.angle())
            rotationMotor.reset_angle(0)
            rotationMotor.run_angle(speed,-90 * multiplyAngle)
            print("Changed Angle ", rotationMotor.angle())
            wait(4000)
        else:
            rotationMotor.run(60)



if __name__ == "__main__":
    main()