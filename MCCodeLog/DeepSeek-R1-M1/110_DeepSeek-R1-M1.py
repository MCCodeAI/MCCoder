
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = [3.1]

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# 1. Move Axis 7 to position 150 and Axis 8 to position 180
posCommand7 = Motion_PosCommand()
posCommand7.profile.type = ProfileType.Trapezoidal
posCommand7.axis = 7
posCommand7.target = 150
posCommand7.profile.velocity = 1000
posCommand7.profile.acc = 10000
posCommand7.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand7)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand8 = Motion_PosCommand()
posCommand8.profile.type = ProfileType.Trapezoidal
posCommand8.axis = 8
posCommand8.target = 180
posCommand8.profile.velocity = 1000
posCommand8.profile.acc = 10000
posCommand8.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand8)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# 2. Linearly interpolate to (191, 222)
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 8)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 191)
lin.SetTarget(1, 222)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until linear interpolation starts deceleration
cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
cond.arg_decelerationStarted.axis = 7
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# 3. Execute cubic spline
spline = Motion_SplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 7)
spline.SetAxis(1, 8)
spline.profile.type = ProfileType.Trapezoidal
spline.profile.velocity = 1600
spline.profile.acc = 10000
spline.profile.dec = 10000

# Add spline points
spline.AddPoint(0, 0)
spline.AddPoint(25, -50)
spline.AddPoint(50, 0)
spline.AddPoint(75, 50)
spline.AddPoint(100, 0)

ret = Wmx3Lib_cm.motion.StartSplinePos(spline)
if ret != 0:
    print('StartSplinePos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until spline motion starts deceleration
cond.arg_decelerationStarted.axis = 7
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# 4. Set IO output 3.1 to 1, wait 0.2s, then set to 0 (repeat 5 times)
for _ in range(5):
    # Set output to 1
    Wmx3Lib.io.SetOutput(3, 1, 1)
    sleep(0.2)
    # Set output to 0
    Wmx3Lib.io.SetOutput(3, 1, 0)
    sleep(0.2)

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()
# Execute the buffer
Wmx3Lib_buf.Execute(0)

# Wait for motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Destroy buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
