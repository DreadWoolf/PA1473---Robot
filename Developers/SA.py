def armMovement(goToZone, angleTarget: int, height: int = 0, operatingSpeed = 120, calibrate: bool = False, potentialCargo = False):
    # Thooths on the gears of the arm.
    bigGear = 40
    smallGear = 8
    multiplyAngle = -(bigGear/smallGear)
    # global Estop
    elevationMotor.run_target(operatingSpeed, target_angle * multiplyAngle)

    height = zoneHeight[goToZone]  # Gets the hegiht for the zone.
    target_angle = angleTarget - height

    # print("Estop  ... ", Estop)

    if calibrate:
        # print("start arm angle " , elevationMotor.angle())
        elevationMotor.run_target(speed = 60, target_angle = angleTarget - height)
        # return
    elif height == 0 and potentialCargo and angleTarget <= 40 * multiplyAngle - 5 and angleTarget >= 40 * multiplyAngle + 5:
        elevationMotor.run_until_stalled(operatingSpeed, then=Stop.HOLD, duty_limit=20)
        # elevationMotor.run_stall(operatingSpeed,(angleTarget - height) * multiplyAngle)
    else:
        ######################################
        ######################################
        ######################################
        #           Här @subhi               #
        # Bör dock vara klart för hantering om vilken höjd.
        #           (angleTarget - height)   #
        ######################################
        ######################################
        ######################################
        
        elevationMotor.run_target(operatingSpeed, target_angle * multiplyAngle)

    # print("targeted arm angle " , elevationMotor.angle())

    # Check if the event is set
    # if Event.is_set():
    #     # Process the updated global variable
    #     print("Thread 2: Global variable (Estop):", Estop)
    #     # Clear the event
    #     Event.clear()
    #test(goToZone, angleTarget, calibrate)
    