
# -*- coding: utf-8 -*-

# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# The following code monitors when Axis 3's remaining distance to its target becomes 500.
# When that condition is met, it moves Axis 1 to position -200 at a speed of 1000,
# waits for Axis 1 to finish moving, and then commands Axis 3 to move to position 1200.
#
# Note: Polling is used to wait for the event condition, and after each motion, the script
# waits for the axis to stop before issuing the next command.
#
# Step 1: Configure the event input for Axis 3.
eventIN_Motion = CoreMotionEventInput()  # Create an event input object
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 3
eventIN_Motion.distanceToTarget.distance = 500
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Removed erroneous call to Wmx3Lib_cm.motion.SetEventInput(eventIN_Motion)
# This function does not exist in the Motion object. Instead, the code uses polling to
# detect when the event condition is met.

import time
# Poll until the event condition is met (i.e., when Axis 3's remaining distance equals 500)
while True:
    if Wmx3Lib_cm.motion.CheckEventStatus(3):
        break
    time.sleep(0.1)

# Step 2: Once the event is triggered, move Axis 1 to position -200 with a speed (velocity) of 1000.
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 1
posCommand1.target = -200
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print("StartPos error code for Axis 1: " + str(ret))
    exit(1)

# Wait until Axis 1 finishes moving.
Wmx3Lib_cm.motion.Wait(1)

# Step 3: Move Axis 3 to the position 1200.
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 3
posCommand3.target = 1200
posCommand3.profile.velocity = 1000
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print("StartPos error code for Axis 3: " + str(ret))
    exit(1)

# Wait until Axis 3 finishes moving.
Wmx3Lib_cm.motion.Wait(3)
