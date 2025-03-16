
# Axes = [4]
# IOOutputs = [5.0, 5.1, 5.2]

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Set the comparison axis 4 command position output to 5.0.
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 5
PsoOut.bitAddress = 0
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 4

# Create a command value of axis 4 moves to position 60 at a speed of 1000, with an acceleration and deceleration of 10000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 60

# Set parameters for a position synchronous output channel 0. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)

# Output to 5.1
PsoOut.byteAddress = 5
PsoOut.bitAddress = 1
# Set parameters for a position synchronous output channel 1. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)

# Output to 5.2
PsoOut.byteAddress = 5
PsoOut.bitAddress = 2
# Set parameters for a position synchronous output channel 2. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

# Set interval position synchronization output parameters: rangeStart = 0, rangeEnd = 30, and interval = 5.
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(0, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData0 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(1, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData1 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(2, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData2 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

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
Wmx3Lib_cm.motion.Wait(4)

# StopPSO
Wmx3Lib_EventCtl.StopPSO(0)
Wmx3Lib_EventCtl.StopPSO(1)
Wmx3Lib_EventCtl.StopPSO(2)
