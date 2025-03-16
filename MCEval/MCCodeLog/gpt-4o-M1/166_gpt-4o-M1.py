
# Axes = [1, 3, 8, 9]
# IOInputs = []
# IOOutputs = []

# Execute a PVT command for Axis 1
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 1
pvt.pointCount = 6

# Define point data for PVT
points = [
    (0, 0, 0),
    (50, 1000, 100),
    (100, 2000, 200),
    (200, 3000, 300),
    (300, 1000, 400),
    (200, 0, 500)
]

for i, (pos, vel, time) in enumerate(points):
    pvtparameter.pos = pos
    pvtparameter.velocity = vel
    pvtparameter.timeMilliseconds = time
    pvt.SetPoints(i, pvtparameter)

# Start PVT motion
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start an absolute linear interpolation for Axes 1 and 3
linearInterp = Motion_LinearInterpolationCommand()
linearInterp.axisCount = 2
linearInterp.SetAxis(0, 1)
linearInterp.SetAxis(1, 3)
linearInterp.targetPosition = [100, 100]
linearInterp.velocity = 1000

ret = Wmx3Lib_cm.motion.StartLinearInterpolation(linearInterp)
if ret != 0:
    print('StartLinearInterpolation error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the linear interpolation to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)
axes.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a cubic spline motion command for Axes 8 and 9
spline = Motion_CubicSplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 8)
spline.SetAxis(1, 9)
spline.totalTimeMilliseconds = 1000

# Define spline points
splinePoints = [
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

for i, (pos8, pos9) in enumerate(splinePoints):
    spline.SetPoint(0, i, pos8)
    spline.SetPoint(1, i, pos9)

ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
if ret != 0:
    print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 8)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
