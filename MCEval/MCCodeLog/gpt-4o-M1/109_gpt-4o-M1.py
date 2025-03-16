
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# Initialize the motion command for Axes 2 and 9
adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 2)
path.SetAxis(1, 9)

# Use a single motion profile for the entire path
path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define the path segments
path.numPoints = 4

# 1st segment: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# 2nd segment: Clockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, -1)  # -1 for clockwise

# 3rd segment: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# 4th segment: Counterclockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, 1)  # 1 for counterclockwise

# Start the path interpolation motion
ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start an absolute linear interpolation for Axes 2 and 9 to position (100, 200) with a velocity of 1000
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
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion command for Axis 2 and 9
path = AdvMotion_PathIntplCommand()
path.SetAxis(0, 2)
path.SetAxis(1, 9)

path.enableConstProfile = 1
path.profile.velocity = 1200

path.numPoints = 1
path.SetType(0, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 0, 100)
path.SetTarget(1, 0, 200)
path.SetCenterPos(0, 0, 100)
path.SetCenterPos(1, 0, 100)
path.SetDirection(0, -1)  # -1 for clockwise

ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 2 and 9 to (100, 200)
lin.SetTarget(0, 100)
lin.SetTarget(1, 200)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
