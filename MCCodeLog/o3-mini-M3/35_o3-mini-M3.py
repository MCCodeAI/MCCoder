
# Axes = [1, 5]
# IOInputs = []
# IOOutputs = []

# Create an absolute motion command for Axis 1 that moves it to -110.
posCommandAxis1 = Motion_PosCommand()
posCommandAxis1.profile.type = ProfileType.Trapezoidal
posCommandAxis1.axis = 1
posCommandAxis1.target = -110
posCommandAxis1.profile.velocity = 1000
posCommandAxis1.profile.acc = 10000
posCommandAxis1.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommandAxis1)
if ret != 0:
    print('StartPos error (Axis 1) code ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Do not wait here because the motion of Axis 1 should continue uninterrupted.
# Instead, we set up a triggered absolute motion command for Axis 5.
tgrPosCommand = Motion_TriggerPosCommand()
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 5
tgrPosCommand.target = -100
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create a Trigger that monitors Axis 1.
trigger = Trigger()
trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 30  # Trigger when Axis 1 is within 30 units of its target

tgrPosCommand.trigger = trigger

# Start the triggered absolute position command for Axis 5.
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error (Axis 5) code ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until both Axis 1 and Axis 5 have stopped moving.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)  # Selecting Axis 1
axisSel.SetAxis(1, 5)  # Selecting Axis 5

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
