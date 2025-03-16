
# Axes = [3, 4, 6]
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

cond = ApiBufferCondition()

# Add position commands for Axis 3 and 4
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 36
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 4
posCommand.target = 45

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to finish moving
Wmx3Lib_buf.Wait(3)
Wmx3Lib_buf.Wait(4)

# Add position command for Axis 6
posCommand.axis = 6
posCommand.target = 108

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End recording and execute the buffer
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for all motions to complete
counter = 50
while True:
    ret, bufStatus = Wmx3Lib_buf.GetStatus(0)
    sleep(0.01)
    counter -= 1
    if bufStatus.remainingBlockCount <= 0 and counter <= 0:
        break

# Wait for individual axes to stop
Wmx3Lib_cm.motion.Wait(3)
Wmx3Lib_cm.motion.Wait(4)
Wmx3Lib_cm.motion.Wait(6)

# Clean up buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
