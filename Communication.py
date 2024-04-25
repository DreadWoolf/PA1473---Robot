#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
from Parameters import *
#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox, BluetoothMailboxServer

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

me = 'server'
# This is the name of the remote EV3 or PC we are connecting to.
SERVERID = 'ev3dev'

if me == 'server':
    print("I'm server")
    server = BluetoothMailboxServer()
    me = server
    me.wait_for_connection()
else:
    # This is the name of the remote EV3 or PC we are connecting to.
    # SERVER = 'ev3dev'
    print("I'm Client")
    client = BluetoothMailboxClient()
    me = client    
    me.connect(SERVERID)
    print('connected!')


ev3 = EV3Brick()
# client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', me)
ev3.speaker.beep()
# print('establishing connection...')


# # In this program, the client sends the first message and then waits for the
# # server to reply.
# for i in range(4):
messages = ['occupied', 'gift4u']

if me == 'client':
    mbox.send(messages[1])
else:
    mbox.wait()

for i in range(5):
    print("Started loop")
    # mbox.send('hello!')
    inbox = mbox.read()
    while inbox == messages[0]: 
        inbox = mbox.read()
        ev3.screen.print(inbox)
    
    if inbox == messages[1]:
        message = messages[0]
    else:
        message = ''

    mbox.send(message)
    # mbox.wait()
    # test = mbox.read()
    ev3.screen.print(message)

    # print(test)

    wait(5000)




#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# # paired using Bluetooth, but do NOT connect them. The program will take care
# # of establishing the connection.

# # The server must be started before the client!

# from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# # # Pybricks imports
# # from pybricks import robotics
# from pybricks.hubs import EV3Brick
# # from pybricks.ev3devices import Motor
# # from pybricks.parameters import Port, Stop
# from pybricks.tools import wait

# ev3 = EV3Brick()
# server = BluetoothMailboxServer()
# mbox = TextMailbox('greeting', server)

# ev3.speaker.beep()

# # The server must be started before the client!
# print('waiting for connection...')
# server.wait_for_connection()
# print('connected!')
# ev3.speaker.beep()



# # In this program, the server waits for the client to send the first message
# # and then sends a reply.
# for i in range(4):
#     mbox.wait()
#     test = mbox.read()
#     ev3.screen.print(test)
#     print(test)
#     mbox.send('hello to you!')

#     wait(5000)