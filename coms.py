#!/usr/bin/env pybricks-micropython

from Parameters import *



distributeText = ['receevied', 'occupied']

# 0 : receevied, 1: Occupied.
distribute = [False, False]




def coms(mbox):
    
    print("I'm listning")
    while True:
        if thread2Alive[0] == False: break

        try:
            mbox.wait()
        except:
            wait(500)

        inbox = mbox.read()

        # Testing purposes.
        # print("Recevied message: ", str(inbox))

        if inbox == messages[0]: # Occupied
            distribute[1] = True # Collision warning!
            # Detta fel.
            # distribute[0] = False # receevied is false.
            ev3.speaker.beep()
            ev3.screen.print("Collision warning!")
        
        elif inbox == messages[1]: # giftForme
            ev3.speaker.beep()

            # Package has been delivered to us and safe to go there.
            distribute[0] = True  # receevied
            
            wait(10)
            ev3.screen.print(inbox)
            
        elif inbox == messages[5]: # Free
            distribute[0] = False # Occupied

        elif inbox == messages[4]: # Emergency stop
            Estop[0] = True  # does this work?


        
        


def sendMessage(mbox):
    # Testing purposes.
    # print("sending message: ", send[0])

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
            elif send[0] == messages[2]: #'feed'
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

    if send[0] != messages[0]: # do not reset from occupied
        send[0] = messages[-1] # Set to nothing, we have sent the message.






# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.
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
        mbox = TextMailbox('greeting', me[0])

    else:
        print("I'm Client")
        client = BluetoothMailboxClient()
        me[0] = client
        mbox = TextMailbox('greeting', me[0])
        for collaborator in collaborators:
                # This is the name of the remote EV3 or PC we are connecting to.
                SERVERID = 'ev3dev-' + collaborator
                ev3.screen.print("Attempting to connect to\n" + SERVERID)
                if collaborator != RobotIdentity:
                    try:
                        ev3.screen.print('establishing connection...')
                        wait(10)
                        me[0].connect(SERVERID)
                        ev3.screen.clear()
                        ev3.screen.print("Connected")
                        wait(1000)
                        ev3.screen.clear()
                    except ValueError:
                        ev3.screen.print("Failed to connect to\n"+ SERVERID)
                        wait(1000)
                        ev3.screen.clear()
    
    return mbox




if __name__ == "__main__":
    mbox = Connect()
    coms(mbox)