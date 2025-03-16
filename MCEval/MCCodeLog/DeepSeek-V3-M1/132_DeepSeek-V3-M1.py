
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

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 to stop moving
Wmx3Lib_cm.motion.Wait(2)

# Set the input event to monitor if the RemainingTime of Axis 2's movement is 1000ms
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Move Axis 1 to position 500 at a speed of 1000 when the RemainingTime condition is met
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 500
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the command when the RemainingTime condition is met
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to stop moving
Wmx3Lib_cm.motion.Wait(1)
