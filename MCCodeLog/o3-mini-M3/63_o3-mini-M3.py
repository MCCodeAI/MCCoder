
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Create an instance of the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command object for absolute positioning
path = AdvMotion_PathIntplCommand()

# Define the axes to be used (sorted order)
path.SetAxis(0, 3)
path.SetAxis(1, 6)

# Use a single motion profile for the entire path
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
# Optionally, set acceleration and deceleration if needed:
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

# Enable auto-smoothing for path blending between segments
path.enableAutoSmooth = 1

# There are 6 motion segments in the given path
path.numPoints = 6

# Segment 0: Move to (-40, -30) with autoSmoothRadius 10 
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -40)  # Axis 3 target
path.SetTarget(1, 0, -30)  # Axis 6 target
path.SetAutoSmoothRadius(0, 10)

# Segment 1: Move to (10, -50) with autoSmoothRadius 20
path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 1, 10)   # Axis 3 target
path.SetTarget(1, 1, -50)  # Axis 6 target
path.SetAutoSmoothRadius(1, 20)

# Segment 2: Move to (-40, -70) with autoSmoothRadius 30
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, -40)  # Axis 3 target
path.SetTarget(1, 2, -70)  # Axis 6 target
path.SetAutoSmoothRadius(2, 30)

# Segment 3: Move to (10, -90) with autoSmoothRadius 40
path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 3, 10)   # Axis 3 target
path.SetTarget(1, 3, -90)  # Axis 6 target
path.SetAutoSmoothRadius(3, 40)

# Segment 4: Move to (-40, -110) with autoSmoothRadius 50
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, -40)  # Axis 3 target
path.SetTarget(1, 4, -110) # Axis 6 target
path.SetAutoSmoothRadius(4, 50)

# Segment 5: Move to (10, -130) (no smoothing radius specified)
path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 5, 10)    # Axis 3 target
path.SetTarget(1, 5, -130)  # Axis 6 target
# No auto-smooth radius provided for the last segment

# Start the absolute position path interpolation command
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
else:
    # Wait for the entire path motion command on both axes to complete
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
