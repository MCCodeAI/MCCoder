
# Axes = [5]
# IOInputs = []
# IOOutputs = [3.4]

# Create an API buffer and a condition object
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Set up the condition: If IO output 3.4 equals 1
cond.bufferConditionType = ApiBufferConditionType.IOOutput
cond.arg_ioOutput.byteAddress = 3
cond.arg_ioOutput.bitAddress = 4
Wmx3Lib_buf.FlowIf(cond)

# Inside IF block: Move Axis 5 by a distance of 200
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # In a real application, proper error handling would be implemented here.
    exit(1)

# Wait until Axis 5 completes its motion.
Wmx3Lib_cm.motion.Wait(5)

# ELSE branch: Otherwise, move Axis 5 by a distance of -140
Wmx3Lib_buf.FlowElse()

posCommand.axis = 5
posCommand.target = -140

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

Wmx3Lib_cm.motion.Wait(5)

# End the IF conditional block.
Wmx3Lib_buf.FlowEndIf()

# End recording to the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer.
Wmx3Lib_buf.Execute(0)

# Wait for Axis 5 to finish its motion if it hasn't already.
Wmx3Lib_cm.motion.Wait(5)

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
