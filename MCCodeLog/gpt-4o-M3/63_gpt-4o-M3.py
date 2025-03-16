
# Axes = [3, 6]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command
path = AdvMotion_PathIntplCommand()

# Set the axes for the path interpolation
path.SetAxis(0, 3)
path.SetAxis(1, 6)

# Use a single motion profile for the entire path
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

# Enable auto smoothing
path.enableAutoSmooth = 1

# Define the path with linear segments and auto-smoothing radii
path.numPoints = 6

path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -40)
path.SetTarget(1, 0, -30)
path.SetAutoSmoothRadius(0, 10)

path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 1, 10)
path.SetTarget(1, 1, -50)
path.SetAutoSmoothRadius(1, 20)

path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, -40)
path.SetTarget(1, 2, -70)
path.SetAutoSmoothRadius(2, 30)

path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 3, 10)
path.SetTarget(1, 3, -90)
path.SetAutoSmoothRadius(3, 40)

path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, -40)
path.SetTarget(1, 4, -110)
path.SetAutoSmoothRadius(4, 50)

path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 5, 10)
path.SetTarget(1, 5, -130)

# Start the path interpolation motion
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 3)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
