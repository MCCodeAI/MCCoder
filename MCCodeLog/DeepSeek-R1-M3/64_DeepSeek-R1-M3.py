
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

# Define reversed segments from original 21 steps
path.numPoints = 21

# Segment 0 (Original 20): Linear to (0,0,-90)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 0)
path.SetTarget(1, 0, 0)
path.SetTarget(2, 0, -90)

# Segment 1 (Original 19): Circular to (0,10,-100) with center (0,2.929,-97.071)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, 0)
path.SetTarget(1, 1, 10)
path.SetTarget(2, 1, -100)
path.SetCircleIntermediateTarget(0, 1, 0)
path.SetCircleIntermediateTarget(1, 1, 2.929)
path.SetCircleIntermediateTarget(2, 1, -97.071)

# Segment 2 (Original 18): Linear to (0,90,-100)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 0)
path.SetTarget(1, 2, 90)
path.SetTarget(2, 2, -100)

# Segment 3 (Original 17): Circular to (0,100,-90) with center (0,97.071,-97.071)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, 0)
path.SetTarget(1, 3, 100)
path.SetTarget(2, 3, -90)
path.SetCircleIntermediateTarget(0, 3, 0)
path.SetCircleIntermediateTarget(1, 3, 97.071)
path.SetCircleIntermediateTarget(2, 3, -97.071)

# Segment 4 (Original 16): Linear to (0,100,-10)
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 0)
path.SetTarget(1, 4, 100)
path.SetTarget(2, 4, -10)

# Segment 5 (Original 15): Circular to (0,90,0) with center (0,97.071,-2.929)
path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, 0)
path.SetTarget(1, 5, 90)
path.SetTarget(2, 5, 0)
path.SetCircleIntermediateTarget(0, 5, 0)
path.SetCircleIntermediateTarget(1, 5, 97.071)
path.SetCircleIntermediateTarget(2, 5, -2.929)

# Segment 6 (Original 14): Linear to (0,0,0)
path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 6, 0)
path.SetTarget(1, 6, 0)
path.SetTarget(2, 6, 0)

# Segment 7 (Original 13): Linear to (0,0,-90)
path.SetType(7, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 7, 0)
path.SetTarget(1, 7, 0)
path.SetTarget(2, 7, -90)

# Segment 8 (Original 12): Circular to (10,0,-100) with center (2.929,0,-97.071)
path.SetType(8, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 8, 10)
path.SetTarget(1, 8, 0)
path.SetTarget(2, 8, -100)
path.SetCircleIntermediateTarget(0, 8, 2.929)
path.SetCircleIntermediateTarget(1, 8, 0)
path.SetCircleIntermediateTarget(2, 8, -97.071)

# Segment 9 (Original 11): Linear to (90,0,-100)
path.SetType(9, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 9, 90)
path.SetTarget(1, 9, 0)
path.SetTarget(2, 9, -100)

# Segment 10 (Original 10): Circular to (100,0,-90) with center (97.071,0,-97.071)
path.SetType(10, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 10, 100)
path.SetTarget(1, 10, 0)
path.SetTarget(2, 10, -90)
path.SetCircleIntermediateTarget(0, 10, 97.071)
path.SetCircleIntermediateTarget(1, 10, 0)
path.SetCircleIntermediateTarget(2, 10, -97.071)

# Segment 11 (Original 9): Linear to (100,0,-10)
path.SetType(11, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 11, 100)
path.SetTarget(1, 11, 0)
path.SetTarget(2, 11, -10)

# Segment 12 (Original 8): Circular to (90,0,0) with center (97.071,0,-2.929)
path.SetType(12, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 12, 90)
path.SetTarget(1, 12, 0)
path.SetTarget(2, 12, 0)
path.SetCircleIntermediateTarget(0, 12, 97.071)
path.SetCircleIntermediateTarget(1, 12, 0)
path.SetCircleIntermediateTarget(2, 12, -2.929)

# Segment 13 (Original 7): Linear to (0,0,0)
path.SetType(13, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 13, 0)
path.SetTarget(1, 13, 0)
path.SetTarget(2, 13, 0)

# Segment 14 (Original 6): Linear to (0,90,0)
path.SetType(14, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 14, 0)
path.SetTarget(1, 14, 90)
path.SetTarget(2, 14, 0)

# Segment 15 (Original 5): Circular to (10,100,0) with center (2.929,97.071,0)
path.SetType(15, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 15, 10)
path.SetTarget(1, 15, 100)
path.SetTarget(2, 15, 0)
path.SetCircleIntermediateTarget(0, 15, 2.929)
path.SetCircleIntermediateTarget(1, 15, 97.071)
path.SetCircleIntermediateTarget(2, 15, 0)

# Segment 16 (Original 4): Linear to (90,100,0)
path.SetType(16, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 16, 90)
path.SetTarget(1, 16, 100)
path.SetTarget(2, 16, 0)

# Segment 17 (Original 3): Circular to (100,90,0) with center (97.071,97.071,0)
path.SetType(17, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 17, 100)
path.SetTarget(1, 17, 90)
path.SetTarget(2, 17, 0)
path.SetCircleIntermediateTarget(0, 17, 97.071)
path.SetCircleIntermediateTarget(1, 17, 97.071)
path.SetCircleIntermediateTarget(2, 17, 0)

# Segment 18 (Original 2): Linear to (100,10,0)
path.SetType(18, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 18, 100)
path.SetTarget(1, 18, 10)
path.SetTarget(2, 18, 0)

# Segment 19 (Original 1): Circular to (90,0,0) with center (97.071,2.929,0)
path.SetType(19, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 19, 90)
path.SetTarget(1, 19, 0)
path.SetTarget(2, 19, 0)
path.SetCircleIntermediateTarget(0, 19, 97.071)
path.SetCircleIntermediateTarget(1, 19, 2.929)
path.SetCircleIntermediateTarget(2, 19, 0)

# Segment 20 (Original 0): Linear to (0,0,0)
path.SetType(20, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 20, 0)
path.SetTarget(1, 20, 0)
path.SetTarget(2, 20, 0)

ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
if ret != 0:
    print('StartPathIntpl3DPos error code:', ret, Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for motion completion
axes = AxisSelection()
axes.axisCount = 3
axes.SetAxis(0, 2)
axes.SetAxis(1, 4)
axes.SetAxis(2, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code:', ret, Wmx3Lib_adv.ErrorToString(ret))
    exit()
