
## ladda in vilka färgar ska vart.
zoneSort = {
    'red'       : 0,
    'nothing'   : 1,
    'blue'      : 2,
    'yellow'    : 3
}


######################################
######################################
######################################
#           Här @mop                 #
######################################
######################################
######################################

def getColor():

    return 'red'

def colorSort():
    color = getColor()

    if color in zoneSort:    
        return zoneSort[color]
    else:
        return 'Error'