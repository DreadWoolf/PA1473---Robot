#!/usr/bin/env pybricks-micropython

from Parameters import *


distributeText = ['receevied', 'deliver']  #0 : receevied, 1: deliver.
distribute = [False, False]




def coms(mbox):
    # global mbox
    # mbox = Connect()
    while True:
        if thread2Alive[0] == False: break

        try:
            mbox.wait()
        except:
            wait(500)

        inbox = mbox.read()

        if inbox == messages[0]: # Occupied
            distribute[1] = True # Collision warning!
            distribute[0] = False # receevied is false.
            ev3.sepaker.beep()
            ev3.screen.print("Collision warning!")
        
        elif inbox == messages[1]: # giftForme
            ev3.speaker.beep()
            # Will go there and pick up the stuff
            # send[0] = 'occupied' # Send occupied signal.

            # Package has been delivered to us and safe to go there.
            distribute[0] = True  # receevied
            distribute[1] = False # occupied 
            wait(10)
            ev3.screen.print(inbox)
            # while True:
            #     if send[0] == 0:
            #         text = messages[0]
            #         print(text)
            #         sendMessage()
            #         # mbox.send(text)
            #         send[0] == 3
            #         break
            #     else:
            #         wait(300)
        elif inbox == messages[5]: # Free
            distribute[0] = False # Occupied
            distribute[1] = False # Receevied
        elif inbox == messages[4]: # Emergency stop
            Estop[0] = True  # does this work?


        
        


def sendMessage(mbox):
    # global mbox
    print("sending message: ", send[0])
    do = True

    while do:
        try:
            if send[0] == messages[0]: # Occupied
                text = send[0]  # occupied
                mbox.send(text)
                do = False
            elif send[0] == messages[1]: # gif4u
                text = send[0]  # gif4u
                mbox.send(text)
                do = False
            elif send[0] == messages[2]: #'feed':
                text = send[0] #messages[2]  # feed
                print("sent message ", send[0])
                mbox.send(text)
                do = False
            elif send[0] == messages[3]: # Stop belt
                text = send[0]  # stop
                mbox.send(text)
                do = False
            elif send[0] == messages[4]: # Emergency
                text = send[0]  # emergency
                mbox.send(text)
                do = False
        except:
            wait(5)






def Connect():



    if me[0] == 'server':
        print("I'm server")
        server = BluetoothMailboxServer()
        me[0] = server
        ev3.screen.print("wait for connection")
        me[0].wait_for_connection()
        ev3.screen.clear()
        ev3.screen.print("Connected")
        wait(1000)
        ev3.screen.clear()
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

    
    return mbox




if __name__ == "__main__":
    mbox = Connect()
    coms(mbox)