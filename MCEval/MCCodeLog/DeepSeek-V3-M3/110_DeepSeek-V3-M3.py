
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = [3.1]

# Record and execute an API buffer
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Move Axis 7 to position 150 and Axis 8 to position 180
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(7)

posCommand.axis = 8
posCommand.target = 180
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(8)

# Linearly interpolate Axis 7 and 8 to (191, 222) at a velocity of 1000
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
Wmx3Lib_buf.Wait(7)
Wmx3Lib_buf.Wait(8)

# Execute a trapezoidal profile type cubic spline for Axis 7 and 8
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

spline = AdvMotion_ProfileSplineCommand()
spline.dimensionCount = 2
spline.SetAxis(0, 7)
spline.SetAxis(1, 8)
spline.profile.type = ProfileType.Trapezoidal
spline.profile.velocity = 1600
spline.profile.acc = 10000
spline.profile.dec = 10000

points = [
    (0, 0),
    (25, -50),
    (50, 0),
    (75, 50),
    (100, 0)
]

pt = []
for i, (x, y) in enumerate(points):
    pt.append(AdvMotion_SplinePoint())
    pt[i].SetPos(0, x)
    pt[i].SetPos(1, y)

ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spline, len(points), pt)
if ret != 0:
    print('StartCSplinePos_Profile error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

Wmx3Lib_buf.Wait(7)
Wmx3Lib_buf.Wait(8)

# Set IO output bit 3.1 to 1, wait 0.2 seconds, then set it to 0, repeating this cycle 5 times
Wmx3Lib_Io = Io(Wmx3Lib)
for _ in range(5):
    ret = Wmx3Lib_Io.SetOutBit(3, 1, 1)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    sleep(0.2)
    ret = Wmx3Lib_Io.SetOutBit(3, 1, 0)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    sleep(0.2)

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Destroy API buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
