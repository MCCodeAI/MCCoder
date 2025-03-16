
# Axes = [9]
# Inputs = []
# Outputs = []

Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Create a new cyclic buffer memory space for Axis 9, with a size of 1,024 cycles.
ret = Wmx3Lib_cyc.OpenCyclicBuffer(9, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Start the execution of the cyclic position command buffer for Axis 9.
ret = Wmx3Lib_cyc.Execute(9)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move to the absolute position of 60 within 100 cycles.
cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 60
ret = Wmx3Lib_cyc.AddCommand(9, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move a relative distance of 140 within 100 cycles.
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 140
ret = Wmx3Lib_cyc.AddCommand(9, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move to the absolute position of -100 within 200 cycles.
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 200
cyclicBufferSingleAxisCommand.command = -100
ret = Wmx3Lib_cyc.AddCommand(9, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Wait for Cyclic buffer executing to end
while True:
    ret, cyc_Status = Wmx3Lib_cyc.GetStatus(9)
    if cyc_Status.remainCount <= 0:
        break
    sleep(0.1)

# Close the cyclic buffer memory space.
ret = Wmx3Lib_cyc.CloseCyclicBuffer(9)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return
