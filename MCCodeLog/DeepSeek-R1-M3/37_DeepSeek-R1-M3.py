
# Axes = [6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
bufStatus = ApiBufferStatus()

# Clear the buffer of the specified channel
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel
Wmx3Lib_buf.StartRecordBufferChannel(0)

for step in range(1, 7):
    # Determine multiplier based on even/odd iteration
    i = 1 if step % 2 == 0 else -1
    target = i * 10

    # Configure position command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute relative move command
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print(f'StartMov error code: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    # Wait for axis to complete motion before next move
    Wmx3Lib_buf.Wait(6)

# Finalize recording and execute buffer
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Monitor buffer execution status
while True:
    ret, bufStatus = Wmx3Lib_buf.GetStatus(0)
    if bufStatus.remainingBlockCount <= 0:
        break
    sleep(0.01)

# Ensure final motion completion
Wmx3Lib_cm.motion.Wait(6)

# Release buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
