
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = [3.1]

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
Wmx3Lib_Io = Io(Wmx3Lib)

# Task 1: Record and execute an API buffer
# Clear and create buffer
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Move Axis 7 to 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(7)

# Move Axis 8 to 180
posCommand.axis = 8
posCommand.target = 180
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(8)

# End recording and execute
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for completion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)

# Task 2: Linear interpolation
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
Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# Task 3: Trapezoidal profile cubic spline
# Free and create spline buffer
Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)

spl = AdvMotion_ProfileSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 7)
spl.SetAxis(1, 8)
spl.profile.type = ProfileType.Trapezoidal
spl.profile.velocity = 1600
spl.profile.acc = 10000
spl.profile.dec = 10000

# Define spline points
points = [
    (0, 0),
    (25, -50),
    (50, 0),
    (75, 50),
    (100, 0)
]

pt = []
for i, (x, y) in enumerate(points):
    spline_point = AdvMotion_SplinePoint()
    spline_point.SetPos(0, x)
    spline_point.SetPos(1, y)
    pt.append(spline_point)

# Execute spline
Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, len(points), pt)
Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# Task 4: IO output cycling
for _ in range(5):
    # Set output bit 3.1 to 1
    Wmx3Lib_Io.SetOutBit(3, 1, 1)
    sleep(0.2)
    # Set output bit 3.1 to 0
    Wmx3Lib_Io.SetOutBit(3, 1, 0)
    sleep(0.2)

# Cleanup
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
