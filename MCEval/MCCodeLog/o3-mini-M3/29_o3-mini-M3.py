
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Create and execute a cyclic buffer memory space for Axis 9.
# This code does the following:
# 1. Opens a cyclic buffer for Axis 9.
# 2. Executes the cyclic buffer.
# 3. Adds three motion commands:
#    - Move to absolute position 60 within 100 cycles.
#    - Move a relative distance of 140 within 100 cycles.
#    - Move to absolute position -100 within 200 cycles.
# 4. After each motion command is added, waits until the axis stops moving.
#    (Note: when commands are added consecutively for continuous motion,
#     waiting is done only after the complete motion.)
# 5. Closes the cyclic buffer.

import time

def wait_for_motion_completion(Wmx3Lib_cyc, axis):
    # Wait until the cyclic buffer execution for the specified axis has no remaining commands.
    while True:
        ret, cyc_Status = Wmx3Lib_cyc.GetStatus(axis)
        if ret != 0:
            print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
            return ret
        # When remainCount is 0 or less, the last command has finished.
        if cyc_Status.remainCount <= 0:
            break
        time.sleep(0.1)
    return 0

def main():
    # Assume Wmx3Lib is available in the runtime environment.
    Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)
    
    # Open a cyclic buffer memory space for Axis 9 with a buffer size of 1024 cycles.
    ret = Wmx3Lib_cyc.OpenCyclicBuffer(9, 1024)
    if ret != 0:
        print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Start the execution of the cyclic buffer for Axis 9.
    ret = Wmx3Lib_cyc.Execute(9)
    if ret != 0:
        print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # First command: Move Axis 9 to the absolute position 60 within 100 cycles.
    cyclicCommand = CyclicBufferSingleAxisCommand()
    cyclicCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicCommand.intervalCycles = 100
    cyclicCommand.command = 60
    ret = Wmx3Lib_cyc.AddCommand(9, cyclicCommand)
    if ret != 0:
        print('AddCommand (Absolute to 60) error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Wait for the axis to stop moving after the first motion.
    if wait_for_motion_completion(Wmx3Lib_cyc, 9) != 0:
        return

    # Second command: Move Axis 9 a relative distance of 140 within 100 cycles.
    cyclicCommand.type = CyclicBufferCommandType.RelativePos
    cyclicCommand.intervalCycles = 100
    cyclicCommand.command = 140
    ret = Wmx3Lib_cyc.AddCommand(9, cyclicCommand)
    if ret != 0:
        print('AddCommand (Relative +140) error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Wait for the axis to stop moving after the second motion.
    if wait_for_motion_completion(Wmx3Lib_cyc, 9) != 0:
        return

    # Third command: Move Axis 9 to the absolute position -100 within 200 cycles.
    cyclicCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicCommand.intervalCycles = 200
    cyclicCommand.command = -100
    ret = Wmx3Lib_cyc.AddCommand(9, cyclicCommand)
    if ret != 0:
        print('AddCommand (Absolute to -100) error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Wait for the axis to stop moving after the third motion.
    if wait_for_motion_completion(Wmx3Lib_cyc, 9) != 0:
        return

    # Close the cyclic buffer memory space.
    ret = Wmx3Lib_cyc.CloseCyclicBuffer(9)
    if ret != 0:
        print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
