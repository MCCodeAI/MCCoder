
# Axes = [6, 8]
# IOInputs = []
# IOOutputs = []

# Record and execute an API buffer that moves:
# - Axis 6 to position 150,
# - Axis 8 to position 180.
# After each motion command, wait for the axis to stop moving.

# Assume that objects such as Wmx3Lib, Wmx3Lib_cm, ApiBuffer, Motion_PosCommand,
# ProfileType, and AxisSelection are already defined and available in the environment.

# Create an instance of the API buffer for the motion system.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer for channel 0.
Wmx3Lib_buf.Clear(0)

# Create a buffer for channel 0 with a size of 3 MB.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)

# Start recording into the API buffer on channel 0.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# -------------------------
# Command 1: Move Axis 6 to position 150.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error for Axis 6: code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    # Terminate or handle the error as appropriate.
    exit(1)

# Wait until the motion for this segment is finished.
Wmx3Lib_buf.Wait(0)

# -------------------------
# Command 2: Move Axis 8 to position 180.
posCommand.axis = 8
posCommand.target = 180
# Optionally reassign velocity, acceleration and deceleration if different parameters are required:
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error for Axis 8: code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until the motion for this segment is finished.
Wmx3Lib_buf.Wait(1)

# End the recording of the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer on channel 0.
Wmx3Lib_buf.Execute(0)

# -------------------------
# Wait for both Axis 6 and Axis 8 to complete their motions.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Clean up: Halt and free API buffer resources on channel 0.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
