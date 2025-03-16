
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Create an instance for advanced motion control (assuming AdvancedMotion and related classes are already defined)
advMotionCtrl = AdvancedMotion(Wmx3Lib)

# Create a new path interpolation command
path = AdvMotion_PathIntplCommand()

# Set the two axes: first coordinate (X) is Axis 2, second coordinate (Y) is Axis 5
path.SetAxis(0, 2)
path.SetAxis(1, 5)

# Specify that a distinct motion profile is used for each segment
path.enableConstProfile = 0

# Total number of segments to execute
path.numPoints = 8

# 1st segment: linear interpolation to (50, 0) with velocity and end velocity = 1000
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 50)   # Axis 2 target
path.SetTarget(1, 0, 0)    # Axis 5 target

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 1000
path.SetProfile(0, profile)

# 2nd segment: clockwise circular interpolation to (75, 25) with center at (50, 25), velocity and end velocity = 900
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 75)   # Axis 2 target
path.SetTarget(1, 1, 25)   # Axis 5 target
path.SetCenterPos(0, 1, 50) # Axis 2 center
path.SetCenterPos(1, 1, 25) # Axis 5 center
path.SetDirection(1, 1)    # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 900
path.SetProfile(1, profile)

# 3rd segment: linear interpolation to (75, 50) with velocity and end velocity = 800
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 75)   # Axis 2 target
path.SetTarget(1, 2, 50)   # Axis 5 target

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 800
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 800
path.SetProfile(2, profile)

# 4th segment: clockwise circular interpolation to (50, 75) with center at (50, 50), velocity and end velocity = 700
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, 50)   # Axis 2 target
path.SetTarget(1, 3, 75)   # Axis 5 target
path.SetCenterPos(0, 3, 50) # Axis 2 center
path.SetCenterPos(1, 3, 50) # Axis 5 center
path.SetDirection(3, 1)    # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(3, profile)

# 5th segment: linear interpolation to (0, 75) with velocity and end velocity = 600
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 0)    # Axis 2 target
path.SetTarget(1, 4, 75)   # Axis 5 target

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 600
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 600
path.SetProfile(4, profile)

# 6th segment: clockwise circular interpolation to (-25, 50) with center at (0, 50), velocity and end velocity = 700
path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, -25)  # Axis 2 target
path.SetTarget(1, 5, 50)   # Axis 5 target
path.SetCenterPos(0, 5, 0)  # Axis 2 center
path.SetCenterPos(1, 5, 50) # Axis 5 center
path.SetDirection(5, 1)    # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 700
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 700
path.SetProfile(5, profile)

# 7th segment: linear interpolation to (-25, 25) with velocity and end velocity = 800
path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 6, -25)  # Axis 2 target
path.SetTarget(1, 6, 25)   # Axis 5 target

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 800
profile.acc = 10000
profile.dec = 10000
profile.endVelocity = 800
path.SetProfile(6, profile)

# 8th segment: clockwise circular interpolation to (0, 0) with center at (0, 25) with velocity = 900
path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 7, 0)    # Axis 2 target
path.SetTarget(1, 7, 0)    # Axis 5 target
path.SetCenterPos(0, 7, 0)  # Axis 2 center
path.SetCenterPos(1, 7, 0 + 25) # Axis 5 center (using (0,25))
path.SetDirection(7, 1)    # 1 for clockwise

profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 900
profile.acc = 10000
profile.dec = 10000
# End velocity is not specified for segment 8, so we'll omit it.
path.SetProfile(7, profile)

# Start the path interpolation absolute position motion command
ret = advMotionCtrl.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotionCtrl.ErrorToString(ret))
    # Early exit on error
    exit(1)

# Wait for the motion to complete on both Axis 2 and Axis 5
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)
