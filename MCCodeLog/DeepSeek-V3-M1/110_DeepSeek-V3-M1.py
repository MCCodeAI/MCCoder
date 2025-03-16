
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = [3.1]

# Record and execute an API buffer
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Move Axis 7 to position 150 and Axis 8 to position 180
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 7
posCommand1.target = 150
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.Trapezoidal
posCommand2.axis = 8
posCommand2.target = 180
posCommand2.profile.velocity = 1000
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.StartPos(posCommand2)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# Linearly interpolate Axis 7 and 8 to (191, 222) at a velocity of 1000 with acceleration and deceleration of 10000
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

# Execute interpolation command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# Execute a trapezoidal profile type cubic spline for Axis 7 and Axis 8 with the points (0, 0), (25, -50), (50, 0), (75, 50), and (100, 0) at a velocity of 1600
spline = Motion_SplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 7)
spline.SetAxis(1, 8)
spline.profile.type = ProfileType.Trapezoidal
spline.profile.velocity = 1600
spline.profile.acc = 10000
spline.profile.dec = 10000
spline.numPoints = 5
spline.SetPoint(0, 0, 0)
spline.SetPoint(1, 25, -50)
spline.SetPoint(2, 50, 0)
spline.SetPoint(3, 75, 50)
spline.SetPoint(4, 100, 0)

# Execute spline command
ret = Wmx3Lib_cm.motion.StartSpline(spline)
if ret != 0:
    print('StartSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# Set IO output bit 3.1 to 1, wait 0.2 seconds, then set it to 0, repeating this cycle 5 times
for i in range(5):
    Wmx3Lib_io.SetOutputBit(3, 1, 1)
    sleep(0.2)
    Wmx3Lib_io.SetOutputBit(3, 1, 0)
    sleep(0.2)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
