
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 5)
path.SetAxis(1, 6)

path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

path.numPoints = 4

# Segment 0: Linear to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# Segment 1: Clockwise circular to (-100, -100) with center (0,0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 50)  # Relative center X: 0 - (-50) = 50
path.SetCenterPos(1, 1, 50)  # Relative center Y: 0 - (-50) = 50
path.SetDirection(1, -1)  # -1 for clockwise

# Segment 2: Linear to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# Segment 3: Counterclockwise circular to (-100, -100) with center (0,0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, -50)  # Relative center X: 0 - 50 = -50
path.SetCenterPos(1, 3, -50)  # Relative center Y: 0 - 50 = -50
path.SetDirection(3, 1)   # 1 for counterclockwise

ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for motion completion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
