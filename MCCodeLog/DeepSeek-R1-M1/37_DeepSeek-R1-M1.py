
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

# Generate 6 movement commands with alternating i values
for count in range(1, 7):
    # Determine i based on even/odd iteration count (1-based)
    i = 1 if (count % 2 == 0) else -1
    target = i * 10

    # Configure position command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute absolute position command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        break

    # Wait for axis to complete motion before next command
    Wmx3Lib_buf.Wait(6)

# Finalize recording and execute buffer
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Monitor buffer execution status
counter = 50
while True:
    ret, bufStatus = Wmx3Lib_buf.GetStatus(0)
    sleep(0.01)
    counter -= 1
    if bufStatus.remainingBlockCount <= 0 and counter <= 0:
        break

# Cleanup resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
