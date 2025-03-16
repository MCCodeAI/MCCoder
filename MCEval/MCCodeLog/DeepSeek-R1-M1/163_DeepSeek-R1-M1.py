
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Jog Axis 3 for 0.5 seconds with 90 velocity
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 3
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

sleep(0.5)
Wmx3Lib_cm.motion.Stop(3)
Wmx3Lib_cm.motion.Wait(3)

# Get Axis 3 status
axisStatus = Axis_Status()
ret = Wmx3Lib_cm.motion.GetStatus(3, axisStatus)
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

actualPos = axisStatus.actualPos

# Move based on Actual Pos
if actualPos > 20:
    target = 150
else:
    target = -150

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = target
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

# Linear interpolation for Axes 1 and 3
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 3)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)  # Axis 1 target
lin.SetTarget(1, 0)    # Axis 3 target

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
