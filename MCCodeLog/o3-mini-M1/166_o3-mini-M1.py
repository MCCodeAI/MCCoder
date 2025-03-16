
# Axes = [1, 3, 8, 9]
# IOInputs = []
# IOOutputs = []

# --- Execute a PVT command for Axis 1 with 6 points ---
pvt = Motion_PVTCommand()
pvt.axis = 1
pvt.pointCount = 6

# Define PVT points: (Position, Velocity, Time)
pvtPoint = Motion_PVTPoint()

# Point 0: (0, 0, 0)
pvtPoint.pos = 0
pvtPoint.velocity = 0
pvtPoint.timeMilliseconds = 0
pvt.SetPoints(0, pvtPoint)

# Point 1: (50, 1000, 100)
pvtPoint.pos = 50
pvtPoint.velocity = 1000
pvtPoint.timeMilliseconds = 100
pvt.SetPoints(1, pvtPoint)

# Point 2: (100, 2000, 200)
pvtPoint.pos = 100
pvtPoint.velocity = 2000
pvtPoint.timeMilliseconds = 200
pvt.SetPoints(2, pvtPoint)

# Point 3: (200, 3000, 300)
pvtPoint.pos = 200
pvtPoint.velocity = 3000
pvtPoint.timeMilliseconds = 300
pvt.SetPoints(3, pvtPoint)

# Point 4: (300, 1000, 400)
pvtPoint.pos = 300
pvtPoint.velocity = 1000
pvtPoint.timeMilliseconds = 400
pvt.SetPoints(4, pvtPoint)

# Point 5: (200, 0, 500)
pvtPoint.pos = 200
pvtPoint.velocity = 0
pvtPoint.timeMilliseconds = 500
pvt.SetPoints(5, pvtPoint)

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print("StartPVT error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 1 stops moving
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print("Wait error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)


# --- Execute an absolute linear interpolation for Axes 1 and 3 to position (100, 100) with velocity 1000 ---
# Set up a position command for Axis 1
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 1
posCommand1.target = 100
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print("StartPos (Axis 1) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Set up a position command for Axis 3
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 3
posCommand3.target = 100
posCommand3.profile.velocity = 1000
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print("StartPos (Axis 3) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until both Axes 1 and 3 stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)


# --- Execute a cubic spline motion command for Axes 8 and 9 ---
# Total motion time: 1000ms
# Spline points for both axes are given as pairs:
#   Index:    Axis 8   Axis 9
#   0:        0        0
#   1:        10       10
#   2:       -20      -20
#   3:        30       30
#   4:       -40      -40
#   5:        50       50
#   6:       -60      -60
#   7:        70       70
#   8:       -80      -80

cubicSpline = Motion_CubicSplineCommand()
cubicSpline.axisCount = 2
cubicSpline.SetAxis(0, 8)
cubicSpline.SetAxis(1, 9)
cubicSpline.pointCount = 9

# Set the total time for the cubic spline motion
cubicSpline.totalTimeMilliseconds = 1000

# List of points for the cubic spline motion
spline_points = [
    (0, 0),
    (10, 10),
    (-20, -20),
    (30, 30),
    (-40, -40),
    (50, 50),
    (-60, -60),
    (70, 70),
    (-80, -80)
]

# Assume the command object has a method SetPoint(axisIndex, pointIndex, position)
for pt_index, (pos8, pos9) in enumerate(spline_points):
    cubicSpline.SetPoint(0, pt_index, pos8)
    cubicSpline.SetPoint(1, pt_index, pos9)

ret = Wmx3Lib_cm.motion.StartCubicSpline(cubicSpline)
if ret != 0:
    print("StartCubicSpline error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until both Axes 8 and 9 stop moving
axisSelSpline = AxisSelection()
axisSelSpline.axisCount = 2
axisSelSpline.SetAxis(0, 8)
axisSelSpline.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSelSpline)
if ret != 0:
    print("Wait_AxisSel (Spline) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
