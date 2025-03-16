
# Axes = [6, 7, 8]
# Inputs = []
# Outputs = [6.7]

# Move Axis 6 to 20 with a velocity of 900 using a trapezoid profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x06, 0x07, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

sleep(0.1)

ret = Wmx3Lib_Io.SetOutBit(0x06, 0x07, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Move Axis 7 to 30
posCommand.axis = 7
posCommand.target = 30
posCommand.profile.velocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)

# Linearly interpolate Axis 7 and 8 to (40, 50)
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 8)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 40)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion command for Axis 6 and 7, with a center position of (50, 50), an arc length of 360
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand.SetAxis(0, 6)
circularIntplCommand.SetAxis(1, 7)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 50)
circularIntplCommand.clockwise = 1
circularIntplCommand.arcLengthDegree = 360
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1000
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 6)
axes.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Establish synchronous control between master axis 6 and slave axis 7, then move Axis 6 to position 60
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
Wmx3Lib_cm.motion.Wait(6)

# Release the synchronization between Axis 6 and Axis 7
ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
