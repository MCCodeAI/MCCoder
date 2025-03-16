
# Axes = [6, 4]
# Inputs = []
# Outputs = []

# Initialize the advanced motion command
advMotion = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command
path = AdvMotion_PathIntplCommand()

# Set the axes for the path interpolation
path.SetAxis(0, 6)
path.SetAxis(1, 4)

# Use a single motion profile for the entire path
path.enableConstProfile = 1

# Define the motion profile
path.profile = Profile()
path.profile.type = ProfileType.Parabolic
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the number of segments in the path
path.numPoints = 2

# Define the first segment: Linear interpolation to (100, 100)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 100)

# Start the first segment motion
ret = advMotion.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
    return

# Wait for the first segment motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
    return

# Define the second segment: Clockwise circular interpolation to (0, 0) with center at (50, 50)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 0)
path.SetTarget(1, 1, 0)
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 50)
path.SetDirection(1, 1)  # 1 for clockwise

# Start the second segment motion
ret = advMotion.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
    return

# Wait for the second segment motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
    return
