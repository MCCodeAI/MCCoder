
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

# Assign axes: Axis 5 and Axis 6 are used.
path.SetAxis(0, 5)
path.SetAxis(1, 6)

# Use a single motion profile for the entire path.
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# There are 4 segments in the path.
path.numPoints = 4

# IMPORTANT:
# The first point time must be set to zero (for both axes) to avoid the "FirstPointTimeNotZero" error.
path.SetPointTime(0, 0, 0)
path.SetPointTime(1, 0, 0)

# Segment 0: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# Segment 1: Clockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, -1)  # -1 for clockwise rotation

# Segment 2: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Segment 3: Counterclockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, 1)  # 1 for counterclockwise rotation

# Start the continuous absolute path interpolation command.
# Since the points are part of one continuous path, do not wait between segments;
# instead, wait only once when the overall motion completes.
ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    exit(1)

# Wait for the motion to complete on Axis 5 and Axis 6.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
