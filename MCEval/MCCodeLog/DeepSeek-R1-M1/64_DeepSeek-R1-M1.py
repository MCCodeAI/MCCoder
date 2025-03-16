
# Axes = [2, 4, 5]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntpl3DCommand()

path.SetAxis(0, 2)
path.SetAxis(1, 4)
path.SetAxis(2, 5)

# Use single motion profile for entire path
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 300
profile.acc = 2000
profile.dec = 2000
path.SetProfile(0, profile)

# Define linear and circular segments
path.numPoints = 21

# Forward path segments
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 90)
path.SetTarget(1, 0, 0)
path.SetTarget(2, 0, 0)

path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 100)
path.SetTarget(1, 1, 10)
path.SetTarget(2, 1, 0)
path.SetCircleIntermediateTarget(0, 1, 97.071)
path.SetCircleIntermediateTarget(1, 1, 2.929)
path.SetCircleIntermediateTarget(2, 1, 0)

path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 100)
path.SetTarget(1, 2, 90)
path.SetTarget(2, 2, 0)

path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, 90)
path.SetTarget(1, 3, 100)
path.SetTarget(2, 3, 0)
path.SetCircleIntermediateTarget(0, 3, 97.071)
path.SetCircleIntermediateTarget(1, 3, 97.071)
path.SetCircleIntermediateTarget(2, 3, 0)

path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 10)
path.SetTarget(1, 4, 100)
path.SetTarget(2, 4, 0)

path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, 0)
path.SetTarget(1, 5, 90)
path.SetTarget(2, 5, 0)
path.SetCircleIntermediateTarget(0, 5, 2.929)
path.SetCircleIntermediateTarget(1, 5, 97.071)
path.SetCircleIntermediateTarget(2, 5, 0)

path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 6, 0)
path.SetTarget(1, 6, 0)
path.SetTarget(2, 6, 0)

path.SetType(7, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 7, 90)
path.SetTarget(1, 7, 0)
path.SetTarget(2, 7, 0)

path.SetType(8, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 8, 100)
path.SetTarget(1, 8, 0)
path.SetTarget(2, 8, -10)
path.SetCircleIntermediateTarget(0, 8, 97.071)
path.SetCircleIntermediateTarget(1, 8, 0)
path.SetCircleIntermediateTarget(2, 8, -2.929)

path.SetType(9, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 9, 100)
path.SetTarget(1, 9, 0)
path.SetTarget(2, 9, -90)

path.SetType(10, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 10, 90)
path.SetTarget(1, 10, 0)
path.SetTarget(2, 10, -100)
path.SetCircleIntermediateTarget(0, 10, 97.071)
path.SetCircleIntermediateTarget(1, 10, 0)
path.SetCircleIntermediateTarget(2, 10, -97.071)

path.SetType(11, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 11, 10)
path.SetTarget(1, 11, 0)
path.SetTarget(2, 11, -100)

path.SetType(12, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 12, 0)
path.SetTarget(1, 12, 0)
path.SetTarget(2, 12, -90)
path.SetCircleIntermediateTarget(0, 12, 2.929)
path.SetCircleIntermediateTarget(1, 12, 0)
path.SetCircleIntermediateTarget(2, 12, -97.071)

path.SetType(13, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 13, 0)
path.SetTarget(1, 13, 0)
path.SetTarget(2, 13, 0)

path.SetType(14, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 14, 0)
path.SetTarget(1, 14, 90)
path.SetTarget(2, 14, 0)

path.SetType(15, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 15, 0)
path.SetTarget(1, 15, 100)
path.SetTarget(2, 15, -10)
path.SetCircleIntermediateTarget(0, 15, 0)
path.SetCircleIntermediateTarget(1, 15, 97.071)
path.SetCircleIntermediateTarget(2, 15, -2.929)

path.SetType(16, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 16, 0)
path.SetTarget(1, 16, 100)
path.SetTarget(2, 16, -90)

path.SetType(17, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 17, 0)
path.SetTarget(1, 17, 90)
path.SetTarget(2, 17, -100)
path.SetCircleIntermediateTarget(0, 17, 0)
path.SetCircleIntermediateTarget(1, 17, 97.071)
path.SetCircleIntermediateTarget(2, 17, -97.071)

path.SetType(18, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 18, 0)
path.SetTarget(1, 18, 10)
path.SetTarget(2, 18, -100)

path.SetType(19, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 19, 0)
path.SetTarget(1, 19, 0)
path.SetTarget(2, 19, -90)
path.SetCircleIntermediateTarget(0, 19, 0)
path.SetCircleIntermediateTarget(1, 19, 2.929)
path.SetCircleIntermediateTarget(2, 19, -97.071)

path.SetType(20, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 20, 0)
path.SetTarget(1, 20, 0)
path.SetTarget(2, 20, 0)

ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
if ret != 0:
    print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the forward path to complete
axes = AxisSelection()
axes.axisCount = 3
axes.SetAxis(0, 2)
axes.SetAxis(1, 4)
axes.SetAxis(2, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Reverse the path from step 21 back to step 1
reversed_path = AdvMotion_PathIntpl3DCommand()
reversed_path.SetAxis(0, 2)
reversed_path.SetAxis(1, 4)
reversed_path.SetAxis(2, 5)
reversed_path.enableConstProfile = 1
reversed_path.SetProfile(0, profile)
reversed_path.numPoints = 21

for i in range(20, -1, -1):
    reversed_path.SetType(20 - i, path.GetType(i))
    reversed_path.SetTarget(0, 20 - i, path.GetTarget(0, i))
    reversed_path.SetTarget(1, 20 - i, path.GetTarget(1, i))
    reversed_path.SetTarget(2, 20 - i, path.GetTarget(2, i))
    if path.GetType(i) == AdvMotion_PathIntplSegmentType.Circular:
        reversed_path.SetCircleIntermediateTarget(0, 20 - i, path.GetCircleIntermediateTarget(0, i))
        reversed_path.SetCircleIntermediateTarget(1, 20 - i, path.GetCircleIntermediateTarget(1, i))
        reversed_path.SetCircleIntermediateTarget(2, 20 - i, path.GetCircleIntermediateTarget(2, i))

ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(reversed_path)
if ret != 0:
    print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the reversed path to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
