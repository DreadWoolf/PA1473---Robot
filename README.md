In this project we were instructed to program a robot to sort packages in a warehouse based on different properties. 
The robot have motors and sensors to make recognize, pick and place items. 

To set up the project you will need to install som important deppendencies to start developing. First and formost you will
need to install a coding edito, like VisualStudio, to be able to run the code. You will also need to use GitHub to acces our code and 
visualise it in  the code editor. Once you do so, you will need to install the ev3 brick extension on your code editor to be able
to run the code on the robot. Once you connect the robot with the usb-cable, you will be good to use the robot.

To make the project run, you will firstly need to set up the origin-position. It means that you will se the robotic arm at the hight and position 
that makes the height perfect for the sensor to see the color of the package. Then, you need to scroll the menu and look for zonecolor_selection and 
in this section you will be able to set up the diffrent zones for wich colors you want the robot to sort them to. you will also need to chose the pick
up zone from this section. Once you are done with all that, you are good to go. Scroll until you find "start_code" and press it. The robot will start
sroting packages based on their color. 

Features
- [ ] US_01: The robot shall locate, handle, and pick up items from a designated position without dropping them accidentally or harming the packages.
- [ ] REQ02: The robot should place packages at a designated position safely, gently, and reliably with reasonable speed.
- [ ] REQ03: The robot should be able to differentiate between workers and packages. As well, it should be able to find the packages in a designated pickup zone.
- [ ] REQ04: The robot should calibrate for a maximum of three different colours (except safety colour) and tell what colour the package is at a designated position.
- [ ] REQ05: The robot should safely, gently, and reliably place down the different items at designated drop-off zones based on the colour of the Item.
- [ ] REQ06: The robot should be able to pick up items from varying elevated positions within the limitations of the robot at designated pickup positions.
- [ ] REQ07: Robot should be able to warn and communicate by any viable method to prevent collision with forklifts and other robots.
- [ ] REQ08: Should periodically check the pickup location to see if new items have arrived at designated pickup positions.
- [ ] REQ09: The Robot should be able to sort items at specific times as required by the customer.
- [ ] REQ10: The customer should be able to manually set the locations and height of one pickup-zone and two drop-off zones.
- [ ] REQ11: There should be a reliable method to stop the robot in case of an emergency.
- [ ] US13: As a customer, I want to easily reprogram the pickup and drop off zone of the robot.
- [ ] US14: As a customer, I want to easily change the schedule of the robot pick up task
- [ ] US15: As a customer, I want to have an emergency stop button, that immediately terminates the operation of the robot safely.
- [ ] US16: As a customer, I want the robot to be able to pick an item up and put it in the designated drop-off location within 5 seconds
- [ ] Us17: As a customer, I want the robot to pick up items from a rolling belt and put them in the designated positions based on color and shape.
- [ ] US18: As a customer, I want to have a pause button that pauses the robot's operation when the button is pushed and then resumes the program from the same point when I push the button again.
- [ ] Us19: As a customer, I want a very nice dashboard to configure the robot program and start some tasks on demand.
