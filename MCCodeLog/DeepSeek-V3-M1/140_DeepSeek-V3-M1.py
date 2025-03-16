
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Set the input event to monitor if the DistanceToTarget of Axis 3's movement is 500
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 3
eventIN_Motion.distanceToTarget.distance = 500
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Move Axis 3 to 1200
posCommand_Axis3 = Motion_PosCommand()
posCommand_Axis3.profile.type = ProfileType.Trapezoidal
posCommand_Axis3.axis = 3
posCommand_Axis3.target = 1200
posCommand_Axis3.profile.velocity = 1000
posCommand_Axis3.profile.acc = 10000
posCommand_Axis3.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis3)
if ret != 0:
    print('StartPos error code for Axis 3 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the event to trigger (DistanceToTarget of Axis 3 is 500)
while not eventIN_Motion.IsTriggered():
    pass

# Move Axis 1 to the position -200 at a speed of 1000
posCommand_Axis1 = Motion_PosCommand()
posCommand_Axis1.profile.type = ProfileType.Trapezoidal
posCommand_Axis1.axis = 1
posCommand_Axis1.target = -200
posCommand_Axis1.profile.velocity = 1000
posCommand_Axis1.profile.acc = 10000
posCommand_Axis1.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis1)
if ret != 0:
    print('StartPos error code for Axis 1 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
