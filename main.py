#!/usr/bin/env pybricks-micropython

# Should import all, and work otherwise uncomment the stuff.
from Parameters import *
from Arm_and_Claw import Place, Pickup, armMovement
from rotationMotor import rotateBase
from colorAlgorithm import colorSort

def main():
    ev3.speaker.beep()

    times = 2
    zoneAmount = 3
    potentialCargo = False
    periodTime = 4000 # 4s (4000)
    
    Calibrate()
    
    run = 0
    location = 1
    lastZone = 0
    
    while run < times: # times = 2.
        run += 1

        goToZone = location


        if potentialCargo:
            sortZone = 0
            ######################################
            ######################################
            ######################################
            #       sortZone = Sort algorithm()
            # sortZone = colorSort()
            sortZone, color = colorSort()

            if sortZone == 'Error' or sortZone == "nothing":

                ## Will continue if found nothing, otherwise place the cargo.
                if sortZone == "Error":
                    
                    ev3.speaker.beep()
                    wait(4)
                    ev3.speaker.beep()

                    ### print error on robot.
                    ev3.screen.print("ERROR, color not supported")
                    wait(100)

                    ## Drop of again, if detected random color.
                    Place(angleTarget=-35, openClawsFirst=False)

            else:
                ### Screen print 
                ev3.screen.print("Color: " + color + " to zone: " + str(sortZone))
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
                lastZone = sortZone  # 0
            
            Place(angleTarget= -35, openClawsFirst= False)
            potentialCargo = False

        else:
            rotateBase(angle = zoneLocation[goToZone] - zoneLocation[lastZone])
            Pickup(angleTarget= -35, openClawsFirst= True)

            # picked up package true or false.
            ######################################
            ######################################
            ######################################
            # Check if we have cargo!
            potentialCargo = True

        print("Check color \nWhere to next= ", location)


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
                wait(periodTime)  # 4000
                ev3.speaker.beep()
        
        
        ######################################
        ######################################
        ######################################
        # Testing placment (problem since the code above is increasing before this)
        # if location == 2 + 1:
        #     potentialCargo = True
        #     print("loc is True")
                    

        

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



## Checks if this is the running script, and not imported from somewhere!
if __name__ == "__main__":
    armMovement(angleTarget= 35)
    
    # for i in range(3):
    # clawMovement(False)
    main()