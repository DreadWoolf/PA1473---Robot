#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

# from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait



# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

ev3 = EV3Brick()
client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

ev3.speaker.beep()

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# # In this program, the client sends the first message and then waits for the
# # server to reply.
# for i in range(4):
mbox.send('hello!')
mbox.wait()
test = mbox.read()
ev3.screen.print(test)

print(test)

#     wait(5000)