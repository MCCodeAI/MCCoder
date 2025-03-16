
# Axes = [7, 9]
# IOInputs = []
# IOOutputs = [0.7]

# Move Axis 7 to position 220 with a speed of 1500
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 220
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(7)

# Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0
Wmx3Lib_cm.io.SetOutput(0, 7, 1)
sleep(0.2)
Wmx3Lib_cm.io.SetOutput(0, 7, 0)

# Start an absolute linear interpolation for Axes 7 and 9 to position (200, 50) with a velocity of 1200
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1200
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 200)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Start a relative linear interpolation for Axes 7 and 9 to position (-100, 50)
lin.SetTarget(0, -100)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 7 and Axis 9 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
