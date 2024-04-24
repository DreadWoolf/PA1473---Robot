#!/usr/bin/env pybricks-micropython


from Parameters import colorSense, wait , zoneSort

## ladda in vilka färgar ska vart.
# zoneSort1 = zoneSort


def newcolor():
    tred=0
    tgreen=0
    tblue=0

    for i in range(50):
      red,green,blue=colorSense.rgb()
      tred += red
      tgreen += green
      tblue += blue

    tred=tred//50
    tblue=tblue//50
    tgreen=tgreen//50

    list1 = [tred,tgreen,tblue]
    list2 = ["r","g","b"]
    cond = ""
    margin = 3


    rec = 0
    for i in range(len(list1)):
        for j in (range(len(list1))):
            if i != j:  # To avoid comparing the number with itself
                if i == 0:
                    if list1[i] > list1[j]+margin and list1[i] > list1[j]-margin:
                        cond += " ("+list2[i] + ">" +list2[j]+"+margin or "+list2[i] + ">" + list2[j]+"-margin) "
                    if  abs(list1[i] - list1[j]) <= margin:
                        cond+= " abs("+list2[i]+ "-" +list2[j]+") <= margin "
                else: 
                    if list1[i] > list1[j]+margin and list1[i] > list1[j]-margin:
                        cond = cond +" and ("+list2[i] + ">"+ list2[j]+" +margin or " + list2[i] + ">" + list2[j]+"-margin) "
                    if  abs(list1[i] - list1[j]) <= margin:
                        cond = cond + " and abs("+list2[i]+ "-" +list2[j]+") <= margin "

    condition = lambda r,g,b,re:eval(cond)
    return condition

    

def ngetColor():
    aos = 5
    hred,hgreen,hblue = 0,0,0
    for scan in range(aos):
        red,green,blue = colorSense.rgb()
        hred += red
        hgreen += green
        hblue += blue
        wait(50)
    print(hred,hgreen,hblue)
    print(abs(hred-hblue))
    colors = [
    ("Blue", lambda r, g, b: b > max(r, g)),
    ("Yellow", lambda r, g, b: r > b and g > b and r > g),
    ("Red", lambda r, g, b: r > max(g, b)),
    ("Green", lambda r, g, b: g > max(r, b)),
    ("nothing", lambda r, g, b: max(r, g, b) == 0)
    ]

    # Check each color condition
    for color_name, condition in colors:
        if condition(hred, hgreen, hblue):
            print(color_name)
            return color_name 
    return "unknown item"  # Object doesn't match any color predominantly









def getColor():
    # Get RGB values from the sensor (assuming they are in the range 0-100)
    fcolor = colorSense.color()
    dis = 2
    aos = 3
    Tred, Tgreen, Tblue, Tref = 0,0,0,0
    for i in range(aos):   
        red, green, blue = colorSense.rgb()
        ref = colorSense.reflection()
        Tref += ref
        Tred += red
        Tgreen += green
        Tblue += blue
        wait(50)
    Tred = Tred//aos
    Tgreen = Tgreen//aos
    Tblue = Tblue//aos
    Tref = Tref//aos
    Tred, Tgreen, Tblue = dis*Tred, dis*Tgreen, dis*Tblue
    # Define margin of error
    margin = 15  # Adjust the margin as needed
    lmargin = 5
    # Define colors and their conditions
    colors = [
        ("Green", lambda r, g, b ,re: (g > r + margin and g > r - margin) and (g > b + margin and g > b - margin) and (g > (margin - lmargin)*dis) or  fcolor=="Color.GREEN"),
        ("Blue", lambda r, g, b, re: (b > r + margin and b > r - margin) and (b > g + margin and b > g - margin) and (b > (margin - lmargin)*dis)),
        ("Yellow", lambda r, g, b, re:(abs(g - (r/2)) <= margin) and (g > b + margin and g > b - margin) and (r > b + margin and r > b - margin ) or fcolor =="Color.YELLOW"),
        ("Red", lambda r, g, b ,re: (r > g + margin and r > g - margin) and (r > b + margin and r > b - margin ) and (r > (margin - lmargin)*dis) and  (55+lmargin>=re>=45-lmargin)), # runt 50
        ("Green", lambda r, g, b, re: abs(g - b) <= margin and (g > r + margin or g > r - margin) and (b > r + margin or b > r - margin) and g > (margin-lmargin)*dis and b > (margin-lmargin)*dis ),  # Condition for Greenb
        ("nothing", lambda r, g, b, re: ((margin)>=r>=0) and ((margin)>=g>=0) and ((margin)>=b>=0))
        # Add more colors here
        # ("ColorName", lambda r, g, b: <condition>)
    ]
    
    # Check each color condition
    for color_name, condition in colors:
        if condition(Tred, Tgreen, Tblue, Tref):
            print(Tred, Tgreen, Tblue)
            print(color_name)
            return color_name
        
    return "unknown item"  # Object doesn't match any color predominantly


# def colorSort():
#     color = getColor()
#     print(color)
#     if color == 'nothing':
#     # if zoneSort[color] == 0:
#         return color, None  # nothing, the color is not in the list.
#     elif color in zoneSort:    
#         return zoneSort[color], color
#     # elif color in zoneSort and zoneSort[color]!=0:    
#         # return color, zoneSort[color] # Return the color.
#     else:
#         return 'Error', None # Did not find any color.
    
def colorSort():
    color = ngetColor()
    print(color)
    if color == 'nothing':
        print(color)
    # if zoneSort[color] == 0:
        return 'Error', None  # nothing, the color is not in the list.
    elif color in zoneSort:    
        return zoneSort[color], color
    # elif color in zoneSort and zoneSort[color]!=0:    
        # return color, zoneSort[color] # Return the color.
    else:
        print(color)
        return 'nothing', None # Did not find any color.


if __name__ == "__main__":
    while True:
        something, color = (colorSort())
        print(something)
        print(color)
        wait(3000)