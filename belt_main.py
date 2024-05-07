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

# def change_speed(change, speed):
#     if -150 < speed + change <= 150:
#         speed += change
#         ev3.screen.print("Speed:", speed)
#         belt.run(speed)
#         wait(300)
#     return speed

# def main():
#     speed = 50
#     belt_on = True
#     belt.run(speed)
#     ev3.screen.print("Speed:", speed)

#     while True:
#         if Button.CENTER in ev3.buttons.pressed():
#             if belt_on:
#                 ev3.light.on(Color.RED)
#                 belt.hold()
#                 ev3.screen.print("STOP")
#             else:
#                 ev3.light.on(Color.GREEN)
#                 belt.run(speed)
#                 ev3.screen.print("Speed:", speed)
#             belt_on = not belt_on
#             wait(2000)
#         if Button.UP in ev3.buttons.pressed() and belt_on:
#             speed = change_speed(10, speed)
#         if Button.DOWN in ev3.buttons.pressed() and belt_on:
#             speed = change_speed(-10, speed)
#         wait(100)


#####################coms##########################

collaborator = 'A'


def resturaunt():
    SERVER = 'ev3dev-' + collaborator
    # SERVER = 'ev3dev-' + collaborator
    client = BluetoothMailboxClient()
    mbox = TextMailbox('greeting', client)
    # ev3.screen.print('establishing connection...')

    while True:
        ev3.screen.print('establishing connection...')
        ev3.screen.print("With " + SERVER)


        try:
            client.connect(SERVER)
            ev3.screen.clear()
            break
        except ValueError:
            ev3.screen.clear()
            ev3.screen.print("Failed to connect")
            wait(5000)



    ev3.screen.print('connected!')

    ev3.screen.print('entering whileloop')
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
    