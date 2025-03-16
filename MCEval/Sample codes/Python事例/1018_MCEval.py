# Write Python code to demonstrate a position synchronous output function using the Equal, PositiveDirection, and NegativeDirection comparison type. Channel 0, 1, 2 are used, each with identical parameter settings except for the comparison type. The position synchronization comparison values are: 150, 300, 450, with the position synchronization output point at 0.0, 0.1, 0.2. Axis 7 is to move to the target position of 500, with a speed of 1000, and acceleration and deceleration are set to 10000.
# Axes = [7]

    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    PsoStu = EventControl_PSOStatus()
    PsoOut = EventControl_PSOOutput()
    PsoCompSor = EventControl_ComparatorSource()

    # Set the comparison axis 7 command position output to 0.0.
    PsoOut.outputType = EventControl_PSOOutputType.IOOutput
    PsoOut.byteAddress = 0
    PsoOut.bitAddress = 0
    PsoOut.invert = 0
    PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
    PsoCompSor.axis = 7
    # The comparison position values are: 150, 300, 450.
    point = [150, 300, 450]
    # Create a command value of axis 7 moves a distance of 500 from the current position at a speed of 1000, with an acceleration and deceleration of 10000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 7
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.target = 500
    # Set parameters for a position synchronous output channel 0. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
    # Output to 0.1
    PsoOut.bitAddress = 1
    # Set parameters for a position synchronous output channel 1. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
    # Output to 0.2
    PsoOut.bitAddress = 2
    # Set parameters for a position synchronous output channel 2. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)
    # Set multiple data points for a position synchronous output channel.
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, 3, point)
    if ret != 0:
        print('SetPSOMultipleData0 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(1, 3, point)
    if ret != 0:
        print('SetPSOMultipleData1 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(2, 3, point)
    if ret != 0:
        print('SetPSOMultipleData2 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(0)
        sleep(0.01)
    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(1)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(1)
        sleep(0.01)
    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(2)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(2)
        sleep(0.01)

    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(0)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(1)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(2)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

    # Execute command to move to a specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(7)
    # StopPSO
    Wmx3Lib_EventCtl.StopPSO(0)
    Wmx3Lib_EventCtl.StopPSO(1)
    Wmx3Lib_EventCtl.StopPSO(2)
