
# Axes = [7, 8]
# IOOutputs = [3.1]

# Initialize API buffer
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer of the specified channel
Wmx3Lib_buf.Clear(0)

# Create a buffer for the specified channel
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)

# Start recording for the specified channel
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Move Axis 7 to position 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
Wmx3Lib_cm.motion.StartPos(posCommand)

# Wait for Axis 7 to stop
Wmx3Lib_buf.Wait(7)

# Move Axis 8 to position 180
posCommand.axis = 8
posCommand.target = 180
Wmx3Lib_cm.motion.StartPos(posCommand)

# Wait for Axis 8 to stop
Wmx3Lib_buf.Wait(8)

# Linearly interpolate Axis 7 and 8 to (191, 222)
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
Wmx3Lib_cm.motion.StartLinearIntplPos(lin)

# Wait for the linear interpolation to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
Wmx3Lib_cm.motion.Wait_AxisSel(axes)

# Execute a trapezoidal profile type cubic spline for Axis 7 and Axis 8
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)

# Create the spline channel buffer
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
spl = AdvMotion_ProfileSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 7)
spl.SetAxis(1, 8)
spl.profile = Profile()
spl.profile.type = ProfileType.Trapezoidal
spl.profile.velocity = 1600
spl.profile.acc = 10000
spl.profile.dec = 10000

pt = []

pt.append(AdvMotion_SplinePoint())
pt[0].SetPos(0, 0)
pt[0].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[1].SetPos(0, 25)
pt[1].SetPos(1, -50)

pt.append(AdvMotion_SplinePoint())
pt[2].SetPos(0, 50)
pt[2].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[3].SetPos(0, 75)
pt[3].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[4].SetPos(0, 100)
pt[4].SetPos(1, 0)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_Profile error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Free the spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far
Wmx3Lib_buf.Execute(0)

# Set IO output bit 3.1 to 1, wait 0.2 seconds, then set it to 0, repeating this cycle 5 times
Wmx3Lib_Io = Io(Wmx3Lib)
for _ in range(5):
    ret = Wmx3Lib_Io.SetOutBit(0x03, 0x01, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    sleep(0.2)
    ret = Wmx3Lib_Io.SetOutBit(0x03, 0x01, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    sleep(0.2)
