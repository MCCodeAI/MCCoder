
# Axes = [1, 3, 8, 9]
# IOInputs = []
# IOOutputs = []

# Execute a PVT command for Axis 1
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 1
pvt.pointCount = 6

# Define point data
pvtparameter.pos = 0
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 0
pvt.SetPoints(0, pvtparameter)

pvtparameter.pos = 50
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 100
pvt.SetPoints(1, pvtparameter)

pvtparameter.pos = 100
pvtparameter.velocity = 2000
pvtparameter.timeMilliseconds = 200
pvt.SetPoints(2, pvtparameter)

pvtparameter.pos = 200
pvtparameter.velocity = 3000
pvtparameter.timeMilliseconds = 300
pvt.SetPoints(3, pvtparameter)

pvtparameter.pos = 300
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 400
pvt.SetPoints(4, pvtparameter)

pvtparameter.pos = 200
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 500
pvt.SetPoints(5, pvtparameter)

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
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 1)
path.SetAxis(1, 3)

# Use single motion profile for entire path
path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1000
path.profile.acc = 10000
path.profile.dec = 10000

# Define linear segment
path.numPoints = 1

path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 100)

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)
axes.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start a cubic spline motion command for Axes 8 and 9
spline = AdvMotion_SplineCommand()

spline.SetAxis(0, 8)
spline.SetAxis(1, 9)

spline.totalTimeMilliseconds = 1000
spline.numPoints = 9

# Define spline points
spline.SetPoint(0, 0, 0)
spline.SetPoint(1, 10, 10)
spline.SetPoint(2, -20, -20)
spline.SetPoint(3, 30, 30)
spline.SetPoint(4, -40, -40)
spline.SetPoint(5, 50, 50)
spline.SetPoint(6, -60, -60)
spline.SetPoint(7, 70, 70)
spline.SetPoint(8, -80, -80)

ret = Wmx3Lib_adv.advMotion.StartSpline(spline)
if ret != 0:
    print('StartSpline error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 8)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
