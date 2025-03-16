
# Axes = [4, 6]
# Inputs = []
# Outputs = []

# Task 1: Execute an absolute position path interpolation motion command for Axis 4 and 6 with auto-smoothing and a velocity of 1000.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

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

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 4)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Task 2: Record and execute an API buffer with the specified sequence for Axis 4.

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

cond = ApiBufferCondition()

# Add a position command to the API buffer.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 111
posCommand.profile.velocity = 1000
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for position command to have 8ms remaining time
cond.bufferConditionType = ApiBufferConditionType.RemainingTime
cond.arg_remainingTime.axis = 4
cond.arg_remainingTime.timeMilliseconds = 8
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Add a position command to the API buffer
posCommand.target = 222
posCommand.profile.velocity = 2000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for position command to have 9ms remaining time
cond.arg_remainingTime.timeMilliseconds = 9
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Add a position command to the API buffer
posCommand.target = 333
posCommand.profile.velocity = 3000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()
# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete.
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)

# Task 3: Establish a Normal type E-CAM motion for master Axis 4 and slave Axis 6.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a command value with a target value of -100.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# The following example illustrates a typical Normal type E-CAM table:
#   Master Axis Position      Slave Axis Position
#   -100                      100
#   -50                       150
#   0                         100
#   50                        50
#   100                       100
#   150                       50
#   250                       150

ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
# The master input is the command position of the master axis.
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
# PyNone: When the E-CAM is activated, the slave axis synchronizes with the master axis immediately.
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
# In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to track the speed of the master-slave curve in the E-CAM table.
ECAMoption.clutch.simpleCatchUpVelocity = 1000
# In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to catch up with the acceleration and deceleration of the master-slave curve in the E-CAM table.
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

# Create a command value with a target value of 300.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
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
