
# Axes = [1, 9]
# IOInputs = []
# IOOutputs = []

# Create and configure the API buffer
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
opt = ApiBufferOptions()

# Clear the buffer of the specified channel.
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel.
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording on the specified channel.
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Prepare the motion command.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.velocity = 1300  # Set the given speed

# ------------------------------
# Command for Axis 9 (relative move of 50)
posCommand.axis = 9
posCommand.target = 50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error for Axis 9: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 9 stops moving.
Wmx3Lib_buf.Wait(9)

# ------------------------------
# Command for Axis 1 (relative move of 60)
posCommand.axis = 1
posCommand.target = 60
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error for Axis 1: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 stops moving.
Wmx3Lib_buf.Wait(1)

# End recording the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()

# Execute the recorded buffer commands.
Wmx3Lib_buf.Execute(0)

# Delay to ensure the execution phase has time to start (if needed).
sleep(3)

# Rewind the API buffer.
Wmx3Lib_buf.Rewind(0)

# Optionally, wait again to make sure both axes have finished the rewound execution.
Wmx3Lib_buf.Wait(9)
Wmx3Lib_buf.Wait(1)

# Halt and free the API buffer resources.
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
