
# Axes = [0, 3]
# IOInputs = []
# IOOutputs = []

# Create the motion command object and trigger object for the interpolation commands.
lin = Motion_LinearIntplCommand()
trig = Trigger()

# -------------------------------
# Step 1: Execute initial linear interpolation to (80, 0)
# -------------------------------

# Configure the command for 2 axes: index 0 for Axis 0 and index 1 for Axis 3.
lin.axisCount = 2
lin.SetAxis(0, 0)  # Map first command axis to Axis 0
lin.SetAxis(1, 3)  # Map second command axis to Axis 3

# Set the motion profile parameters.
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1500
lin.profile.acc = 10000  # Acceleration value (assumed)
lin.profile.dec = 10000  # Deceleration value (assumed)

# Set the target position for the initial move: (80, 0)
lin.SetTarget(0, 80)  # Target for Axis 0
lin.SetTarget(1, 0)   # Target for Axis 3

# Start the absolute position linear interpolation motion.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the motion on Axis 0 and Axis 3 completes.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# -------------------------------
# Step 2: Triggered interpolation to (80, 80) when remaining distance is 10
# -------------------------------

# Configure the trigger parameters.
trig.triggerAxis = 0  # Monitor Axis 0 for triggering
trig.triggerType = TriggerType.RemainingDistance
trig.triggerValue = 10

# Prepare the next interpolation target: (80, 80) for Axis 0 and Axis 3.
lin.SetTarget(0, 80)  # Axis 0 remains 80
lin.SetTarget(1, 80)  # Axis 3 moves to 80

# Brief pause before starting the triggered motion.
sleep(0.001)

# Start the triggered interpolation motion.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger (to 80,80) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until motion completes.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after 80,80) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# -------------------------------
# Step 3: Triggered interpolation to (0, 80) when remaining distance is 10
# -------------------------------

# Update the next target: (0, 80)
lin.SetTarget(0, 0)   # Axis 0 moves to 0
lin.SetTarget(1, 80)  # Axis 3 remains 80

sleep(0.001)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger (to 0,80) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after 0,80) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# -------------------------------
# Step 4: Triggered interpolation to (0, 0) when remaining distance is 10
# -------------------------------

# Update the target to (0, 0) for both axes.
lin.SetTarget(0, 0)  # Axis 0 to 0
lin.SetTarget(1, 0)  # Axis 3 to 0

sleep(0.001)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger (to 0,0) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel (after 0,0) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
