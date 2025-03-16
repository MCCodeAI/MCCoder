
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Create an absolute linear interpolation motion command for Axes 1 and 3.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 3)

# Configure the motion profile with a trapezoidal profile.
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the target positions for each axis (Axis 1 to 100, Axis 3 to 100).
lin.SetTarget(0, 100)
lin.SetTarget(1, 100)

# Start the absolute position linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until both Axes 1 and 3 have stopped moving.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
