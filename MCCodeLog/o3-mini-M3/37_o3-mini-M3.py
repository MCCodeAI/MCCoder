
# Axes = [6]
# IOInputs = []
# IOOutputs = []

def main():
    # Create an API buffer instance for recording the motion commands.
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    
    # Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create the buffer (3 MB in size).
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording commands on channel 0.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    # Record 6 motion commands for Axis 6.
    # For each iteration, set i = 1 if the loop count is even, and i = -1 if odd.
    for count in range(1, 7):
        factor = 1 if (count % 2 == 0) else -1
        
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 6
        posCommand.target = factor * 10  # target position = i * 10
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        # Issue the motion command to move Axis 6.
        ret = Wmx3Lib_cm.motion.StartMov(posCommand)
        if ret != 0:
            print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until Axis 6 has completely stopped moving for this command.
        Wmx3Lib_buf.Wait(6)

    # End the record mode for the API buffer.
    Wmx3Lib_buf.EndRecordBufferChannel()

    # Execute the entire recorded API buffer.
    Wmx3Lib_buf.Execute(0)

    # Optionally, wait for the final motion on Axis 6 to complete.
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Clean up the buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

if __name__ == "__main__":
    main()
