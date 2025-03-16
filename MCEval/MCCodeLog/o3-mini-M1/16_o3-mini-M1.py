
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Create an absolute position path interpolation command for Axes 6 and 4
advMotion = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

# Set up the axes for motion: first coordinate from Axis6 and second coordinate from Axis4.
path.SetAxis(0, 6)
path.SetAxis(1, 4)

# Use a single motion profile (parabolic) for the entire path
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Parabolic
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the path with 2 segments:
# 1st Segment: Linear interpolation to (100, 100)
# 2nd Segment: Clockwise circular interpolation to (0, 0) with center at (50, 50)
path.numPoints = 2

# Segment 0: Linear interpolation to (100, 100)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 100)  # Axis6 target position
path.SetTarget(1, 0, 100)  # Axis4 target position

# Segment 1: Circular interpolation to (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 0)   # Axis6 target position
path.SetTarget(1, 1, 0)   # Axis4 target position
path.SetCenterPos(0, 1, 50)  # Center position for Axis6
path.SetCenterPos(1, 1, 50)  # Center position for Axis4

# According to convention: 1 for counterclockwise, -1 for clockwise.
path.SetDirection(1, -1)   # Set circular interpolation direction to clockwise

# Start the path interpolation motion command
ret = advMotion.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
    exit(1)

# Wait for the complete motion to finish on Axes 6 and 4.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
