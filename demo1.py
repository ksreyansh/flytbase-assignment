import time
from flyt_python import api

drone = api.navigation(timeout=120000)

drone.take_off(5.0)
print("1. Taking Off till height of 5m")
drone.take_off(5.0)

print("Current position: Initial position of the square")
print("Move the drone in side length 6.5m at a height of 5m")
print("Moving to 2nd point of the square")
drone.position_set(6.5, 0, 0, relative=True)
print("Moving to 3rd point of the square")
drone.position_set(0, 6.5, 0, relative=True)
print("Moving to 4th point of the square")
drone.position_set(-6.5, 0, 0, relative=True)
print("Moving back to 1st point of the square")
drone.position_set(0, -6.5, 0, relative=True)
print("Landing")
drone.land(async=False)

# Disconnect the drone
drone.disconnect()