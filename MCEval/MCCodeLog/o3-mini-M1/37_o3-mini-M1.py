
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Record and execute an API buffer to move Axis 6.
# For 6 iterations, set i = 1 for even iterations and i = -1 for odd iterations.
# Then move Axis 6 to position = i * 10.
#
# Note: After each motion command, the code waits for Axis 6 to stop moving.

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel (allocate 3 MB).
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Loop 6 times to record the sequence of motion commands.
for idx in range(6):
    # Set i = 1 when the iteration index is even, and i = -1 when odd.
    if idx % 2 == 0:
        sign = 1
    else:
        sign = -1
    target_position = sign * 10

    # Create a motion position command for Axis 6.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = target_position
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute the relative move command.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print("StartMov error code is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait here for Axis 6 to stop moving before proceeding to the next command.
    Wmx3Lib_buf.Wait(6)

# End recording the API buffer commands.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer.
Wmx3Lib_buf.Execute(0)

# Optionally, ensure Axis 6 has completely finished motion after buffer execution.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print("Wait error code is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))

# Clean up API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
