
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Task 1: Path interpolation motion
path = AdvMotion_PathIntplCommand()
path.SetAxis(0, 2)
path.SetAxis(1, 9)

path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

path.numPoints = 4

# Segment 1: Linear to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# Segment 2: Clockwise circular to (-100, -100) with center (0,0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, 1)  # 1 for clockwise

# Segment 3: Linear to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Segment 4: Counterclockwise circular to (-100, -100) with center (0,0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, -1)  # -1 for counterclockwise

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Task 2: Linear interpolation to (100, 200) with velocity 1000
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
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 3: Clockwise circular interpolation with center (100,100), arc length 180, velocity 1200
circular = Motion_CenterAndLengthCircularIntplCommand()
circular.SetAxis(0, 2)
circular.SetAxis(1, 9)
circular.SetCenterPos(0, 100)
circular.SetCenterPos(1, 100)
circular.clockwise = 1
circular.arcLengthDegree = 180
circular.profile.type = ProfileType.Trapezoidal
circular.profile.velocity = 1200
circular.profile.acc = 10000
circular.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circular)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 4: Move to (100, 200)
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 100
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 9
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
