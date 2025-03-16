
# Axes = [0, 3]
# IOInputs = []
# IOOutputs = []

# This script first moves Axis 0 and Axis 3 to the absolute position (80, 0)
# at a velocity of 1500. Once that motion has completed, it executes three trigger‐based
# linear interpolation motions. When the remaining distance (on Axis 0) equals 10,
# it triggers the interpolation to (80, 80), then (0, 80), and finally (0, 0).
# After each motion command, the script waits for the axes to finish moving before
# issuing the next command.

from time import sleep

# Move axes using absolute linear interpolation command
lin = Motion_LinearIntplCommand()
trig = Trigger()

# Configure for two axes: mapping index 0 -> Axis 0, index 1 -> Axis 3
lin.axisCount = 2
lin.SetAxis(0, 0)
lin.SetAxis(1, 3)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1500
lin.profile.acc = 10000
lin.profile.dec = 10000

# First absolute motion to (80, 0): Axis 0 -> 80, Axis 3 -> 0.
lin.SetTarget(0, 80)
lin.SetTarget(1, 0)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print("StartLinearIntplPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()  # Early exit on error

# Wait for the motion to complete (axes become idle)
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Configure the trigger condition: trigger when the remaining distance (Axis 0) equals 10.
trig.triggerAxis = 0
trig.triggerType = TriggerType.RemainingDistance
trig.triggerValue = 10

# --- Triggered Motion 1: move to (80, 80) ---
sleep(0.001)   # short delay before trigger command

lin.SetTarget(0, 80)  # Axis 0 target: 80
lin.SetTarget(1, 80)  # Axis 3 target: 80

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print("StartLinearIntplPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# --- Triggered Motion 2: move to (0, 80) ---
sleep(0.001)   # short delay before next trigger command

lin.SetTarget(0, 0)   # Axis 0 target: 0
lin.SetTarget(1, 80)  # Axis 3 target remains 80

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print("StartLinearIntplPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# --- Triggered Motion 3: move to (0, 0) ---
sleep(0.001)   # short delay before next trigger command

lin.SetTarget(0, 0)   # Axis 0 target remains 0
lin.SetTarget(1, 0)   # Axis 3 target: 0

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print("StartLinearIntplPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

print("All motions completed successfully.")
