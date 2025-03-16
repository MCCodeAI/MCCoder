
# Axes = [9]
# IOInputs = []
# IOOutputs = []

import time

# Create a new cyclic buffer instance for Axis 9.
Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Open a cyclic buffer memory space for Axis 9 with a size of 1024 cycles.
ret = Wmx3Lib_cyc.OpenCyclicBuffer(9, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()

# Start the execution of the cyclic buffer for Axis 9.
ret = Wmx3Lib_cyc.Execute(9)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()

# Create and add a command to move from the current position to the absolute position 60 within 100 cycles.
cyclicCmd = CyclicBufferSingleAxisCommand()
cyclicCmd.type = CyclicBufferCommandType.AbsolutePos
cyclicCmd.intervalCycles = 100
cyclicCmd.command = 60
ret = Wmx3Lib_cyc.AddCommand(9, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()

# Add a command to move a relative distance of 140 within 100 cycles.
cyclicCmd.type = CyclicBufferCommandType.RelativePos
cyclicCmd.intervalCycles = 100
cyclicCmd.command = 140
ret = Wmx3Lib_cyc.AddCommand(9, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()

# Add a command to move to the absolute position -100 within 200 cycles.
cyclicCmd.type = CyclicBufferCommandType.AbsolutePos
cyclicCmd.intervalCycles = 200
cyclicCmd.command = -100
ret = Wmx3Lib_cyc.AddCommand(9, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()

# Wait for the cyclic buffer execution to finish.
while True:
    ret, cyc_Status = Wmx3Lib_cyc.GetStatus(9)
    if cyc_Status.remainCount <= 0:
        break
    time.sleep(0.1)

# Close the cyclic buffer memory space.
ret = Wmx3Lib_cyc.CloseCyclicBuffer(9)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    exit()
