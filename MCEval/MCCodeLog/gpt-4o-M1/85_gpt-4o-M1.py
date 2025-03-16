
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Initialize API buffer and condition
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
# Start recording for the specified channel
Wmx3Lib_buf.StartRecordBufferChannel(0)

lin = Motion_LinearIntplCommand()

# First linear interpolation (0, 0) -> (100, 0)
lin.axisCount = 2
lin.SetAxis(0, 3)
lin.SetAxis(1, 6)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 100)
lin.SetTarget(1, 0)

# Execute interpolation command to move to a specified absolute position
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the first linear interpolation starts deceleration
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Second linear interpolation (100, 0) -> (100, 100)
lin.SetTarget(0, 100)
lin.SetTarget(1, 100)
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the second linear interpolation starts deceleration
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Third linear interpolation (100, 100) -> (0, 100)
lin.SetTarget(0, 0)
lin.SetTarget(1, 100)
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the third linear interpolation starts deceleration
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Fourth linear interpolation (0, 100) -> (0, 0)
lin.SetTarget(0, 0)
lin.SetTarget(1, 0)
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far
Wmx3Lib_buf.Execute(0)

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 3)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Destroy API buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
