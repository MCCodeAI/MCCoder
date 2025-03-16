
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create an API buffer instance for recording commands.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)

# Create a buffer with a 3MB size for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)

# Start recording commands on channel 0.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Create a condition object to wait for a specific remaining time.
cond = ApiBufferCondition()

# -------------------------
# First Motion: Move Axis 3 to target position 111 at a speed of 1000.
# -------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 111
posCommand.profile.velocity = 1000
posCommand.profile.endVelocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for the remaining time to be 8 ms before adding the next command.
cond.bufferConditionType = ApiBufferConditionType.RemainingTime
cond.arg_remainingTime.axis = 3
cond.arg_remainingTime.timeMilliseconds = 8
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# -------------------------
# Second Motion: Move Axis 3 to target position 222 at a speed of 2000.
# -------------------------
posCommand.target = 222
posCommand.profile.velocity = 2000
posCommand.profile.endVelocity = 2000
# Optionally adjust accelerations if needed.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for the remaining time to be 9 ms before adding the next command.
cond.arg_remainingTime.timeMilliseconds = 9
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# -------------------------
# Third Motion: Move Axis 3 to target position 333 at a speed of 3000.
# -------------------------
posCommand.target = 333
posCommand.profile.velocity = 3000
posCommand.profile.endVelocity = 3000
# Optionally adjust accelerations if needed.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# End recording commands.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer on channel 0.
Wmx3Lib_buf.Execute(0)

# Wait for Axis 3 to finish moving.
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Cleanup: Halt and free the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
