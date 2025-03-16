
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# -----------------------------------------------------------------------------
# This script executes a series of motion commands:
# 1. An absolute path interpolation that includes 4 segments on Axes 2 and 9.
#    • Segment 0: Linear interpolation to (-50, -50)
#    • Segment 1: Clockwise circular interpolation to (-100, -100) with center (0, 0)
#    • Segment 2: Linear interpolation to (50, 50)
#    • Segment 3: Counterclockwise circular interpolation to (-100, -100) with center (0, 0)
#
# 2. An absolute linear interpolation command to move Axes 2 and 9 to (100, 200)
#    with a velocity of 1000.
#
# 3. A single clockwise circular interpolation command for Axes 2 and 9 with a center
#    at (100, 100), an arc length of 180, and a velocity of 1200.
#
# 4. A direct move (e.g. point-to-point) command to move Axes 2 and 9 to (100, 200).
#
# Each independent motion command is followed by waiting for the involved axes to become idle.
# -----------------------------------------------------------------------------

# Step 1: Absolute position path interpolation on Axes 2 and 9 with velocity 1200.
adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

# Set the axes (order: axis index 0 is axis 2, index 1 is axis 9)
path.SetAxis(0, 2)
path.SetAxis(1, 9)

# Use a single (constant) motion profile for the entire path.
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

path.numPoints = 4

# Segment 0: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)  # For axis index 0 (axis 2): -50
path.SetTarget(1, 0, -50)  # For axis index 1 (axis 9): -50

# Segment 1: Clockwise circular interpolation to (-100, -100) with center (0,0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
# Clockwise: use -1 for direction
path.SetDirection(1, -1)

# Segment 2: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Segment 3: Counterclockwise circular interpolation to (-100, -100) with center (0,0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
# Counterclockwise: use 1 for direction
path.SetDirection(3, 1)

ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    exit(1)

# Wait until Axes 2 and 9 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Step 2: Absolute position linear interpolation to (100, 200) on Axes 2 and 9 with velocity 1000.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set absolute targets: Axis 2 to 100, Axis 9 to 200.
lin.SetTarget(0, 100)
lin.SetTarget(1, 200)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for this move to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Step 3: Clockwise circular interpolation on Axes 2 and 9.
# Assume there exists a command class for circular interpolation.
circ = Motion_CircularIntplCommand()
circ.axisCount = 2
circ.SetAxis(0, 2)
circ.SetAxis(1, 9)

# Set the center position to (100, 100) and arc length to 180.
circ.centerX = 100  # For axis index 0 (axis 2)
circ.centerY = 100  # For axis index 1 (axis 9)
circ.arcLength = 180

circ.profile.type = ProfileType.Trapezoidal
circ.profile.velocity = 1200
circ.profile.acc = 10000
circ.profile.dec = 10000

# Direction: Clockwise interpolation implies using -1 for the direction inside the command.
circ.direction = -1

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circ)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for the circular interpolation motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Step 4: Move Axes 2 and 9 to (100, 200) using a point-to-point (PTP) command.
ptp = Motion_PTPCommand()
ptp.axisCount = 2
ptp.SetAxis(0, 2)
ptp.SetAxis(1, 9)

# Set the target positions.
ptp.SetTarget(0, 100)
ptp.SetTarget(1, 200)

# Start the point-to-point move.
ret = Wmx3Lib_cm.motion.StartPTPPos(ptp)
if ret != 0:
    print('StartPTPPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for the final motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
