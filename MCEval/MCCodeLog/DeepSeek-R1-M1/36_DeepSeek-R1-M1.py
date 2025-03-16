
# Axes = [6, 8]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Create a command value.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to specified absolute position
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(6)

posCommand.axis = 8
posCommand.target = 180
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to specified absolute position
Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(8)

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()
# Execute recorded buffer
Wmx3Lib_buf.Execute(0)

# Wait for motion completion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Cleanup resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
