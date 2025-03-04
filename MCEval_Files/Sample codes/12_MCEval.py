# Write python code to Create and execute a cyclic buffer memory space for Axis 4, to pisition 100 within 200 cycles, then move a relative 0 distance within 600 cycles, then to pisition -100 within 200 cycles, then sleep 1.5s, and close the cyclic buffer.
    # Axes = [4]

    Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

    # Create a new cyclic buffer memory space for Axis 4, with a size of 1,024 cycles.
    ret = Wmx3Lib_cyc.OpenCyclicBuffer(4, 1024)
    if ret != 0:
        print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Start the execution of the cyclic position command buffer for Axis 4.
    ret = Wmx3Lib_cyc.Execute(4)
    if ret != 0:
        print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Dynamically add points to move from the current position to the absolute position of 100 within 200 cycles.
    cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicBufferSingleAxisCommand.intervalCycles = 200
    cyclicBufferSingleAxisCommand.command = 100
    ret = Wmx3Lib_cyc.AddCommand(4, cyclicBufferSingleAxisCommand)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # The relative position is 0, which means there was no movement for 600 cycles from the previous position.
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
    cyclicBufferSingleAxisCommand.intervalCycles = 600
    cyclicBufferSingleAxisCommand.command = 0
    ret = Wmx3Lib_cyc.AddCommand(4, cyclicBufferSingleAxisCommand)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Move from the current position to the absolute position of -100 within 200 cycles.
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicBufferSingleAxisCommand.intervalCycles = 200
    cyclicBufferSingleAxisCommand.command = -100
    ret = Wmx3Lib_cyc.AddCommand(4, cyclicBufferSingleAxisCommand)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Wait for Cyclic buffer executing to end
    while True:
        ret,cyc_Status=Wmx3Lib_cyc.GetStatus(4)
        if(cyc_Status.remainCount<=0):
            break
        sleep(0.1)

    # Wait for 1.5 seconds
    sleep(1.5)

    # Close the cyclic buffer memory space.
    ret = Wmx3Lib_cyc.CloseCyclicBuffer(4)
    if ret != 0:
        print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

