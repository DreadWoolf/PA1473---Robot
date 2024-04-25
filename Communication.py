#!/usr/bin/env pybricks-micropython
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.hubs import EV3Brick


# Change this later
# from Parameters import *
ev3 = EV3Brick()

# Initialize the hub.
hub = TechnicHub(broadcast_channel=1)
observe = TechnicHub(observe_channels=2)

# # Initialize the motors.
# left_motor = Motor(Port.A)
# right_motor = Motor(Port.B)


data = True
listeningData = False

while True:
    # # Read the motor angles to be sent to the other hub.
    # left_angle = left_motor.angle()
    # right_angle = right_motor.angle()

    # # Set the broadcast data and start broadcasting if not already doing so.
    # data = (left_angle, right_angle)

    # data = True

    if data:
        hub.ble.broadcast(data)
        data = False
    else:
        hub.ble.broadcast(data)
        data = True

    listeningData = hub.ble.observe(2)
    if listeningData:
        ev3.speaker.beep()
    
    print("Sending data is: ", data)
    print("listening data is: ", listeningData)
    


    # Broadcasts are only sent every 100 milliseconds, so there is no reason
    # to call the broadcast() method more often than that.
    wait(100)


# Initialize the hub.
# hub = TechnicHub(observe_channels=[1])

# # Initialize the motors.
# left_motor = Motor(Port.A)
# right_motor = Motor(Port.B)

# while True:
#     # Receive broadcast from the other hub.

# #     data = hub.ble.observe(1)

#     if data is None:
#         # No data has been received in the last 1 second.
#         hub.light.on(Color.RED)
#     else:
#         # Data was received and is less that one second old.
#         hub.light.on(Color.GREEN)

#         # *data* contains the same values in the same order
#         # that were passed to hub.ble.broadcast() on the
#         # other hub.
#         left_angle, right_angle = data

#         # Make the motors on this hub mirror the position of the
#         # motors on the other hub.
#         left_motor.track_target(left_angle)
#         right_motor.track_target(right_angle)

#     # Broadcasts are only sent every 100 milliseconds, so there is
#     # no reason to call the observe() method more often than that.
#     wait(100)
