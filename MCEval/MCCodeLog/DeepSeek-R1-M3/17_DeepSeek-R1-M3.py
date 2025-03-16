
# Axes = [5, 7]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 5)
path.SetAxis(1, 7)

# Configure motion profile
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

# Add path segments with relative pattern (10*j, -10*j)
path.numPoints = 5
for j in range(5):
    path.SetType(j, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, j, 10 * j)  # Axis 5 target
    path.SetTarget(1, j, -10 * j) # Axis 7 target

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for axes to stop
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 5)
axes.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
