
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Create an API buffer object and condition object.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear any previous recordings and configure the buffer.
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Create a linear interpolation command for two axes.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 3)  # Assign Axis 3
lin.SetAxis(1, 6)  # Assign Axis 6
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# ---------------------------
# First segment: move to (100, 0)
lin.SetTarget(0, 100)  # Axis 3 -> 100
lin.SetTarget(1, 0)    # Axis 6 -> 0

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the motion starts deceleration on Axis 3
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# ---------------------------
# Second segment: move to (100, 100)
lin.SetTarget(0, 100)  # Axis 3 remains at 100
lin.SetTarget(1, 100)  # Axis 6 moves to 100

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until deceleration starts
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# ---------------------------
# Third segment: move to (0, 100)
lin.SetTarget(0, 0)    # Axis 3 moves to 0
lin.SetTarget(1, 100)  # Axis 6 remains at 100

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until deceleration starts
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 3
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# ---------------------------
# Fourth segment: move to (0, 0)
lin.SetTarget(0, 0)  # Axis 3 remains at 0
lin.SetTarget(1, 0)  # Axis 6 moves to 0

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End the recording and execute the API buffer
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for both axes to complete their motion.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 3)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Clean up the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
