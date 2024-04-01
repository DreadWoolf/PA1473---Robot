

zoneSort = {
    'red'       : 0,
    'nothing'   : 1,
    'blue'      : 2,
    'yellow'    : 3
}


######################################
def newcolor():
    list1 = [12,11,50]
    list2 = ["r","g","b"]
    cond=""
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

    condition = lambda r,g,b:eval(cond)


    r=12
    g=13
    b=50
    print(cond)
    if condition(r,g,b):
        print("yeah")
    else:
        print("nah")
    

    

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


def colorSort():
    color = getColor()

    if color in zoneSort:    
        return zoneSort[color]
    else:
        return 'Error'