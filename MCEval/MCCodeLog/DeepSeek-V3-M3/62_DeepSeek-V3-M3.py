
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command
path = AdvMotion_PathIntplCommand()

# Set the axes for the path interpolation
path.SetAxis(0, 2)  # Axis 2
path.SetAxis(1, 5)  # Axis 5

# Specify motion profile for each segment
path.enableConstProfile = 0

# Define linear and circular segments
path.numPoints = 8

# Segment 1: Linear interpolation to (50, 0) with velocity and end velocity of 1000
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 50)
path.SetTarget(1, 0, 0)

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 1000
path.SetProfile(0, profile)

# Segment 2: Clockwise circular interpolation to (75, 25) with center at (50, 25) with velocity and end velocity of 900
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 75)
path.SetTarget(1, 1, 25)
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 25)
path.SetDirection(1, 1)  # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 900
path.SetProfile(1, profile)

# Segment 3: Linear interpolation to (75, 50) with velocity and end velocity of 800
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

# Segment 4: Clockwise circular interpolation to (50, 75) with center at (50, 50) with velocity and end velocity of 700
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, 50)
path.SetTarget(1, 3, 75)
path.SetCenterPos(0, 3, 50)
path.SetCenterPos(1, 3, 50)
path.SetDirection(3, 1)  # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(3, profile)

# Segment 5: Linear interpolation to (0, 75) with velocity and end velocity of 600
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

# Segment 6: Clockwise circular interpolation to (-25, 50) with center at (0, 50) with velocity and end velocity of 700
path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, -25)
path.SetTarget(1, 5, 50)
path.SetCenterPos(0, 5, 0)
path.SetCenterPos(1, 5, 50)
path.SetDirection(5, 1)  # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(5, profile)

# Segment 7: Linear interpolation to (-25, 25) with velocity and end velocity of 800
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

# Segment 8: Clockwise circular interpolation to (0, 0) with center at (0, 25) with velocity of 900
path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 7, 0)
path.SetTarget(1, 7, 0)
path.SetCenterPos(0, 7, 0)
path.SetCenterPos(1, 7, 25)
path.SetDirection(7, 1)  # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
path.SetProfile(7, profile)

# Start the path interpolation motion
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
