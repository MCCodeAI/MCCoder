
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# Create the motion command for absolute linear interpolation on Axes 2 and 4.
lin = Motion_LinearIntplCommand()

# This command will work with 2 axes.
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 4)

# Configure the motion profile as Jerk Limited.
lin.profile.type = ProfileType.JerkLimited
lin.profile.velocity = 800
lin.profile.acc = 8000
lin.profile.jerkAcc = 20000

# Set target positions: Axis 2 to -100, Axis 4 to -50.
lin.SetTarget(0, -100)
lin.SetTarget(1, -50)

# Start the absolute linear interpolation motion.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the motion for both axes is complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
