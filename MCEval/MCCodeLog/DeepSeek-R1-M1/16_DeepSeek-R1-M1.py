
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 4)
path.SetAxis(1, 6)

# Use single motion profile for entire path
path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Parabolic
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define path segments
path.numPoints = 2

# Segment 0: Linear interpolation to (100, 100)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)  # Axis 4 position
path.SetTarget(1, 0, 100)  # Axis 6 position

# Segment 1: Clockwise circular interpolation to (0, 0) with center (50, 50)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 0)    # Axis 4 position
path.SetTarget(1, 1, 0)    # Axis 6 position
path.SetCenterPos(0, 1, 50)  # Axis 4 center
path.SetCenterPos(1, 1, 50)  # Axis 6 center
path.SetDirection(1, 1)     # Clockwise direction

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 4)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
