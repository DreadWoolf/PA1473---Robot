#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.ev3devices import Motor
from pybricks.parameters import Direction, Port, Stop, Button, Color
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

# Load belt
belt = Motor(Port.D, Direction.CLOCKWISE)
belt.control.limits(speed=150, acceleration=60)

#####################coms##########################

#collaborator = 'D'
collaborators = ['A', 'B', 'C', 'D','E','F','G']


def resturaunt():
    client = BluetoothMailboxClient()
    mbox = TextMailbox('greeting', client)

    for collaborator in collaborators:
        SERVER = 'ev3dev-' + collaborator
        ev3.screen.print('establishing connection...')
        ev3.screen.print("With " + SERVER)
        try:
            client.connect(SERVER)
            ev3.screen.clear()

            break
        # ev3.screen.print('establishing connection...')
        except ValueError:
            ev3.screen.print("Failed to connect to\n"+ SERVER)
            wait(5000)
            ev3.screen.clear()



    ev3.screen.print('connected!')

    while True:
        mbox.wait() #here we got an error
        ev3.screen.print('reeved')
        inbox = mbox.read()
        ev3.screen.print("read!")
        if inbox == "feed":
            speed = 50
            ev3.screen.print("Speed:", speed)
            belt.run(speed)
        elif inbox == "stop":
            ev3.screen.print("halt!")
            belt.stop()


def main():
    ev3.screen.print("Waiting for \ncenter btn")
    do = True
    while do:
        buttons = ev3.buttons.pressed()
        wait(250) # 250
        for button in buttons:
            if str(button) == "Button.CENTER":
                ev3.speaker.beep()        
                ev3.screen.clear()
                wait(5)
                do = False
                break  # Avbryt loopen när knappen trycks

    resturaunt()   #when geting "feed" feed material!!!


if __name__ == '__main__':
    main()
    