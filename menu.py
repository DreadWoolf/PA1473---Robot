from Parameters import *

def menu():
    choicelist = ["start_code","zonecolor_selection", "zone_hight", "set_origin"]
    current_index=0
    temp=True
    
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
                if choicelist[current_index] == "zone_hight":
                    zonecords = zone_hight()
                    print(zonecords)
                if choicelist[current_index] == "set_origin":
                    origin = set_origin()
                    print(origin)

def zone_hight():
    zonenum = [1,2,3]
    zonecords = {"1":[],
                 "2":[],
                 "3":[]
                 }
    rotationMotor.reset_angle(0)
    elevationMotor.reset_angle(0)
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
                    zonecords[str(num)] =[horangle,verangle]
                    if num == 3:
                        return zonecords
                    temp=False
                if button_str == "Button.LEFT":
                    rotationMotor.run_angle(60,-10)
                if button_str == "Button.RIGHT":
                    rotationMotor.run_angle(60,10)
def set_origin():
    origin=[]
    temp=True
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
                origin = [horangle,verangle]
                return origin
            if button_str == "Button.LEFT":
                rotationMotor.run_angle(60,-10)
            if button_str == "Button.RIGHT":
                rotationMotor.run_angle(60,10)
