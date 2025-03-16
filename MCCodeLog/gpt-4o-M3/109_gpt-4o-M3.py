
# Axes = [9, 2]
# IOInputs = []
# IOOutputs = []

# Start an absolute path interpolation motion command for Axes 9 and 2 with a velocity of 1200.
adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 9)
path.SetAxis(1, 2)

# Use single motion profile for entire path
path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Define linear and circular segments
path.numPoints = 4

# Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# Clockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, 1)

# Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Counterclockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, -1)

ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 9)
axes.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start an absolute linear interpolation for Axes 9 and 2 to position (100, 200) with a velocity of 1000
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 9)
lin.SetAxis(1, 2)

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
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion command for Axis 9 and 2, with a center position of (100, 100), an arc length of 180, and a velocity of 1200
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()

circularIntplCommand.SetAxis(0, 9)
circularIntplCommand.SetAxis(1, 2)
circularIntplCommand.SetCenterPos(0, 100)
circularIntplCommand.SetCenterPos(1, 100)
circularIntplCommand.clockwise = 1
circularIntplCommand.arcLengthDegree = 180
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1200
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 9 and 2 to (100, 200)
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.target = 100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 2
posCommand.target = 200

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
