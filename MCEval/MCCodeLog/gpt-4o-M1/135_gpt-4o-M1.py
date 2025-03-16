
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = []

# Set the input event to monitor if the CompletedTime of Axis 3's movement is 300ms
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.CompletedTime
eventIN_Motion.completedTime.axis = 3
eventIN_Motion.completedTime.timeMilliseconds = 300
eventIN_Motion.completedTime.disableIdleAxisTrigger = 1

# Move Axis 1 to the position 300 at a speed of 1000
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 1
posCommand1.target = 300
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

# Move Axis 3 and 2 to 2000
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 3
posCommand3.target = 2000
posCommand3.profile.velocity = 1000
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.Trapezoidal
posCommand2.axis = 2
posCommand2.target = 2000
posCommand2.profile.velocity = 1000
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000

# Execute command to move Axis 3
ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute command to move Axis 2
ret = Wmx3Lib_cm.motion.StartPos(posCommand2)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 and 2 to stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
