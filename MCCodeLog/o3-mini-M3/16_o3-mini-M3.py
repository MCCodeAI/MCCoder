
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Create an instance of AdvancedMotion using the provided library handle.
advMotion = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

# Assign axes in sorted order: axis 0 corresponds to Axis 4 and axis 1 corresponds to Axis 6.
path.SetAxis(0, 4)
path.SetAxis(1, 6)

# Use a constant motion profile for the entire path.
# Configure the profile to use a parabolic motion type with velocity 1200.
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Parabolic
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the path segments.
# We have two segments:
# 1. Linear interpolation to (100, 100).
# 2. Clockwise circular interpolation to (0, 0) with center at (50, 50).
path.numPoints = 2

# Segment 0: Linear interpolation
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
# For the linear segment, the target positions for the two axes are:
#   - For axis 4 (assigned at index 0): position 100
#   - For axis 6 (assigned at index 1): position 100
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 100)

# Segment 1: Circular interpolation (clockwise)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
# For the circular segment, the target positions become:
#   - For axis 4: position 0
#   - For axis 6: position 0
path.SetTarget(0, 1, 0)
path.SetTarget(1, 1, 0)
# Specify the center position for the circular arc
path.SetCenterPos(0, 1, 50)
path.SetCenterPos(1, 1, 50)
# Specify the interpolation direction: -1 indicates a clockwise motion.
path.SetDirection(1, -1)

# Start the absolute path interpolation motion.
ret = advMotion.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
else:
    # After the entire multi-segment path command has been issued,
    # wait for all specified axes to become idle.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 4)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + advMotion.ErrorToString(ret))
