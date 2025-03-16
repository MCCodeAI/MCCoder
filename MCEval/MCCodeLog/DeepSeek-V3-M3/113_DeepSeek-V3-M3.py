
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = []

# 1. Path interpolation with look-ahead channel 10 for Axis 3 and 5
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Allocate buffer memory for a path interpolation with look-ahead channel with 1000 points for Channel 10
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the configuration for the path interpolation with look-ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 1500
conf.compositeAcc = 10000
conf.sampleDistance = 10
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add interpolation commands to the path interpolation with look-ahead channel
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
point.linear.smoothRadius = 12
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start the motion for the path interpolation with look-ahead channel
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the path interpolation with look-ahead channel
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 2. Cubic spline motion command for Axes 3 and 5
# Allocate buffer memory for a spline execution channel with 100 points for Channel 0
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 3)
splineCommand.SetAxis(1, 5)
splineCommand.totalTimeMilliseconds = 1000

# Set the spline point data with 9 points
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

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 9, splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the spline execution channel
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 3. Establish synchronous control between master axis 3 and 5
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(3, 5)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 3 to position 120 with velocity 1000
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

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 3 to position 240 with velocity 1000
posCommand.target = 240
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Release the synchronization between Axis 3 and 5
ret = Wmx3Lib_cm.sync.ResolveSync(5)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# 4. Execute a PVT interpolation command for Axis 3 and Axis 5
pvti = Motion_PVTIntplCommand()

pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, 20)
pvti.SetPointCount(1, 20)

# Generate 20 points on a circle with diameter 100 and center at (-50, 0)
import math
radius = 50
center_x = -50
center_y = 0
time_increment = 100

for i in range(20):
    angle = 2 * math.pi * i / 20
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    
    pvtparameter0.pos = x
    pvtparameter0.velocity = 100
    pvtparameter0.timeMilliseconds = i * time_increment
    
    pvtparameter1.pos = y
    pvtparameter1.velocity = 100
    pvtparameter1.timeMilliseconds = i * time_increment
    
    pvti.SetPoints(0, i, pvtparameter0)
    pvti.SetPoints(1, i, pvtparameter1)

# Execute the PVT interpolation command
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
