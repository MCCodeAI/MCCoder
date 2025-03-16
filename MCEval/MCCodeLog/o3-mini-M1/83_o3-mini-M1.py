
# Axes = [5]
# IOInputs = []
# IOOutputs = [3.4]

# Create an API buffer to execute a conditional motion command.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Configure the position command for Axis 5.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Set the condition: if IO output at byte 3, bit 4 equals 1.
cond.bufferConditionType = ApiBufferConditionType.IOOutput
cond.arg_ioOutput.byteAddress = 3
cond.arg_ioOutput.bitAddress = 4

# Start the IF branch.
Wmx3Lib_buf.FlowIf(cond)

# IF branch: move Axis 5 by a relative distance of 200.
posCommand.axis = 5
posCommand.target = 200
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code in IF branch: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # If desired, add proper error handling or return.
    return

# End the IF branch and start the ELSE branch.
Wmx3Lib_buf.FlowElse()

# ELSE branch: move Axis 5 by a relative distance of -140.
posCommand.axis = 5
posCommand.target = -140
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code in ELSE branch: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Complete the conditional structure.
Wmx3Lib_buf.FlowEndIf()

# End recording the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the API buffer.
Wmx3Lib_buf.Execute(0)

# Wait for Axis 5 to stop moving after the motion command completes.
Wmx3Lib_cm.motion.Wait(5)

# Clean up API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
