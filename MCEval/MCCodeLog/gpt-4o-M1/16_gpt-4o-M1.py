
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command
path = AdvMotion_PathIntplCommand()

# Set the axes for the motion
path.SetAxis(0, 6)
path.SetAxis(1, 4)

# Use a parabolic profile for the entire path
path.enableConstProfile = 1

# Define the motion profile
path.profile = Profile()
path.profile.type = ProfileType.Parabolic
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the path segments
path.numPoints = 2

# First segment: Linear interpolation to (100, 100)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 100)

# Second segment: Clockwise circular interpolation to (0, 0) with center at (50, 50)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 0)
path.SetTarget(1, 1, 0)
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 50)
path.SetDirection(1, 1)  # 1 for clockwise

# Start the path interpolation motion
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 6)
axes.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
