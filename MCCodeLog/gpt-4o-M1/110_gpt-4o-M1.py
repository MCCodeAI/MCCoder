
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

# Move Axis 7 to position 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(7)

# Move Axis 8 to position 180
posCommand.axis = 8
posCommand.target = 180

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(8)

# Linear interpolation for Axis 7 and 8 to (191, 222)
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

# Wait for the linear interpolation to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute a trapezoidal profile type cubic spline for Axis 7 and Axis 8
spline = Motion_CubicSplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 7)
spline.SetAxis(1, 8)
spline.profile.type = ProfileType.Trapezoidal
spline.profile.velocity = 1600
spline.SetPoint(0, 0, 0)
spline.SetPoint(1, 25, -50)
spline.SetPoint(2, 50, 0)
spline.SetPoint(3, 75, 50)
spline.SetPoint(4, 100, 0)

ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
if ret != 0:
    print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the spline motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set IO output bit 3.1 to 1, wait 0.2 seconds, then set it to 0, repeating this cycle 5 times
for _ in range(5):
    Wmx3Lib_cm.io.SetOutputBit(3, 1, 1)
    sleep(0.2)
    Wmx3Lib_cm.io.SetOutputBit(3, 1, 0)
    sleep(0.2)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
