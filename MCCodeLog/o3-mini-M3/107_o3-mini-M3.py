
# Axes = [7, 9]
# IOInputs = []
# IOOutputs = [0.7]

# Move Axis 7 to position 220 with speed 1500.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 220
posCommand.profile.velocity = 1500
# Use default acceleration and deceleration values.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error moving Axis 7:", ret)
# Wait until Axis 7 finishes the move.
Wmx3Lib_cm.motion.Wait(7)

# Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0.
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x01)
if ret != 0:
    print("Error setting IO output bit 0.7:", ret)

sleep(0.2)

ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x00)
if ret != 0:
    print("Error resetting IO output bit 0.7:", ret)

# Start an absolute linear interpolation for Axes 7 and 9 to position (200, 50) with a velocity of 1200.
lin_cmd = Motion_LinearIntplCommand()
lin_cmd.axisCount = 2
lin_cmd.SetAxis(0, 7)
lin_cmd.SetAxis(1, 9)
lin_cmd.profile.type = ProfileType.Trapezoidal
lin_cmd.profile.velocity = 1200
lin_cmd.profile.acc = 10000
lin_cmd.profile.dec = 10000
lin_cmd.SetTarget(0, 200)  # Position for Axis 7.
lin_cmd.SetTarget(1, 50)   # Position for Axis 9.

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin_cmd)
if ret != 0:
    print("Error starting absolute linear interpolation:", ret)

# Wait for Axes 7 and 9 to complete their interpolation.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error while waiting for Axes 7 and 9 (absolute):", ret)

# Start a relative linear interpolation for Axes 7 and 9 to move by (-100, 50).
# In a relative command, the targets are treated as distances.
lin_cmd.SetTarget(0, -100)  # Relative distance for Axis 7.
lin_cmd.SetTarget(1, 50)    # Relative distance for Axis 9.

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin_cmd)
if ret != 0:
    print("Error starting relative linear interpolation:", ret)

# Wait for Axes 7 and 9 to complete the relative move.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error while waiting for Axes 7 and 9 (relative):", ret)
