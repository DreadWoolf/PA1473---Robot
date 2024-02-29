class Robot:
    def __init__(self):
        self.zone_colors = {}  # Dictionary to store zone-color mappings

    def calibrate_zone_color(self, zone, color):
        self.zone_colors[zone] = color
        print(f"Zone {zone} calibrated with color {color}")

    def pick_up_package(self, package):
        color = self.detect_color(package)
        for zone, zone_color in self.zone_colors.items():
            if color == zone_color:
                print(f"Robot picked up package {package} from zone {zone}")
                return package
        print("Package doesn't match any calibrated zone color. Ignoring.")

    def move_to_zone(self, zone):
        print(f"Robot moved to zone {zone}")

    def drop_package(self, package, zone):
        print(f"Robot dropped package {package} in zone {zone}")

    def detect_color(self, package):
        # Simulated color detection
        return "Red"  # Replace with actual color detection logic


# Example usage
robot = Robot()

# Calibrating zones with colors
robot.calibrate_zone_color("Zone A", "Red")
robot.calibrate_zone_color("Zone B", "Blue")

# Picking up packages from zones and dropping them in target zones
package1 = "Package with Red Color"
picked_package = robot.pick_up_package(package1)
if picked_package:
    robot.move_to_zone("Zone A")
    robot.drop_package(picked_package, "Zone A")

package2 = "Package with Green Color"
picked_package = robot.pick_up_package(package2)
if picked_package:
    robot.move_to_zone("Zone B")
    robot.drop_package(picked_package, "Zone B")


zones = {
    1: 'Red',
    2: 'blue'
}

