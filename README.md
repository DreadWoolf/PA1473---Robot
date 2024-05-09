In this project, we were tasked with programming a robot to sort packages in a warehouse based on various properties. The robot is equipped with motors and sensors to recognize, pick, and place items.

To set up the project, you will need to install some important dependencies to begin development. Firstly, you'll need to install a coding editor such as Visual Studio to run the code. Additionally, you'll need to use GitHub to access our code and visualize it in the code editor. Once this is done, you'll need to install the EV3 Brick extension on your code editor to enable running the code on the robot. After connecting the robot with the USB cable, you'll be ready to use it.

To initiate the project, you'll first need to establish the origin position. This involves positioning the robotic arm at the correct height and orientation for the sensor to accurately detect the color of the package. Next, navigate the menu to locate the "zone color selection" section. Here, you can define the different zones for sorting packages by color and select the pickup zone. Once you've completed these steps, you're ready to proceed. Scroll until you find the "start code" option and press it. The robot will begin sorting packages based on their color.

Features
- [x] US_01: The robot shall locate, handle, and pick up items from a designated position without dropping them accidentally or harming the packages.
- [x] REQ02: The robot should place packages at a designated position safely, gently, and reliably with reasonable speed.
- [x] REQ03: The robot should be able to differentiate between workers and packages. As well, it should be able to find the packages in a designated pickup zone.
- [x] REQ04: The robot should calibrate for a maximum of three different colours (except safety colour) and tell what colour the package is at a designated position.
- [x] REQ05: The robot should safely, gently, and reliably place down the different items at designated drop-off zones based on the colour of the Item.
- [x] REQ06: The robot should be able to pick up items from varying elevated positions within the limitations of the robot at designated pickup positions.
- [x] REQ07: Robot should be able to warn and communicate by any viable method to prevent collision with forklifts and other robots.
- [x] REQ08: Should periodically check the pickup location to see if new items have arrived at designated pickup positions.
- [ ] REQ09: The Robot should be able to sort items at specific times as required by the customer.
- [x] REQ10: The customer should be able to manually set the locations and height of one pickup-zone and two drop-off zones.
- [x] REQ11: There should be a reliable method to stop the robot in case of an emergency.
- [x] US13: As a customer, I want to easily reprogram the pickup and drop off zone of the robot.
- [x] US14: As a customer, I want to easily change the schedule of the robot pick up task
- [x] US15: As a customer, I want to have an emergency stop button, that immediately terminates the operation of the robot safely.
- [x] US16: As a customer, I want the robot to be able to pick an item up and put it in the designated drop-off location within 5 seconds
- [x] Us17: As a customer, I want the robot to pick up items from a rolling belt and put them in the designated positions based on color and shape.
- [x] US18: As a customer, I want to have a pause button that pauses the robot's operation when the button is pushed and then resumes the program from the same point when I push the button again.
- [x] Us19: As a customer, I want a very nice dashboard to configure the robot program and start some tasks on demand.
