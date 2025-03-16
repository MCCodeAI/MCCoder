
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Task 1: Absolute position path interpolation motion for Axis 4 and 6
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 4)
path.SetAxis(1, 6)

path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

path.enableAutoSmooth = 1

path.numPoints = 6

positions = [
    (-40, -30, 10),
    (10, -50, 20),
    (-40, -70, 30),
    (10, -90, 40),
    (-40, -110, 50),
    (10, -130, 0)
]

for i in range(6):
    path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, i, positions[i][0])
    path.SetTarget(1, i, positions[i][1])
    if i < 5:
        path.SetAutoSmoothRadius(i, positions[i][2])

ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print(f'StartPathIntplPos error: {Wmx3Lib_adv.ErrorToString(ret)}')
    exit()

axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 4)
axes.SetAxis(1, 6)
Wmx3Lib_cm.motion.Wait_AxisSel(axes)

# Task 2: API buffer sequence for Axis 4
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# First move
posCommand.target = 111
posCommand.profile.velocity = 1000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()

cond = ApiBufferCondition()
cond.bufferConditionType = ApiBufferConditionType.RemainingTime
cond.arg_remainingTime.axis = 4
cond.arg_remainingTime.timeMilliseconds = 8
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Second move
posCommand.target = 222
posCommand.profile.velocity = 2000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()

cond.arg_remainingTime.timeMilliseconds = 9
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Third move
posCommand.target = 333
posCommand.profile.velocity = 3000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()

Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)
Wmx3Lib_cm.motion.Wait(4)
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)

# Task 3: E-CAM motion for Axis 4 and 6
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Move Axis 4 to -100
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()
Wmx3Lib_cm.motion.Wait(4)

# Setup E-CAM
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()
ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone

ECAMdata.masterAxis = 4
ECAMdata.slaveAxis = 6
ECAMdata.numPoints = 7
ECAMdata.options = ECAMoption

master_pos = [-100, -50, 0, 50, 100, 150, 250]
slave_pos = [100, 150, 100, 50, 100, 50, 150]

for i in range(7):
    ECAMdata.SetMasterPos(i, master_pos[i])
    ECAMdata.SetSlavePos(i, slave_pos[i])

ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print(f'StartECAM error: {Wmx3Lib.ErrorToString(ret)}')
    exit()

# Move Axis 4 to 300
posCommand.target = 300
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()
Wmx3Lib_cm.motion.Wait(4)

# Stop E-CAM
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print(f'StopECAM error: {Wmx3Lib.ErrorToString(ret)}')
