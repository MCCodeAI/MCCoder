
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Start relative motion for Axes 4 and 6 in three sequential steps.
# Each motion command waits for the axes to stop moving before starting the next command.

# First relative motion: move by (100, -100) with a velocity of 900.
lin1 = Motion_LinearIntplCommand()
lin1.axisCount = 2
lin1.SetAxis(0, 4)   # Assign Axis 4
lin1.SetAxis(1, 6)   # Assign Axis 6

lin1.profile.type = ProfileType.Trapezoidal
lin1.profile.velocity = 900
lin1.profile.acc = 10000   # Acceleration (example value)
lin1.profile.dec = 10000   # Deceleration (example value)

lin1.SetTarget(0, 100)     # Relative move for Axis 4: +100
lin1.SetTarget(1, -100)    # Relative move for Axis 6: -100

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin1)
if ret != 0:
    print('StartLinearIntplMov (first motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until both Axis 4 and Axis 6 have completed the motion.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after first motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Second relative motion: move by (-100, 0) with the same velocity.
lin2 = Motion_LinearIntplCommand()
lin2.axisCount = 2
lin2.SetAxis(0, 4)
lin2.SetAxis(1, 6)

lin2.profile.type = ProfileType.Trapezoidal
lin2.profile.velocity = 900
lin2.profile.acc = 10000
lin2.profile.dec = 10000

lin2.SetTarget(0, -100)    # Relative move for Axis 4: -100
lin2.SetTarget(1, 0)       # Relative move for Axis 6: 0

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin2)
if ret != 0:
    print('StartLinearIntplMov (second motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until both Axis 4 and Axis 6 are idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after second motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Third relative motion: move by (0, 100) with the same velocity.
lin3 = Motion_LinearIntplCommand()
lin3.axisCount = 2
lin3.SetAxis(0, 4)
lin3.SetAxis(1, 6)

lin3.profile.type = ProfileType.Trapezoidal
lin3.profile.velocity = 900
lin3.profile.acc = 10000
lin3.profile.dec = 10000

lin3.SetTarget(0, 0)      # Relative move for Axis 4: 0
lin3.SetTarget(1, 100)    # Relative move for Axis 6: +100

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin3)
if ret != 0:
    print('StartLinearIntplMov (third motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Final wait until both Axis 4 and Axis 6 have completed the last move.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after third motion) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

print("All relative interpolation motions for Axes 4 and 6 have been completed successfully.")
