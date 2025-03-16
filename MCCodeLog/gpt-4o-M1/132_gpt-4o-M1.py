
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to position 2000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 2000
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 2 to the specified position
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 to stop moving
Wmx3Lib_cm.motion.Wait(2)

# Set the input event to monitor the RemainingTime of Axis 2's movement is 1000ms
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Move Axis 1 to position 500 at a speed of 1000
posCommand.axis = 1
posCommand.target = 500
posCommand.profile.velocity = 1000

# Execute command to move Axis 1 to the specified position
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to stop moving
Wmx3Lib_cm.motion.Wait(1)
