
# Axes = [1, 3]
# Inputs = []
# Outputs = []

# Set the input event to monitor if the DistanceToTarget of Axis 3's movement is 500
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 3
eventIN_Motion.distanceToTarget.distance = 500
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Move Axis 1 to the position -200 at a speed of 1000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = -200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 1
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to stop moving
Wmx3Lib_cm.motion.Wait(1)

# Move Axis 3 to 1200
posCommand.axis = 3
posCommand.target = 1200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 3
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 to stop moving
Wmx3Lib_cm.motion.Wait(3)
