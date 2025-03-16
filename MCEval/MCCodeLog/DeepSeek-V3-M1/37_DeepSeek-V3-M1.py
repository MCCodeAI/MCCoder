
# Axes = [6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
bufStatus = ApiBufferStatus()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Loop to move Axis 6 to position i*10 for 6 times
for i in range(1, 7):
    # Set i = 1 when even and i = -1 when odd
    if i % 2 == 0:
        i_value = 1
    else:
        i_value = -1

    # Add a position command to the API buffer.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = i_value * 10
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified relative position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 6 to stop moving before the next motion
    Wmx3Lib_buf.Wait(6)

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()
# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Check the status periodically to see if execution has finished
counter = 50
while True:
    ret, bufStatus = Wmx3Lib_buf.GetStatus(0)
    sleep(0.01)
    counter = counter - 1
    if (bufStatus.remainingBlockCount <= 0 and counter <= 0):
        break

# Wait for Axis 6 to complete motion
Wmx3Lib_cm.motion.Wait(6)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
