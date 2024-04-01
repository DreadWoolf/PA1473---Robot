#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement
from rotationMotor import rotateBase
from colorAlgorithm import colorSort

def main():
    ev3.speaker.beep()

    times = 5
    zoneAmount = 3
    cargo = False
    
    Calibrate()
    
    run = 0
    location = 1
    lastZone = 0
    # for i in range(times):
    while run < times:
        run += 1

        goToZone = location


        if cargo:
            sortZone = 0
            ######################################
            ######################################
            ######################################
            #       sortZone = Sort algorithm()
            sortZone = colorSort()

            if sortZone == 'Error':
                print("Error for sortZone!")
                # Does this exist?!
                ev3.speaker.error()

                ev3.speaker.beep()
                wait(2)
                ev3.speaker.beep()

            else:
                ######################################
                ######################################
                ######################################
                # Make sure this works...
                if sortZone == 0:
                    rotateBase(angle= zoneLocation[sortZone])
                else:
                    # This might not work as intended... (if we want to go to the next zone for example)
                    rotateBase(angle = zoneLocation[sortZone] - zoneLocation[lastZone])
                lastZone = sortZone  # 0
            
            Place(angleTarget= -35, openClawsFirst= False)
            cargo = False

        else:
            rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
            Pickup(angleTarget= -35, openClawsFirst= True)

            # picked up package true or false.
            ######################################
            ######################################
            ######################################
            # Check if we have cargo!
            cargo = True

            # print("Open claws")
            # clawMovement(open = True)
            # armMovement(angleTarget= -35)

            # print("Grip")
            # clawMovement(open = False)
            # armMovement(angleTarget= 35)

        print("Check color \nWhere to next= ", location)
        cargo = False

        
        

        # if cargo:
            
        #     # goToZone = 0
        #     # cargo = False
        #     # Go to drop of.
        # else:


        if location >= zoneAmount:
            location = 0
            goToZone = 0
        else:
            lastZone = location
            location += 1
            goToZone = location
            if location >= zoneAmount + 1:
                location = 0
                # LocationZero()
                rotateBase(angle= 0)
                wait(1000)
                ev3.speaker.beep()
        
        
        ######################################
        ######################################
        ######################################
        # Testing placment (problem since the code above is increasing before this)
        if location == 2 + 1:
            cargo = True
            print("loc is True")
                    

        

        print("GoToZone = ", goToZone)
        # goToZone = 0

        # rotateBase(angle=zoneLocation[goToZone])
        # # zone0Calibration()

        # armMovement(angleTarget= -35)
        # print("Let go")
        # clawMovement(open = True)
        # armMovement(angleTarget= 35)
        # print("Close the empty claws")
        # clawMovement(open = False)
        # # rotateBase(operatingSpeed= 60, angle = zoneLocation[0])

    # Go back to start, if arm is higher than ground level.
    armMovement(angleTarget= -35)


def Calibrate():
    # LocationZero()

    print("Calibrate arm")
    print("Calibrate claw\n\n")

    rotateBase(angle= 0)
    return 0


# def LocationZero():
#     while not pressureSense.pressed():
#         rotationMotor.run(60)
    
#     rotationMotor.reset_angle(0)


# def rotateBase(angle, operatingSpeed = 60, speed_limit = 60, acceleration_limit = 120):
#     smallGear = 12  #Tooths for gear moving clockwise. 
#     bigGear = 36   #Tooths for gear moving counter clockwise. 
#     multiplyAngle = -(bigGear/smallGear)

#     print("angle = ", angle)

#     if angle == 0:
#         LocationZero()
#         print("\nGoing back")
#     else:
#         print("...")
#         rotationMotor.run_angle(operatingSpeed,(angle) * multiplyAngle)



## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    armMovement(angleTarget= 35)
    # for i in range(3):
    # clawMovement(False)
    main()