
# Axes = [1, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add a position command to the API buffer for Axis 1
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 60
posCommand.profile.velocity = 1300
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Pause execution until Axis 1 has finished motion
Wmx3Lib_buf.Wait(1)

# Add a position command to the API buffer for Axis 9
posCommand.axis = 9
posCommand.target = 50
posCommand.profile.velocity = 1300
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Pause execution until Axis 9 has finished motion
Wmx3Lib_buf.Wait(9)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete
Wmx3Lib_cm.motion.Wait(1)
Wmx3Lib_cm.motion.Wait(9)

# Rewind the API buffer
Wmx3Lib_buf.Rewind(0)

# Wait for the motion to complete after rewind
Wmx3Lib_cm.motion.Wait(1)
Wmx3Lib_cm.motion.Wait(9)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
