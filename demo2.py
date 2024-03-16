import time
from flyt_python import api

drone = api.navigation(timeout=120000)

print "Current position: initial position of triangle trajectory"
print "Move the drone in a triangle trajectory of side length 10m at a height of 10m"
print "Taking off till 10 m"
drone.take_off(10.0)
print "Moving to point 2 of the triangle"
drone.position_set(8.0, 6.0, 10, relative=True)
print "Moving to point 3 of the triangle"
drone.position_set(-8.0, 6.0, 0, relative=True)
print "Moving back to point 1 of the triangle"
drone.position_set(0, -10, 0, relative=True)
print "Drone Landing"
drone.land(async=False)
print "Shutdown instance"
drone.disconnect()