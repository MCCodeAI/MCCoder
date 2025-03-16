
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = []

# 1. Path interpolation with look-ahead channel 10 for Axis 3 and 5
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Allocate buffer memory for a path interpolation with look ahead channel with 1,000 points for Channel 10.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the configuration for the path interpolation with lookahead channel, specifying Axis 3 and Axis 5, with composite velocity of 1500, composite acceleration of 20,000, and sample distance of 100.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 1500
conf.compositeAcc = 20000
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add interpolation commands to the path interpolation with look ahead channel.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 12
path.SetPoint(0, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 12
path.SetPoint(1, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 12
path.SetPoint(2, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start the motion for the path interpolation with look ahead channel.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for a path interpolation with lookahead channel.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 2. Cubic spline motion command for Axes 3 and 5
# Allocate buffer memory for a spline execution channel with 100 points for Channel 0.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options, specifying Axis 3 and Axis 5, with a total time of 1,000 milliseconds to complete the spline motion.
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 3)
splineCommand.SetAxis(1, 5)
splineCommand.totalTimeMilliseconds = 1000

# Set the spline point data with 9 points.
splinePoint = []

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[0].SetPos(0, 0)
splinePoint[0].SetPos(1, 0)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[1].SetPos(0, 10)
splinePoint[1].SetPos(1, 10)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[2].SetPos(0, -20)
splinePoint[2].SetPos(1, -20)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[3].SetPos(0, 30)
splinePoint[3].SetPos(1, 30)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[4].SetPos(0, -40)
splinePoint[4].SetPos(1, -40)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[5].SetPos(0, 50)
splinePoint[5].SetPos(1, 50)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[6].SetPos(0, -60)
splinePoint[6].SetPos(1, -60)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[7].SetPos(0, 70)
splinePoint[7].SetPos(1, 70)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[8].SetPos(0, -80)
splinePoint[8].SetPos(1, -80)

# Execute the spline command.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 9, splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the spline execution channel.
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 3. Establish synchronous control between master axis 3 and 5
# Move Axis 3 to position 120 and 240 respectively with a velocity of 1000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(3)

posCommand.target = 240
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(3)

# 4. Execute a PVT interpolation command for Axis 3 and Axis 5
# Generate points on a circle with a diameter of 100 and a center at (-50, 0)
import math

points = []
for i in range(20):
    angle = 2 * math.pi * i / 20
    x = -50 + 50 * math.cos(angle)
    y = 0 + 50 * math.sin(angle)
    points.append((x, y, 100, 100, 100 * (i + 1)))

# Execute PVT interpolation
pvtCommand = AdvMotion_PVTCommand()
pvtCommand.dimensionCount = 2
pvtCommand.SetAxis(0, 3)
pvtCommand.SetAxis(1, 5)
pvtCommand.numPoints = 20

for i, point in enumerate(points):
    pvtCommand.SetPoint(i, point[0], point[1], point[2], point[3], point[4])

ret = Wmx3Lib_adv.advMotion.StartPVT(pvtCommand)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the PVT motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
