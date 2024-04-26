#!/usr/bin/env pybricks-micropython

from Parameters import *
from pybricks.messaging import BluetoothMailboxClient, TextMailbox, BluetoothMailboxServer


distribute = [False, False]  #0 : receevied, 1: deliver.

def coms():
    mbox = Connect()
    while True:
        mbox.wait()
        inbox = mbox.read()
        if inbox == messages[1]:
            ev3.speaker.beep()
            distribute[0] = True
            send[0] = 0
            wait(10)
            ev3.screen.print(inbox)
            while True:
                if send[0] == 0:
                    text = messages[0]
                    print(text)
                    mbox.send(text)
                    send[0] == 3
                    break
                else:
                    wait(300)



def Connect():
    if me[0] == 'server':
        print("I'm server")
        server = BluetoothMailboxServer()
        me[0] = server
        me[0].wait_for_connection()
    else:
        # This is the name of the remote EV3 or PC we are connecting to.
        # SERVER = 'ev3dev'
        print("I'm Client")
        client = BluetoothMailboxClient()
        me[0] = client    
        me[0].connect(SERVERID)
        print('connected!')
        # client = BluetoothMailboxClient()
        ev3.speaker.beep()
    
    mbox = TextMailbox('greeting', me[0])

    
    # if me == 'client':
    #     mbox.send(messages[1])
    # else:
    #     mbox.wait()
    return mbox


# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
#!/usr/bin/env pybricks-micropython


# print('establishing connection...')


# # In this program, the client sends the first message and then waits for the
# # server to reply.
# for i in range(4):

# if me == 'client':
#     mbox.send(messages[1])
# else:
#     mbox.wait()

# for i in range(5):
#     print("Started loop")
#     # mbox.send('hello!')
#     inbox = mbox.read()
#     while inbox == messages[0]: 
#         inbox = mbox.read()
#         ev3.screen.print(inbox)
    
#     if inbox == messages[1]:
#         message = messages[0]
#     else:
#         message = ''

#     mbox.send(message)
#     # mbox.wait()
#     # test = mbox.read()
#     ev3.screen.print(message)

#     # print(test)

#     wait(5000)




if __name__ == "__main__":
    coms()