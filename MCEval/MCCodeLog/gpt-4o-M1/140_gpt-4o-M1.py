
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Set the input event to monitor if the DistanceToTarget of Axis 3's movement is 500
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 3
eventIN_Motion.distanceToTarget.distance = 500
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Move Axis 1 to the position -200 at a speed of 1000
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 1
posCommand1.target = -200
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

# Execute command to move Axis 1
ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to stop moving
Wmx3Lib_cm.motion.Wait(1)

# Move Axis 3 to 1200
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 3
posCommand3.target = 1200
posCommand3.profile.velocity = 1000
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

# Execute command to move Axis 3
ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 to stop moving
Wmx3Lib_cm.motion.Wait(3)
