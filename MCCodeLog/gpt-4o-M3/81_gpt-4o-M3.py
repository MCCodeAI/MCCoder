
# Axes = [1, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
opt = ApiBufferOptions()

# Clear the buffer on the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add a position command for Axis 9 to the API buffer.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.target = 50
posCommand.profile.velocity = 1300
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 9 to the specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 9 to complete its motion.
Wmx3Lib_buf.Wait(9)

# Add a position command for Axis 1 to the API buffer.
posCommand.axis = 1
posCommand.target = 60
# Execute command to move Axis 1 to the specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to complete its motion.
Wmx3Lib_buf.Wait(1)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Set the API buffer execution options
opt.autoRewind = True
Wmx3Lib_buf.SetOptions(0, opt)

# Rewind the API buffer.
Wmx3Lib_buf.Rewind(0)

# Wait for both axes to complete motion
Wmx3Lib_cm.motion.Wait(9)
Wmx3Lib_cm.motion.Wait(1)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
