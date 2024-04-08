#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement, clawMovement
from rotationMotor import rotateBase
from colorAlgorithm import colorSort

def main():
    ev3.speaker.beep()

    times = 7
    zoneAmount = 3
    potentialCargo = False
    periodTime = 4000 # 4s (4000)

    armStartAngle = 39  # 40
    
    Calibrate(armStartAngle)
    
    run = 0
    location = 0 # Go to first 1.
    lastZone = 0
    goToZone = 0
    
    while run < times: # times = 2.
        run += 1

        # goToZone = location

        # if location >= zoneAmount:  # + 1
        #         print("\n\n Reset and sleep")
        #         location = 0
        #         goToZone = 0
        #         # LocationZero()
        #         rotateBase(angle= 0)
        #         wait(periodTime)  # 4000
        #         ev3.speaker.beep()

        if potentialCargo:

            sortZone = 0
            wait(2)
            sortZone, color = colorSort()

            if sortZone == 'Error' or sortZone == 'nothing':
                print("Sortzone ", sortZone)

                ## Will continue if found nothing, otherwise place the cargo.
                if sortZone == "nothing":
                    
                    ev3.speaker.beep()
                    wait(4)
                    ev3.speaker.beep()

                    ### print error on robot.
                    ev3.screen.print('Error "color" 404')
                    wait(1000)

                    ## Drop of again, if detected random color.
                    Place(angleTarget=-armStartAngle, openClawsFirst=False)

                    lastZone = location

            else:
                ### Screen print 
                ev3.screen.print(str(color) + " to: " + str(sortZone))
                wait(100)
                ######################################
                ######################################
                ######################################
                # Make sure this works...
                if sortZone == 0:
                    rotateBase(angle= zoneLocation[sortZone]) # Go to zone '0'.
                else:
                    # This might not work as intended... (if we want to go to the next zone for example)
                    rotateBase(angle = zoneLocation[sortZone] - zoneLocation[lastZone])
                # Uppdate the lastZone.
                Place(angleTarget= -armStartAngle, openClawsFirst= False)
                lastZone = sortZone  # 0
            
            potentialCargo = False

        elif location >= zoneAmount:  # + 1
                print("\n\n Reset and sleep")
                location = 0
                goToZone = 0
                # LocationZero()
                rotateBase(angle= 0)
                wait(periodTime)  # 4000
                ev3.speaker.beep()
        else:
            

            # lastZone = location
            # location += 1
            # if location >= zoneAmount:
            #     location = 0
            #     goToZone = 0
            # else:

            # lastZone = location
            location += 1

            if location == lastZone: ## If we sorted to the zone we wanna go to.
                location += 1

            goToZone = location
            # if location >= zoneAmount + 1:  # + 1
            #     print("\n\n Reset and sleep")
            #     location = 0
            #     goToZone = 0
            #     # LocationZero()
            #     rotateBase(angle= 0)
            #     wait(periodTime)  # 4000
            #     ev3.speaker.beep()
            

            rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
            Pickup(angleTarget= -armStartAngle, openClawsFirst= True)

            lastZone = location

            # picked up package true or false.
            ######################################
            ######################################
            ######################################
            # Check if we have cargo!
            potentialCargo = True

        # print("Check color \nWhere to next= ", location)


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
    armMovement(angleTarget= -armStartAngle)
    print("\n\nStopped!")


def Calibrate(armStartAngle:int = 40):
    # LocationZero()

    print("Calibrate arm")
    # print(elevationMotor.angle())
    # print(type(elevationMotor.angle()))
    # tmp = int(elevationMotor.angle())
    # print(tmp)
    if elevationMotor.angle() != armStartAngle:
        armMovement(armStartAngle, calibrate= True)

    print("Calibrate claw\n\n")
    clawMovement(None, calibrate= True)
    # clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None)

    rotateBase(angle= 0)
    return 0



## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    # armMovement(angleTarget= 40)
    
    # for i in range(3):
    # clawMovement(False)

    # Calibrate(50)
    # armMovement(angleTarget= 20)
    # rotateBase(90)
    # Calibrate(50)
    main()