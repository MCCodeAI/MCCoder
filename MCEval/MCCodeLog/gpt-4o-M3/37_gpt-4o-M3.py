
# Axes = [6]
# Inputs = []
# Outputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add a position command to the API buffer.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000  # Assuming a default acceleration
posCommand.profile.dec = 10000  # Assuming a default deceleration

# Loop to move Axis 6 to position i*10 for 6 times
for i in range(6):
    # Set i = 1 when even and i = -1 when odd
    multiplier = 1 if i % 2 == 0 else -1
    posCommand.target = multiplier * 10

    # Execute command to move to a specified position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait for the axis to complete motion before the next iteration
    Wmx3Lib_cm.motion.Wait(6)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()
# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for the axis 6 motion to complete.
Wmx3Lib_cm.motion.Wait(6)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
