
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Jog Axis 3 for 0.5 seconds with a velocity of 90
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 3
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

# Start jogging
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 0.5 seconds
sleep(0.5)

# Stop jogging
Wmx3Lib_cm.motion.Stop(3)

# Wait for Axis 3 to stop
Wmx3Lib_cm.motion.Wait(3)

# Get the Axis status for Axis 3
axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(3)
actualPos = axisStatus.actualPosition

# Move Axis 3 based on Actual Pos
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

if actualPos > 20:
    posCommand.target = 150
else:
    posCommand.target = -150

# Execute command to move Axis 3
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 to stop
Wmx3Lib_cm.motion.Wait(3)

# Start an absolute linear interpolation for Axes 1 and 3 to position (100, 0) with a velocity of 1000
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 3)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)  # Set target of Axis 1 to be 100
lin.SetTarget(1, 0)    # Set target of Axis 3 to be 0

# Start an absolute position linear interpolation motion command
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
