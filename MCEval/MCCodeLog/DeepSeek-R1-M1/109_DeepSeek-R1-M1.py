
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# Create Advanced Motion object
adv = AdvancedMotion(Wmx3Lib)

# Part 1: Path interpolation motion command
path = AdvMotion_PathIntplCommand()

# Set axes
path.SetAxis(0, 2)
path.SetAxis(1, 9)

# Set constant motion profile
path.enableConstProfile = 1

# Set motion profile
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define path segments
path.numPoints = 4

# Segment 1: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# Segment 2: Clockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, -1)  # -1 for clockwise

# Segment 3: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Segment 4: Counterclockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, 1)  # 1 for counterclockwise

# Start path interpolation
ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    exit()

# Wait for axes to stop
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Part 2: Linear interpolation to (100, 200) with velocity 1000
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)
lin.SetTarget(1, 200)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for axes to stop
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Part 3: Clockwise circular interpolation with center at (100, 100), arc length 180, velocity 1200
circ = Motion_CircularIntplCommand()
circ.axisCount = 2
circ.SetAxis(0, 2)
circ.SetAxis(1, 9)

circ.profile.type = ProfileType.Trapezoidal
circ.profile.velocity = 1200
circ.profile.acc = 10000
circ.profile.dec = 10000

circ.SetCenterPos(0, 100)
circ.SetCenterPos(1, 100)
circ.SetDirection(-1)  # -1 for clockwise
circ.SetArcLength(180)

# Calculate target position based on arc length
# (This is a simplified example, actual calculation may vary based on specific requirements)
circ.SetTarget(0, 100 + 100 * math.cos(math.radians(180)))
circ.SetTarget(1, 100 + 100 * math.sin(math.radians(180)))

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circ)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for axes to stop
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Part 4: Move to (100, 200)
lin.SetTarget(0, 100)
lin.SetTarget(1, 200)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for axes to stop
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
