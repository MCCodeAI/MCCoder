
# Axes = [1, 9]
# IOInputs = []
# IOOutputs = []

# Initialize the API buffer objects and options
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
opt = ApiBufferOptions()

# Clear the buffer for channel 0 and create a new buffer
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)

# Start recording commands into the API buffer for channel 0
Wmx3Lib_buf.StartRecordBufferChannel(0)

# ---------------------------
# Command 1: Move Axis 9 to a relative position of 50 at a speed of 1300
# ---------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.target = 50
posCommand.profile.velocity = 1300
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 9 has stopped moving before recording the next command
Wmx3Lib_buf.Wait(9)

# ---------------------------
# Command 2: Move Axis 1 to a relative position of 60 at a speed of 1300
# ---------------------------
# Reuse posCommand object with updated parameters for Axis 1
posCommand.axis = 1
posCommand.target = 60
posCommand.profile.velocity = 1300  # same speed as before; acc & dec remain unchanged

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 1 has stopped moving
Wmx3Lib_buf.Wait(1)

# End recording the API buffer
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded API buffer (channel 0)
Wmx3Lib_buf.Execute(0)

# After execution, rewind the API buffer
Wmx3Lib_buf.Rewind(0)

# Optionally, wait again for each axis to ensure all motions are complete
Wmx3Lib_cm.motion.Wait(9)
Wmx3Lib_cm.motion.Wait(1)

# Destroy API buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
