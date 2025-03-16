
# Axes = [4]
# IOInputs = []
# IOOutputs = [5.0, 5.1, 5.2]

# Create instances for event control and motion command
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Configure the output point and comparator source for Axis 4
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
# For Channel 0 (Equal), set IO output point at 5.0 (byteAddress=5, bitAddress=0)
PsoOut.byteAddress = 5
PsoOut.bitAddress = 0
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 4

# Create the position command for Axis 4
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 60

# Set up PSO for Channel 0 using the Equal comparison type
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig Channel 0 error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# For Channel 1 (PositiveDirection), assign the associated IO output point at 5.1
PsoOut.byteAddress = 5
PsoOut.bitAddress = 1
ret = Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig Channel 1 error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# For Channel 2 (NegativeDirection), assign the associated IO output point at 5.2
PsoOut.byteAddress = 5
PsoOut.bitAddress = 2
ret = Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig Channel 2 error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Set interval position synchronization parameters: rangeStart = 0, rangeEnd = 30, interval = 5
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.SetPSOIntervalData(channel, 0, 30, 5)
    if ret != 0:
        print('SetPSOIntervalData Channel ' + str(channel) + ' error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Check and stop PSO if already active for each channel
for channel in [0, 1, 2]:
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(channel)
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(channel)
        sleep(0.01)

# Start PSO on channels 0, 1, and 2
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.StartPSO(channel)
    if ret != 0:
        print('StartPSO Channel ' + str(channel) + ' error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Execute the position command to move Axis 4 to position 60
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
# Wait for Axis 4 to come to a complete stop
Wmx3Lib_cm.motion.Wait(4)

# Stop the PSO on all channels after the motion is complete
for channel in [0, 1, 2]:
    Wmx3Lib_EventCtl.StopPSO(channel)
