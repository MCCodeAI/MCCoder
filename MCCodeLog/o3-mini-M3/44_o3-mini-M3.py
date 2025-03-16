
from time import sleep

# ---------- Absolute Position Triggered Linear Interpolation ----------
# This script performs an absolute position triggered linear interpolation.
# It linearly interpolates Axis 4 and Axis 5 to positions 100 and 50 respectively
# at a velocity of 1000 with acceleration and deceleration of 10000.
# When the remaining distance (DistanceToTarget) equals 20, a trigger causes Axis 8 to move to 200.
#
# Note: Do not import any motion libraries. It is assumed that the motion system API objects and functions
# (such as Motion_LinearIntplCommand, Trigger, Wmx3Lib_cm.motion.StartLinearIntplPos, etc.)
# are already available in the runtime environment.
#
# IMPORTANT: Wait for axes to stop moving after the complete motion command, but do not wait in the middle
# of continuous motion.

# Create and configure the linear interpolation command
lin = Motion_LinearIntplCommand()
trig = Trigger()

# Combine all three axes:
# Axis 4 and Axis 5 - primary (continuous) interpolation axes.
# Axis 8 - triggered axis.
lin.axisCount = 3
lin.SetAxis(0, 4)  # Primary interpolation: Axis 4
lin.SetAxis(1, 5)  # Primary interpolation: Axis 5
lin.SetAxis(2, 8)  # Triggered axis: Axis 8

# Set the common profile parameters
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the target positions for the interpolation:
# For Axis 4 and Axis 5, assign the new target positions.
lin.SetTarget(0, 100)  # Move Axis 4 to 100
lin.SetTarget(1, 50)   # Move Axis 5 to 50
# For Axis 8 (triggered axis), keep its current value until the trigger updates it.
lin.SetTarget(2, 0)    # Assume Axis 8 is initially at 0

# Start the primary absolute position interpolation for Axis 4 and Axis 5.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print("StartLinearIntplPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Do NOT wait here because the motion is continuous.

# Now, set up the trigger move for Axis 8:
# Update the target position for Axis 8 to 200.
lin.SetTarget(2, 200)

# Configure the trigger so that when the remaining distance (DistanceToTarget) equals 20,
# the command for Axis 8 will be executed.
trig.triggerAxis = 2           # Corresponding to Axis 8 (third axis in lin)
trig.triggerType = TriggerType.RemainingDistance
trig.triggerValue = 20

# Append the trigger command to the continuous motion.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print("StartLinearIntplPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for all axes (Axis 4, 5, and 8) to finish their motion.
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
axisSel.SetAxis(2, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# ---------- Sleep 1.6 Seconds ----------
# Pause execution for 1.6 seconds.
sleep(1.6)

# ---------- Set Output Bit 0.2 High then Low ----------
# Set output bit 0.2 to 1, wait 0.15 seconds, and then set it to 0.
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x01)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)

sleep(0.15)

ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x00)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)
