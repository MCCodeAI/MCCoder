
# Axes = [0, 1]
# Inputs = []
# Outputs = []

# Set the input event to monitor if the RemainingDistance of Axis 0's movement is 1000
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
eventIN_Motion.remainingDistance.axis = 0
eventIN_Motion.remainingDistance.distance = 1000
eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

# Move Axis 1 to the position 800 at a speed of 1000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 800
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

# Move Axis 0 to 2000
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 0
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 0 to stop moving
Wmx3Lib_cm.motion.Wait(0)
