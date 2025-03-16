
# Axes = [8]
# IOInputs = [3.5]
# IOOutputs = []

# Create and record an API buffer based on the IO input condition.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
# Clear the buffer for channel 0.
Wmx3Lib_buf.Clear(0)
# Create a buffer (allocating 3 MB of space).
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording commands on channel 0.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Set the condition for IO input at byte 3, bit 5.
cond = ApiBufferCondition()
cond.bufferConditionType = ApiBufferConditionType.IOInput
cond.arg_ioInput.byteAddress = 3
cond.arg_ioInput.bitAddress = 5

# Use FlowIfNot to branch when IO input 3.5 equals 0.
# (Assuming that normally the condition is true when the input is 1,
# FlowIfNot will execute the branch when the input is 0.)
Wmx3Lib_buf.FlowIfNot(cond)

# Branch for IO input 3.5 equals 0: Move Axis 8 by a distance of 200.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Else branch: when IO input 3.5 does not equal 0, move Axis 8 by a distance of -140.
Wmx3Lib_buf.FlowElse()

# Reuse the position command for Axis 8 with modified target.
posCommand.target = -140

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End the conditional branch.
Wmx3Lib_buf.FlowEndIf()

# End the recording of the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer commands.
Wmx3Lib_buf.Execute(0)

# Wait for Axis 8 to stop moving.
Wmx3Lib_cm.motion.Wait(8)

# Clean up the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
