
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Assuming that Wmx3Lib, Wmx3Lib_cm, and the required classes (ApiBuffer, ApiBufferCondition, 
# ApiBufferConditionType, Motion_PosCommand, ProfileType) are already defined in the environment.

# Create and configure the API buffer for channel 0
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Create a condition object to wait for specific remaining time events
cond = ApiBufferCondition()

# --- First Motion Command: Move Axis 3 to position 111 at a speed of 1000 ---
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 111
posCommand.profile.velocity = 1000
# Set acceleration and deceleration for smooth motion (values chosen arbitrarily)
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the first absolute position command on Axis 3
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # In a real application, you might exit or handle the error accordingly.
    
# Wait for the command to nearly complete, i.e. when remaining time is 8 ms on Axis 3.
cond.bufferConditionType = ApiBufferConditionType.RemainingTime
cond.arg_remainingTime.axis = 3
cond.arg_remainingTime.timeMilliseconds = 8
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# --- Second Motion Command: Move Axis 3 to position 222 at a speed of 2000 ---
# Update the position command parameters for the new target and speed.
posCommand.target = 222
posCommand.profile.velocity = 2000
# You can adjust acceleration/deceleration if needed; here we keep them the same.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    
# Wait until the remaining time on Axis 3 is 9 ms.
cond.arg_remainingTime.timeMilliseconds = 9
Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

# --- Third Motion Command: Move Axis 3 to position 333 at a speed of 3000 ---
posCommand.target = 333
posCommand.profile.velocity = 3000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# End the recording of commands for the API buffer on channel 0.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer which will run the sequence
Wmx3Lib_buf.Execute(0)

# Wait for Axis 3 to complete its motion before finishing.
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Free the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
