
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

# Map physical axes to the command: Axis 5 is mapped to index 0 and Axis 6 to index 1
path.SetAxis(0, 5)
path.SetAxis(1, 6)

# Use a single motion profile for the entire path
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the path with 4 segments:
# Segment 0: Linear interpolation to (-50, -50)
# Segment 1: Clockwise circular interpolation to (-100, -100) with center (0, 0)
# Segment 2: Linear interpolation to (50, 50)
# Segment 3: Counterclockwise circular interpolation to (-100, -100) with center (0, 0)
path.numPoints = 4

# Segment 0: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)  # Axis 5 target
path.SetTarget(1, 0, -50)  # Axis 6 target

# Segment 1: Circular interpolation (clockwise: direction -1) to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)  # Axis 5 target
path.SetTarget(1, 1, -100)  # Axis 6 target
path.SetCenterPos(0, 1, 0)  # Axis 5 center
path.SetCenterPos(1, 1, 0)  # Axis 6 center
path.SetDirection(1, -1)    # -1 for clockwise

# Segment 2: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)   # Axis 5 target
path.SetTarget(1, 2, 50)   # Axis 6 target

# Segment 3: Circular interpolation (counterclockwise: direction 1) to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)  # Axis 5 target
path.SetTarget(1, 3, -100)  # Axis 6 target
path.SetCenterPos(0, 3, 0)  # Axis 5 center
path.SetCenterPos(1, 3, 0)  # Axis 6 center
path.SetDirection(3, 1)     # 1 for counterclockwise

# Start the absolute path interpolation motion command
ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for the motion to complete, blocking until Axis 5 and Axis 6 become idle
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
