
# Axes = [6, 7, 8]
# IOInputs = []
# IOOutputs = [6.7]

# Task 1: Move Axis 6 to 20 with trapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error code for Axis 6: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

Wmx3Lib_cm.motion.Wait(6)

# Task 2: Set output 6.7 to 1, sleep, then 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(6, 7, 1)
if ret != 0:
    print(f'SetOutBit error setting 6.7 to 1: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
    return

sleep(0.1)

ret = Wmx3Lib_Io.SetOutBit(6, 7, 0)
if ret != 0:
    print(f'SetOutBit error setting 6.7 to 0: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
    return

# Task 3: Move Axis 7 to 30
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 30
posCommand.profile.velocity = 1000  # Default assumption
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error code for Axis 7: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

Wmx3Lib_cm.motion.Wait(7)

# Task 4: Linear interpolate Axis 7 & 8 to (40, 50)
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 8)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000  # Default assumption
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 40)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print(f'StartLinearIntplPos error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Task 5: Clockwise circular interpolation for Axis 6 & 7
cir = Motion_CenterAndLengthCircularIntplCommand()
cir.SetAxis(0, 6)
cir.SetAxis(1, 7)
cir.SetCenterPos(0, 50)
cir.SetCenterPos(1, 50)
cir.clockwise = 1
cir.arcLengthDegree = 360
cir.profile.type = ProfileType.Trapezoidal
cir.profile.velocity = 1000  # Default assumption
cir.profile.acc = 10000
cir.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cir)
if ret != 0:
    print(f'StartCircularIntplPos error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Task 6: Establish sync control and move Axis 6 to 60
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print(f'SetSyncMasterSlave error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 900  # Same as Task 1
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error for Axis 6 sync move: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

Wmx3Lib_cm.motion.Wait(6)

ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print(f'ResolveSync error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return
