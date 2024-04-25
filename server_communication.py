#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxServer, TextMailbox, BluetoothMailboxClient

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')

# # Pybricks imports
# from pybricks import robotics
from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import Motor
# from pybricks.parameters import Port, Stop
from pybricks.tools import wait

ev3 = EV3Brick()
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

ev3.speaker.beep()

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')
ev3.speaker.beep()



# In this program, the server waits for the client to send the first message
# and then sends a reply.
# for i in range(4):
mbox.wait()
test = mbox.read()
ev3.screen.print(test)
print(test)
mbox.send('hello to you!')

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