
# Axes = [3]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add a position command to the API buffer.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 111
posCommand.profile.velocity = 1000
posCommand.profile.endVelocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for position command to have 8ms remaining time
cond.bufferConditionType = ApiBufferConditionType.RemainingTime
cond.arg_remainingTime.axis = 3
cond.arg_remainingTime.timeMilliseconds = 8
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Add a position command to the API buffer
posCommand.target = 222
posCommand.profile.velocity = 2000
posCommand.profile.endVelocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for position command to have 9ms remaining time
cond.arg_remainingTime.timeMilliseconds = 9
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# Add a position command to the API buffer
posCommand.target = 333
posCommand.profile.velocity = 3000
posCommand.profile.endVelocity = 3000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End Recording.
Wmx3Lib_buf.EndRecordBufferChannel()
# Drive the motion accumulated in the buffer so far.
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 3 becomes idle.
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Destroy API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
