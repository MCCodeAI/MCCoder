
# Axes = [4]
# IOInputs = []
# IOOutputs = [5.0, 5.1, 5.2]

# Initialize the event control and PSO components
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Set the comparison axis 4 command position output to 5.0, 5.1, 5.2
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 5
PsoOut.bitAddress = 0
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 4

# Create a command value of axis 4 moves a distance of 60 from the current position at a speed of 1000, with an acceleration and deceleration of 10000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 60

# Set parameters for a position synchronous output channel 0
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)

# Output to 5.1
PsoOut.bitAddress = 1
# Set parameters for a position synchronous output channel 1
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)

# Output to 5.2
PsoOut.bitAddress = 2
# Set parameters for a position synchronous output channel 2
Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

# Set interval data for each channel
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(0, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData0 error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(1, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData1 error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOIntervalData(2, 0, 30, 5)
if ret != 0:
    print('SetPSOIntervalData2 error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Get the channel status and stop if already enabled
for channel in range(3):
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(channel)
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(channel)
        sleep(0.01)

# Start PSO for each channel
for channel in range(3):
    ret = Wmx3Lib_EventCtl.StartPSO(channel)
    if ret != 0:
        print(f'StartPSO channel {channel} error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Execute command to move to a specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(4)

# Stop PSO for each channel
for channel in range(3):
    Wmx3Lib_EventCtl.StopPSO(channel)
