#!/usr/bin/env pybricks-micropython

from Parameters import *
from rotationMotor import rotateBase
from Arm_and_Claw import armMovement, clawMovement


def emergencyStop(gotoZone:int, angletarget:int, duringCallibration = False):
    global Estop
    global restart

    while(Estop):
        elevationMotor.hold()
        clawMotor.hold()
        rotationMotor.hold()
        wait(1000)
        # if Estop == False:
        if restart:
            s.sys.exit()

    rotateBase(zoneLocation[gotoZone], 80, duringCallibration)
    armMovement(angletarget, zoneHeight[gotoZone], 80, duringCallibration)
    clawMovement(False, calibrate= True)