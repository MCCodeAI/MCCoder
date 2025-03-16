
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Create an absolute position path interpolation motion command for Axis 2 and Axis 5,
# with a distinct motion profile defined for each segment.

# Assume that the following classes and functions are available:
#   AdvancedMotion, AdvMotion_PathIntplCommand, AdvMotion_PathIntplSegmentType,
#   Profile, ProfileType, AxisSelection, and the motion library objects Wmx3Lib and Wmx3Lib_cm.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

# Map logical path axis slots to actual axis numbers. Index 0 -> Axis 2, index 1 -> Axis 5.
path.SetAxis(0, 2)
path.SetAxis(1, 5)

# Use motion profiles per segment (not a single constant profile).
path.enableConstProfile = 0

# There are 8 segments in the path.
path.numPoints = 8

# Segment 0: Linear interpolation to (50, 0) with velocity and end velocity = 1000.
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 50)    # Axis 2 target position = 50
path.SetTarget(1, 0, 0)     # Axis 5 target position = 0
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 1000
path.SetProfile(0, profile)

# Segment 1: Clockwise circular interpolation to (75, 25) with center at (50, 25) with velocity and end velocity = 900.
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 75)
path.SetTarget(1, 1, 25)
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 25)
path.SetDirection(1, 1)  # 1 indicates clockwise motion.
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 900
path.SetProfile(1, profile)

# Segment 2: Linear interpolation to (75, 50) with velocity and end velocity = 800.
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 75)
path.SetTarget(1, 2, 50)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 800
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 800
path.SetProfile(2, profile)

# Segment 3: Clockwise circular interpolation to (50, 75) with center at (50, 50) with velocity and end velocity = 700.
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, 50)
path.SetTarget(1, 3, 75)
path.SetCenterPos(0, 3, 50)
path.SetCenterPos(1, 3, 50)
path.SetDirection(3, 1)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(3, profile)

# Segment 4: Linear interpolation to (0, 75) with velocity and end velocity = 600.
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 0)
path.SetTarget(1, 4, 75)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 600
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 600
path.SetProfile(4, profile)

# Segment 5: Clockwise circular interpolation to (-25, 50) with center at (0, 50) with velocity and end velocity = 700.
path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, -25)
path.SetTarget(1, 5, 50)
path.SetCenterPos(0, 5, 0)
path.SetCenterPos(1, 5, 50)
path.SetDirection(5, 1)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(5, profile)

# Segment 6: Linear interpolation to (-25, 25) with velocity and end velocity = 800.
path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 6, -25)
path.SetTarget(1, 6, 25)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 800
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 800
path.SetProfile(6, profile)

# Segment 7: Clockwise circular interpolation to (0, 0) with center at (0, 25) with velocity = 900.
# (Assuming the end velocity is the same as the transition velocity.)
path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 7, 0)
path.SetTarget(1, 7, 0)
path.SetCenterPos(0, 7, 0)
path.SetCenterPos(1, 7, 25)
path.SetDirection(7, 1)
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 900
path.SetProfile(7, profile)

# Start the absolute position path interpolation motion.
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Error handling can be added here as needed.
    exit()

# Wait for the motion to complete on both axes.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
