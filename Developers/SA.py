#!/usr/bin/env pybricks-micropython
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

def getColor():
    # Get RGB values from the sensor (assuming they are in the range 0-100)
    fcolor = colorSense.color()
    ref = colorSense.reflection()
    dis = 3
    red, green, blue = colorSense.rgb()
    red, green, blue = dis*red, dis*green, dis*blue
    # Define margin of error
    margin = 33  # Adjust the margin as needed
    lmargin = 15
    # Define colors and their conditions
    colors = [
        ("Red", lambda r, g, b ,re: (r > g + margin or r > g - margin) and (r > b + margin or r > b - margin ) and (r > (margin - lmargin)*dis) and  (50+lmargin>=re>=50-lmargin)),
        ("Green", lambda r, g, b ,re: (g > r + margin or g > r - margin) and (g > b + margin or g > b - margin) and (g > (margin - lmargin)*dis) or (fcolor=="Color.YELLOW" or fcolor=="Color.GREEN")),
        ("Blue", lambda r, g, b, re: (b > r + margin or b > r - margin) and (b > g + margin or b > g - margin) and (b > (margin - lmargin)*dis)),
        ("Greenb", lambda r, g, b, re: abs(g - b) <= margin and (g > r + margin or g > r - margin) and (b > r + margin or b > r - margin) and g > (margin-lmargin)*dis and b > (margin-lmargin)*dis ),  # Condition for Greenb
        ("nothing", lambda r, g, b, re: ((margin)>=r>=0) and ((margin)>=g>=0) or ((margin)>=b>=0))
        # Add more colors here
        # ("ColorName", lambda r, g, b: <condition>)
    ]
    # Check each color condition
    for color_name, condition in colors:
        if condition(red, green, blue, ref):
            return color_name

    return "unknown item"  # Object doesn't match any color predominantly
