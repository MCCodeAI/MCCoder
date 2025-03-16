
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 2)
path.SetAxis(1, 7)

# Use single motion profile for entire path
path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 2200
path.profile.acc = 10000
path.profile.dec = 10000

# Define linear and circular segments
path.numPoints = 5

# Line to (50, 0)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 50)
path.SetTarget(1, 0, 0)

# Circular to (50, 0) through (50, 100)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 50)
path.SetTarget(1, 1, 0)
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 100)
path.SetDirection(1, 1)  # 1 for clockwise, -1 for counterclockwise

# Line to (100, 0)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 100)
path.SetTarget(1, 2, 0)

# Sleep for 0.5 seconds
path.SetType(3, AdvMotion_PathIntplSegmentType.Dwell)
path.SetDwellTime(3, 500)  # Dwell time in milliseconds

# Line to (150, 100)
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 150)
path.SetTarget(1, 4, 100)

# Line to (200, 0)
path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 5, 200)
path.SetTarget(1, 5, 0)

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
