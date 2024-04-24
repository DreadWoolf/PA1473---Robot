#!/usr/bin/env pybricks-micropython
from Parameters import *


def menu():
    #global Estop
    #global restart
    #Estop = False
    #restart = False
    choicelist = ["start_code", "set_origin","zonecolor_selection","zone_hight"]
    current_index=0
    temp=True
    zonecords = 0
    czones = 0
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
                    zonecords = zone_hight()
                    print(zonecords)
                if choicelist[current_index] == "set_origin":
                    origin = set_origin()
                    print(origin)
                if choicelist[current_index] == "zonecolor_selection":
                    czones=colorzones()
                    print(czones)
                if choicelist[current_index] == "start_code":
                    return czones , zonecords
                # if choicelist[current_index] == "EMERGENCY" and Estop:
                #     return 0

def Emenu():
    #global Estop
    #global restart
    Estop = False
    restart = False
    Echoicelist = ["restart","resume","manual"]
    current_index=0
    temp=True
    zonecords = 0
    czones = 0
    ev3.screen.print(Echoicelist[current_index])

    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)

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
                ev3.screen.clear()
                ev3.screen.print("you chose ",Echoicelist[current_index])
                if Echoicelist[current_index] == "restart":
                    restart = True

                if Echoicelist[current_index] == "resume":
                    Estop = False

                if Echoicelist[current_index] == "manual":
                    set_origin()

                            #get out of here
                            #break
                            #  wait(1000)


                            #### needs to båe imporved#######################3
                            ######################################3
                            #########################3                    

#stop till False
#reset till True


def zone_hight():
    zonenum = [1,2,3]
    zonecords = {
                 0:0,
                 1:0,
                 2:0,
                 3:0
                 }
    #rotationMotor.reset_angle(0)
    #elevationMotor.reset_angle(0)
    horangle = 0 
    verangle = 0
    temp=True
    for num in zonenum:
        temp=True
        ev3.screen.clear()
        ev3.screen.print("chose the location \n of zone: ",num)
        while temp:
            buttons = ev3.buttons.pressed()
            wait(250)
            for button in buttons:
                button_str = str(button)
                if button_str == "Button.UP":
                    elevationMotor.run_angle(60,-10)
                if button_str == "Button.DOWN":
                    elevationMotor.run_angle(60,10)
                elif button_str == "Button.CENTER":
                    horangle = rotationMotor.angle() 
                    verangle = elevationMotor.angle()
                    zonecords[num] = verangle
                    if num == 3:
                        return zonecords
                    temp=False
                if button_str == "Button.LEFT":
                    rotationMotor.run_angle(60,-10)
                if button_str == "Button.RIGHT":
                    rotationMotor.run_angle(60,10)

def set_origin():
    temp=True
    while temp:
        buttons = ev3.buttons.pressed()
        wait(250)
        for button in buttons:
            combos = [str(obj) for obj in buttons]
            button_str = str(button)
            if button_str == "Button.UP":
                elevationMotor.run_angle(60,-10)
            if button_str == "Button.DOWN":
                elevationMotor.run_angle(60,10)
            elif button_str == "Button.CENTER": 
                verangle = elevationMotor.angle()
                bigGear = 40
                smallGear = 8
                multiplyAngle = -(bigGear/smallGear)
                elevationMotor.reset_angle(40 * multiplyAngle)
                return 0
            if button_str == "Button.LEFT":
                rotationMotor.run_angle(60,-10)
            if button_str == "Button.RIGHT":
                rotationMotor.run_angle(60,10) 
            if combos == ["Button.RIGHT", "Button.LEFT"] or combos == ["Button.LEFT", "Button.RIGHT"] :
                clawMotor.run_angle(10,-10)
            if combos == ["Button.UP", "Button.DOWN"] or combos == ["Button.DOWN", "Button.UP"] :
                clawMotor.run_until_stalled(40, then=Stop.BRAKE, duty_limit=None) 

def colorzones():
    global zoneSort
    # zoneSort = {
    # 'Red'       : 0,
    # 'Green'     : 1,
    # 'Blue'      : 2,
    # 'Yellow'   : 3
    # }    
    counter = 0
    colors = ["Red","Yellow", "Green","Blue", "pick1", "pick2"]
    current_index=0
    temp = True
    ev3.screen.print("set color for zone\n"+"nr"+str(counter+1)+"\n"+colors[current_index])
    while temp:
        buttons= ev3.buttons.pressed()
        wait(250)
        for button in buttons:

            if len(colors) == 0:
                ev3.screen.print("done!")
                temp = False
                keys_to_keep = list(zoneSort.keys())[:-2]
                sorted_items = sorted(zoneSort.items(), key=lambda x: x[1])
                sorted_items = sorted_items[:-2]
                new_dict = dict(sorted_items)
                print("THE NEW DICK: "+ str(new_dict))                
                return new_dict
            
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
                print("Colors:", colors)
                print("popped:", chosen)
                zoneSort[chosen.lower()] = str(counter)
                #chosen_zone = zoneSort[chosen.lower()] 
                #ev3.screen.print("you chose ",choicelist[current_index])
                #temp=False
            print(zoneSort)
            



if __name__ =="__main__":
    menu()
#menu()