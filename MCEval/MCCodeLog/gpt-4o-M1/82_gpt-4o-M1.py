
# Axes = [5]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
opt = ApiBufferOptions()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add a position command to the API buffer.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 150
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop moving
Wmx3Lib_cm.motion.Wait(5)

# Add a position command to the API buffer
posCommand.target = -150
# Execute command to move to a specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop moving
Wmx3Lib_cm.motion.Wait(5)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Set the API buffer execution options
opt.autoRewind = True
Wmx3Lib_buf.SetOptions(0, opt)

# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for 0.5 seconds after execution
sleep(0.5)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
