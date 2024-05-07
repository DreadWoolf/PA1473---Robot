#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

# from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
# Pybricks imports
# from pybricks import robotics
# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import Motor
# from pybricks.parameters import Port, Stop
# from pybricks.tools import wait
ev3 = EV3Brick()
#collaborator = 'D'
collaborators = ['A', 'B', 'C', 'D','E','F','G']
for collaborator in collaborators:
    try:
        SERVER = 'ev3dev-' + collaborator
        client = BluetoothMailboxClient()
        mbox = TextMailbox('greeting', client)
        do = True
    except: #value error?
        wait(5)

while do:
    ev3.screen.print('gonna connect!!')
    try:
        client.connect(SERVER)
        do = False
    except:
        wait(500)
        

while True:

    ev3.screen.print('connected!')

    ev3.screen.print('sedning <3')
    mbox.send('gift4u')
    mbox.wait()
    inbox = mbox.read()
    if inbox == 'occupied':
        ev3.screen.print(inbox)
        ev3.speaker.beep()
        ev3.screen.print("ok!")
        ev3.screen.print("i wont go there")
        wait(12000)
        ev3.screen.clear()


# # This is the name of the remote EV3 or PC we are connecting to.
# SERVER = 'ev3dev'

# ev3 = EV3Brick()
# client = BluetoothMailboxClient()
# mbox = TextMailbox('greeting', client) # <---- ska det inte stå SERVER ist för client

# ev3.speaker.beep()

# print('establishing connection...')
# client.connect(SERVER)
# print('connected!')

# # # In this program, the client sends the first message and then waits for the
# # # server to reply.
# # for i in range(4):
# mbox.send('hello!')
# mbox.wait()
# test = mbox.read()
# ev3.screen.print(test)

# print(test)

# #     wait(5000)