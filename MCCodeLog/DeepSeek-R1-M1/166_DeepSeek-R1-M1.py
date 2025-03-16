
# Axes = [1, 3, 8, 9]
# IOInputs = []
# IOOutputs = []

# Execute PVT command for Axis 1
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 1
pvt.pointCount = 6

# Define PVT points for Axis 1
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

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to complete
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start absolute linear interpolation for Axes 1 and 3
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 1)
path.SetAxis(1, 3)

path.numPoints = 1
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 100)

path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1000
path.profile.acc = 10000
path.profile.dec = 10000

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for Axes 1 and 3 to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)
axes.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start cubic spline motion for Axes 8 and 9
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 8)
path.SetAxis(1, 9)

path.numPoints = 8
path.enableConstProfile = 1

path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1000
path.profile.acc = 10000
path.profile.dec = 10000

points = [
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

for i, (pos8, pos9) in enumerate(points):
    path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, i, pos8)
    path.SetTarget(1, i, pos9)

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for Axes 8 and 9 to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 8)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
