
# Axes = [2, 1]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 2
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 2000
posCommand.profile.velocity = 1000  # Default velocity
posCommand.profile.acc = 10000      # Default acceleration
posCommand.profile.dec = 10000      # Default deceleration

# Execute the position command for Axis 2
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 to start moving
Wmx3Lib_cm.motion.Wait(2)

# Create event input for monitoring RemainingTime of Axis 2
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Create a position command for Axis 1
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 500
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the position command for Axis 1 after the RemainingTime condition is met
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to complete their movements
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
