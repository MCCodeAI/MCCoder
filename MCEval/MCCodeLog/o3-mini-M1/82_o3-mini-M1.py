
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

# --- First Motion: Move Axis 5 to a relative position of +150 at a speed of 1500 ---
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 150
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 5 to +150.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 5 stops moving.
Wmx3Lib_buf.Wait(5)

# --- Second Motion: Move Axis 5 to a relative position of -150 at the same speed ---
posCommand.target = -150

# Execute command to move Axis 5 to -150.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 5 stops moving.
Wmx3Lib_buf.Wait(5)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()

# Enable Auto Rewind.
opt.autoRewind = True
Wmx3Lib_buf.SetOptions(0, opt)

# Execute the buffered API commands.
Wmx3Lib_buf.Execute(0)

# Auto rewind buffer and stop the execution after 0.5 seconds.
sleep(0.5)

# Halt and free the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
