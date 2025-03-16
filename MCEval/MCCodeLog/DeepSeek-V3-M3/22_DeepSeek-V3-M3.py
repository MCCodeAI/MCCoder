
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# Execute an absolute linear interpolation for Axes 2 and 4 to position (-100, -50) with a velocity of 800 using a Jerk Limited profile with Acc as 8000 and jerkAcc as 20000.

lin = Motion_LinearIntplCommand()

# Execute absolute position linear interpolation motion command
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 4)

lin.profile.type = ProfileType.JerkLimited
lin.profile.velocity = 800
lin.profile.acc = 8000
lin.profile.jerkAcc = 20000  # Adjusted jerkAcc to a valid range

lin.SetTarget(0, -100)
lin.SetTarget(1, -50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 2 and Axis 4 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
