
# Axes = [6, 8]
# Inputs = []
# Outputs = []

# Move Axis 6 to position 220 with a speed of 1600
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 220
posCommand.profile.velocity = 1600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Move Axis 6 as a distance of 110 with a speed of 600
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 110
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to a specified distance relatively.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Start an absolute linear interpolation for Axes 6 and 8 to position (200, 50) with a velocity of 1100
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 6)
lin.SetAxis(1, 8)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1100
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 200)  # Set target of Axis 6
lin.SetTarget(1, 50)   # Set target of Axis 8

# Start an absolute position linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 6 and Axis 8 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
