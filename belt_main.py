#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Direction, Port, Stop, Button, Color
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

# Load belt
belt = Motor(Port.D, Direction.CLOCKWISE)
belt.control.limits(speed=150, acceleration=60)

def change_speed(change, speed):
    if -150 < speed + change <= 150:
        speed += change
        ev3.screen.print("Speed:", speed)
        belt.run(speed)
        wait(300)
    return speed

def main():
    speed = 50
    belt_on = True
    belt.run(speed)
    ev3.screen.print("Speed:", speed)

    while True:
        if Button.CENTER in ev3.buttons.pressed():
            if belt_on:
                ev3.light.on(Color.RED)
                belt.hold()
                ev3.screen.print("STOP")
            else:
                ev3.light.on(Color.GREEN)
                belt.run(speed)
                ev3.screen.print("Speed:", speed)
            belt_on = not belt_on
            wait(2000)
        if Button.UP in ev3.buttons.pressed() and belt_on:
            speed = change_speed(10, speed)
        if Button.DOWN in ev3.buttons.pressed() and belt_on:
            speed = change_speed(-10, speed)
        wait(100)


#####################3coms##########################
def resturaunt(order):
    while order == "feed":
        speed = 50
        ev3.screen.print("Speed:", speed)
        belt.run(speed)
        wait(300)
    speed = 0
    ev3.screen.print("Speed:", speed)
    belt.stop()
    # elif order == "wait":
    #     speed = 0
    #     ev3.screen.print("Speed:", speed)
    #     belt.run(speed)
    #     wait(300)
    #     return 1

SERVER = 'ev3dev'
client = BluetoothMailboxClient()
mbox = TextMailbox('kitchen', client)
print('establishing connection...')
client.connect(SERVER)
print('connected!')
while True:
    mbox.wait()
    inbox = mbox.read()
    resturaunt(inbox)


if __name__ == '__main__':
    main()
    #when get "feed" being feeding!!!