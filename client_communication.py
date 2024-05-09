#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

# from pybricks.messaging import BluetoothMailboxClient, TextMailbox
# from pybricks.messaging import BluetoothMailboxClient, TextMailbox
# from pybricks.tools import wait
# from pybricks.hubs import EV3Brick

from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxClient, TextMailbox, BluetoothMailboxServer

from coms import coms, sendMessage, Connect, messages, send
import threading as th
# from Parameters import messages, send

# Pybricks imports
# from pybricks import robotics
# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import Motor
# from pybricks.parameters import Port, Stop
# from pybricks.tools import wait
ev3 = EV3Brick()
#collaborator = 'D'
mbox = ''
collaborators = ['A', 'B', 'C', 'D','E','F','G']

mbox = Connect()
# for collaborator in collaborators:
#     try:
#         SERVER = 'ev3dev-' + collaborator
#         client = BluetoothMailboxClient()
#         mbox = TextMailbox('greeting', client)
#         do = True
#     except: #value error?
#         wait(5)

# while do:
#     ev3.screen.print('gonna connect!!')
#     try:
#         client.connect(SERVER)
#         do = False
#     except:
#         wait(500)

myThread = th.Thread(target=coms, args=(mbox,))
myThread.start()

def main2():

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



def main():

    #DO your stuff and get to work!
    #okidoki

    # messages = ['occupied', 'gift4u', 'feed', 'stop', 'emergency', 'free', 'nothing']
    # send = ['nothing']
    ev3.screen.print("L:occupiedU:gift4u\nD:feedR:stopC.UR:emergency\nC.LR:freeC.UD:nothing")

    temp = True
    while temp:
        wait(250)
        buttons = ev3.buttons.pressed()
        # print("buttons:", buttons)
        for button in buttons:
            combos = [str(obj) for obj in buttons]
            # print("combos:", combos)
            if str(button) == "Button.LEFT":
                send[0] = messages[0] # Occcupied
                sendMessage(mbox)        
            if str(button) == "Button.UP":
                send[0] = messages[1] # gift4u
                sendMessage(mbox)
            if str(button) == "Button.DOWN":
                send[0] = messages[2] # feed
                sendMessage(mbox)
            if str(button) == "Button.RIGHT":
                send[0] = messages[3] # stop
                sendMessage(mbox)
            if combos == ["Button.UP", "Button.RIGHT"] or combos == ["Button.RIGHT", "Button.UP"]:  
                send[0] = messages[4] # emergency
                sendMessage(mbox)
            if str(button) == "Button.CENTER":
                send[0] = messages[5] # free
                sendMessage(mbox)
            if combos == ["Button.UP", "Button.DOWN"] or combos == ["Button.DOWN", "Button.UP"]:  
                send[0] = messages[6] # nothing
                sendMessage(mbox)
#            if str(button) == "Button.CENTER":
#                temp = False # exit
    return 0






if __name__ == "__main__":
    main()