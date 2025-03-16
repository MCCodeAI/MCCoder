
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# 1. Execute an absolute position path interpolation motion command for Axis 4 and 6 with auto-smoothing and a velocity of 1000.
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 4)
path.SetAxis(1, 6)

# Use single motion profile for entire path
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

# Auto smoothing
path.enableAutoSmooth = 1

# Define linear segments
path.numPoints = 6

path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -40)
path.SetTarget(1, 0, -30)
path.SetAutoSmoothRadius(0, 10)

path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 1, 10)
path.SetTarget(1, 1, -50)
path.SetAutoSmoothRadius(1, 20)

path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, -40)
path.SetTarget(1, 2, -70)
path.SetAutoSmoothRadius(2, 30)

path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 3, 10)
path.SetTarget(1, 3, -90)
path.SetAutoSmoothRadius(3, 40)

path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, -40)
path.SetTarget(1, 4, -110)
path.SetAutoSmoothRadius(4, 50)

path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 5, 10)
path.SetTarget(1, 5, -130)

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 4)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 2. Record and execute an API buffer with the following sequence:
# First, move Axis 4 to a target position of 111 at a speed of 1000.
# When the remaining time is 8 ms, move to the target position of 222 at a speed of 2000.
# Finally, when the remaining time is 9 ms, move to the target position of 333 at a speed of 3000.

# Create a command value for the first move.
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 4
posCommand1.target = 111
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

# Execute the first move.
ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the remaining time is 8 ms.
Wmx3Lib_cm.motion.WaitRemainingTime(8)

# Create a command value for the second move.
posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.Trapezoidal
posCommand2.axis = 4
posCommand2.target = 222
posCommand2.profile.velocity = 2000
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000

# Execute the second move.
ret = Wmx3Lib_cm.motion.StartPos(posCommand2)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the remaining time is 9 ms.
Wmx3Lib_cm.motion.WaitRemainingTime(9)

# Create a command value for the third move.
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 4
posCommand3.target = 333
posCommand3.profile.velocity = 3000
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

# Execute the third move.
ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# 3. Establish a Normal type E-CAM motion for master Axis 4 and slave Axis 6.
# Move Axis 4 to -100 with a velocity of 1000.
posCommand4 = Motion_PosCommand()
posCommand4.profile.type = ProfileType.Trapezoidal
posCommand4.axis = 4
posCommand4.target = -100
posCommand4.profile.velocity = 1000
posCommand4.profile.acc = 10000
posCommand4.profile.dec = 10000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand4)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# Set up an E-CAM table with the pairs (-100, 100), (-50, 150), (0, 100), (50, 50), (100, 100), (150, 50), and (250, 150).
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Set the E-CAM table.
ECAMdata.masterAxis = 4
ECAMdata.slaveAxis = 6
ECAMdata.numPoints = 7
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, -100)
ECAMdata.SetMasterPos(1, -50)
ECAMdata.SetMasterPos(2, 0)
ECAMdata.SetMasterPos(3, 50)
ECAMdata.SetMasterPos(4, 100)
ECAMdata.SetMasterPos(5, 150)
ECAMdata.SetMasterPos(6, 250)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 150)
ECAMdata.SetSlavePos(2, 100)
ECAMdata.SetSlavePos(3, 50)
ECAMdata.SetSlavePos(4, 100)
ECAMdata.SetSlavePos(5, 50)
ECAMdata.SetSlavePos(6, 150)

# Start ECAM
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Finally, move Axis 4 to 300.
posCommand5 = Motion_PosCommand()
posCommand5.profile.type = ProfileType.Trapezoidal
posCommand5.axis = 4
posCommand5.target = 300
posCommand5.profile.velocity = 1000
posCommand5.profile.acc = 10000
posCommand5.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand5)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# Stop ECAM is a necessary step!
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
