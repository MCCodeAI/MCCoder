
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Get Axis 3 status and move it based on its Actual Pos value

# Retrieve the current status from the motion engine.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

axis_to_check = 3
actualPos = CmStatus.GetAxesStatus(axis_to_check).actualPos
print('Axis {} Actual Pos: {}'.format(axis_to_check, actualPos))

# Determine the target position for Axis 3 based on Actual Pos
if actualPos > 20:
    target_pos = 150
else:
    target_pos = -150

# Create and setup a position command for Axis 3
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis_to_check
posCommand.target = target_pos
posCommand.profile.velocity = 1000  # Using a standard velocity value (can be adjusted as needed)
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Initiate the move for Axis 3 and wait for it to complete
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(axis_to_check)

# Now, start an absolute linear interpolation for Axes 1 and 3 to drive them to (100, 0) with a velocity of 1000

# Prepare a linear interpolation command for two axes
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
# Map the command axes: index 0 corresponds to Axis 1; index 1 corresponds to Axis 3.
lin.SetAxis(0, 1)
lin.SetAxis(1, 3)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set target positions: Axis 1 moves to 100 and Axis 3 moves to 0.
lin.SetTarget(0, 100)
lin.SetTarget(1, 0)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until both Axis 1 and Axis 3 have finished moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
