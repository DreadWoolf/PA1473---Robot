#!/usr/bin/env pybricks-micropython
from Parameters import *




def menu(zoneHeight = zoneHeight, zoneSort = zoneSort):
    choicelist = ["start_code", "set_origin","zonecolor_selection","zone_hight","work_times"]
    current_index=0
    temp=True
    zoneHeight[2] = 30
    inMenu[0]= True
    
    if Estop[0] == False:
        ev3.screen.print("set origin first")
        set_origin()
        #tempfunc()
        ev3.screen.clear()
        ev3.screen.print(choicelist[current_index])
    else:
        ev3.screen.print(choicelist[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
                 
        for button in buttons:
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(choicelist)
                ev3.screen.print(choicelist[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(choicelist)
                ev3.screen.print(choicelist[current_index])
            
            if str(button) == "Button.CENTER":
                ev3.screen.clear()
                ev3.screen.print("you chose ",choicelist[current_index])
            
                    # DO emergency shit!
                    # if resume pressed Estop = False
                if choicelist[current_index] == "zone_hight":
                    ev3.speaker.beep()
                    zoneHeight = zone_hight()
                    print(zoneHeight)
                    ev3.screen.clear()
                    ev3.screen.print(choicelist[current_index])
                if choicelist[current_index] == "set_origin":
                    ev3.speaker.beep()
                    origin = set_origin()
                    print(origin)
                    
                    ev3.screen.clear()
                    ev3.screen.print(choicelist[current_index])
                if choicelist[current_index] == "zonecolor_selection":
                    ev3.speaker.beep()
                    zoneSort = colorzones()
                    print(zoneSort)
                    ev3.screen.clear()
                    ev3.screen.print(choicelist[current_index])
                if choicelist[current_index] =="work_times":
                    ev3.speaker.beep()
                    work_times()
                    ev3.screen.clear()
                    ev3.screen.print(choicelist[current_index])
                if choicelist[current_index] == "start_code":
                    ev3.speaker.beep()
                    inMenu[0] = False
                    return zoneSort , zoneHeight
                # if choicelist[current_index] == "EMERGENCY" and Estop:
                #     return 0




def Emenu(zoneSort:dict, zoneHeight:dict):
    Echoicelist = ["resume", "manual", "startmenu"] #, "restart"]
    current_index=0
    do = True

    ev3.screen.print(Echoicelist[current_index])

    while do:
        buttons= ev3.buttons.pressed()
        wait(250)
        #ev3.speaker.say("Emergency!")
        for button in buttons:
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(Echoicelist)
                ev3.screen.print(Echoicelist[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(Echoicelist)
                ev3.screen.print(Echoicelist[current_index])
            
            if str(button) == "Button.CENTER":
                ev3.speaker.beep()
                ev3.screen.clear()
                ev3.screen.print("you chose ",Echoicelist[current_index])
                # if Echoicelist[current_index] == "restart":
                #     restart = True
                #     wait(5)
                #     ev3.screen.clear()
                #     return
                if Echoicelist[current_index] == "resume":
                    # Estop[0] = False
                    wait(5)
                    ev3.screen.clear()
                    ev3.screen.print(Echoicelist[current_index])
                    do = False
                
                if Echoicelist[current_index] == "startmenu":
                    ev3.screen.clear()
                    zoneSort, zoneHeight = menu(zoneHeight, zoneSort)
                    ev3.screen.clear()
                    ev3.screen.print(Echoicelist[current_index])
                    do = False

                if Echoicelist[current_index] == "manual":
                    ev3.screen.clear()
                    ev3.screen.print("manual control")
                    set_origin()
                    ev3.screen.clear()
    Estop[0] = False
    return zoneSort, zoneHeight
    
             



def get_user_input(prompt, min_value, max_value):
    """
    Get user input using buttons and limit the value between min_value and max_value.
    """
    value = min_value
    temp=True
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)             
        for button in buttons:
            strbut = str(button) 
            ev3.screen.clear()
            ev3.screen.print(prompt)
            ev3.screen.print(str(value))
            if strbut == "Button.RIGHT":
                if value < max_value:
                    value = value + 1 
                    ev3.screen.clear()
                    ev3.screen.print(prompt)
                    ev3.screen.print(str(value))
            elif strbut == "Button.LEFT":
                if value > min_value:
                    value = value - 1
                    ev3.screen.clear()
                    ev3.screen.print(prompt)
                    ev3.screen.print(str(value))
            elif strbut == "Button.CENTER":
                temp=False
    return value

def get_month_days(year, month):
    """
    Get the number of days in a given month and year.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        # Leap year check
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 0

def work_times():
    rsd_year = get_user_input("Enter current\n year:", 2024, 2100)
    rsd_month = get_user_input("Enter current\n month (1-12):", 1, 12)
    rsd_days_in_month = get_month_days(rsd_year, rsd_month)
    rsd_day = get_user_input("Enter current\n day (1-{}):".format(rsd_days_in_month), 1, rsd_days_in_month)
    rsd_hour = get_user_input("Enter current\n hour (1-24):", 1, 24)
    rsd_min = get_user_input("Enter current\n minute (0-59):", 0, 59)
    rsd = [rsd_year,rsd_month,rsd_day,rsd_hour,rsd_min]

    # Phase 1: Choose the number of time stamps (limit between 1 and 99)
    aots = get_user_input("How many time\nstamps do you want:", 1, 99)

    # Initialize an empty dictionary to store time stamps
    timestamps = {}

    # Phase 2: Choose the year (limit between 2024 and 2100)
    year = get_user_input("Enter the\n year:", 2024, 2100)
    print(year)

    # Phase 3: Choose the month (limited between 1 and 12)
    month = get_user_input("Enter the\n month (1-12):", 1, 12)
    print(month)
    # Phase 4: Choose the day (limited between 1 and the number of days in the chosen month)
    days_in_month = get_month_days(year, month)
    day = get_user_input("Enter the\n day (1-{}):".format(days_in_month), 1, days_in_month)
    print(day)

    # Phase 5: Choose the starting hour (limited between 1 and 24)
    start_hour = get_user_input("Enter the starting\n hour (1-24):", 1, 24)
    print(start_hour)
    # Phase 6: Choose the starting minute (limited between 0 and 59)
    start_min = get_user_input("Enter the starting\n minute (0-59):", 0, 59)
    print(start_min)
    # Phase 7: Choose the ending hour (limited between 1 and 24)
    end_hour = get_user_input("Enter the ending\n hour (1-24):", 1, 24)

    print(end_hour)
    # Phase 8: Choose the ending minute (limited between 0 and 59)
    end_min = get_user_input("Enter the ending\n minute (0-59):", 0, 59)
    print(end_min)
    # Create start_date and end_date strings
    start_date = [year, month, day, start_hour, start_min]
    end_date = [year, month, day, end_hour, end_min]
    print(start_date)
    print(end_date)

    # Check if start_date is before end_date
    try:
        if (start_hour < end_hour) or ((start_hour == end_hour) and (start_min < end_min)) :
            # Store the time stamps in the dictionary
            timestamps[aots] = [start_date, end_date]
            print("Time stamps:")
            for key, value in timestamps.items():
                print("{}: {}".format(key, value))
            Parameters.tstamps = timestamps
            Parameters.ctime = rsd
            wtii(rsd,timestamps)
        else:
            print("Invalid time range. Start date must be before end date.")
    except ValueError:
        print("Invalid date format. Please enter a valid date and time.")


# def tempfunc():
#     zonecords = {
#                 0:-200,
#                 1:0,
#                 2:0,
#                 3:0
#                 }
#     print(zonecords)
#     abso = {key: abs(value) for key, value in zonecords.items()}
#     fartkey = max(abso, key=abso.get)
#     highest = zonecords[fartkey]
#     #print("Key with farthest value from 0:", farthest_key)
#     print("highest in the room: ", highest)
#     bigGear = 40
#     smallGear = 8
#     multiplyAngle = -(bigGear/smallGear)

#     weHaveHeight[0] = abs((abs(highest) + packageheight)/multiplyAngle)
#     print("weHaveHeight[0] =",weHaveHeight[0])
#     return 0
                             

#stop till False
#reset till True


def zone_hight():
    zonenum = [1,2,3,4, "done?"]
    zonecords = {
                 0:0,
                 1:0,
                 2:0,
                 3:0
                 }
    #rotationMotor.reset_angle(0)
    #elevationMotor.reset_angle(0) 
    current_index=0
    verangle = 0
    temp=True
    anothertemp = False
    # for num in zonenum:
    #     temp=True
    #     ev3.screen.clear()
    #     ev3.screen.print("chose the location \n of zone: ",num)
    ev3.screen.clear()
    ev3.screen.print(zonenum)
    ev3.screen.print("set hight for zone\n"+ str(zonenum[current_index])+"?\n")
    while temp:
        buttons = ev3.buttons.pressed()
        wait(250)  
        for button in buttons:
            print(button, "in", buttons)
            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(zonenum)
                ev3.screen.print("set hight for zone\n"+ str(zonenum[current_index])+"?\n")
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(zonenum)
                ev3.screen.print("set higt for zone\n"+str(zonenum[current_index])+"?\n")

            elif str(button) == "Button.CENTER":
                if zonenum[current_index % len(zonenum)] == "done?":
                    temp = False
                    abso = {key: abs(value) for key, value in zonecords.items()}
                    fartkey = max(abso, key=abso.get)
                    highest = zonecords[fartkey]
                    #print("Key with farthest value from 0:", farthest_key)
                    print("highest in the room: ", highest)
                    bigGear = 40
                    smallGear = 8
                    multiplyAngle = -(bigGear/smallGear)
                    weHaveHeight[0] = abs((abs(highest) + packageheight)/multiplyAngle)
                    print(weHaveHeight[0])
                    print(zonecords)
                    ev3.speaker.beep()
                    ev3.screen.print("back!")
                    ev3.speaker.beep()
                    ev3.screen.clear()
                    return zonecords
                else:
                    anothertemp = True
                    ev3.screen.print("changing hight for: \n" + str(zonenum[current_index % len(zonenum)]))
            while anothertemp == True:
                buttons = []
                buttons = ev3.buttons.pressed()
                for button in buttons:
                    wait(100)
                    button_str = str(button)
                    if button_str == "Button.UP":
                        elevationMotor.run_angle(60,-10)
                    if button_str == "Button.DOWN":
                        elevationMotor.run_angle(60,10)
                    if button_str == "Button.LEFT":
                        rotationMotor.run_angle(60,-10)
                    if button_str == "Button.RIGHT":
                        rotationMotor.run_angle(60,10)

                    if button_str == "Button.CENTER":
                        ev3.speaker.beep()
                        verangle = elevationMotor.angle()
                        zonecords[zonenum[current_index % len(zonenum)] - 1] = verangle 
                        ev3.screen.print("you chose: " + str(zonenum[current_index% len(zonenum)]) +  "\n")
                        ev3.screen.print("to zone: " + str(verangle) +  "\n")
                        wait(550)
                        ev3.screen.clear()
                        ev3.screen.print("set hight for zone\n"+ str(zonenum[current_index])+"?\n")
                        print(zonecords)
                        anothertemp=False
                        # if num == :
                        #     ev3.speaker.beep()
                        #     ev3.screen.clear()
                        #     ev3.screen.print("done!")
                        #     ev3.speaker.beep()
                        #     return zonecords
                        

def set_origin():
    temp=True

    while temp:
        wait(250)
        buttons = ev3.buttons.pressed()
        speed = 10
        for button in buttons:
            combos = [str(obj) for obj in buttons]
            button_str = str(button)
            if button_str == "Button.UP":
                speed += 5
                elevationMotor.run_angle(60 + speed,-10)
            if button_str == "Button.DOWN":
                speed += 5
                elevationMotor.run_angle(60 + speed,10)
            elif button_str == "Button.CENTER":
                ev3.speaker.beep()
                wait(450) 
                ev3.speaker.beep()
                verangle = elevationMotor.angle()
                bigGear = 40
                smallGear = 8
                multiplyAngle = -(bigGear/smallGear)
                # Check if we are coming from Emenu or at startup.
                if Estop[0] == False:
                    elevationMotor.reset_angle(40 * multiplyAngle)
                    ev3.screen.print("angle reseted")
                    return 0  # To go back to menu.
                else:    
                    ev3.screen.print("Finished")
                    return 0 #Back to Emenu.
            if button_str == "Button.LEFT":
                speed += 5
                rotationMotor.run_angle(60 + speed,-10)
            if button_str == "Button.RIGHT":
                speed += 5
                rotationMotor.run_angle(60 + speed,10) 
            if combos == ["Button.RIGHT", "Button.LEFT"] or combos == ["Button.LEFT", "Button.RIGHT"] :
                clawMotor.run_angle(10,-10)
            if combos == ["Button.UP", "Button.DOWN"] or combos == ["Button.DOWN", "Button.UP"] :
                clawMotor.run_angle(60,-10) 

def colorzones():
    global zoneSort
    counter = 0
    colors = ["Red","Yellow", "Green","Blue", "pickup", "coms", "belt"]
    current_index=0
    temp = True
    ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
        theend = 5
        if len(colors) in {1,2,3}: #counter == 4:    #len(colors) in {1, 2}:
            for i in colors:
                ev3.screen.clear()
                ev3.screen.print("processing...")
                theend += 1 
                zoneSort[i] = theend
                ev3.speaker.beep()
            ev3.screen.clear()
            ev3.screen.print("done!")
            ev3.speaker.beep()
            temp = False
            #keys_to_keep = list(zoneSort.keys())[:-3]
            sorted_items = sorted(zoneSort.items(), key=lambda x: x[1]) # sorts based on number
            sorted_items = sorted_items[:-3] # cuts so only 4 left
            zoneSort = dict(sorted_items)
            print("THE NEW DICT: "+ str(zoneSort))                
            return zoneSort
        for button in buttons:

            #elif len(colors) == 0:

            if str(button) == "Button.LEFT":
                ev3.screen.clear()
                current_index = (current_index + 1) % len(colors)
                ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
            
            if str(button) == "Button.RIGHT":
                ev3.screen.clear()
                current_index = (current_index - 1) % len(colors)
                ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
            
            if str(button) == "Button.CENTER":
                counter += 1
                ev3.screen.clear()
                chosen = colors.pop(current_index % len(colors)) 
                print("popped:", chosen, "zone:", counter)
                zoneSort[chosen] = counter - 1
                ev3.speaker.beep()
                ev3.screen.print("you chose: " + str(chosen) +  "\n")
                ev3.screen.print("to zone: " + str(counter) +  "\n")
                wait(500)
                ev3.screen.clear()
                ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index % len(colors)])
                #chosen_zone = zoneSort[chosen.lower()] 
                #ev3.screen.print("you chose ",choicelist[current_index])
                #temp=False

            
###


if __name__ =="__main__":
    menu()
#menu()