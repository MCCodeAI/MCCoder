
# Axes = [2]
# IOOutputs = [3.0, 3.1, 3.2]

# Initialize the event control and PSO components
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Set the comparison axis 2 command position output to 3.0, 3.1, 3.2
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 3
PsoOut.bitAddress = 0
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 2

# The comparison position values are: 12, 24, 36
points = [12, 24, 36]

# Create a command value for axis 2 to move to a target position of 48
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 48

# Set parameters for a position synchronous output channel 0
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)

# Output to 3.1
PsoOut.bitAddress = 1
# Set parameters for a position synchronous output channel 1
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)

# Output to 3.2
PsoOut.bitAddress = 2
# Set parameters for a position synchronous output channel 2
Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

# Set multiple data points for each position synchronous output channel
for channel in range(3):
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(channel, len(points), points)
    if ret != 0:
        print(f'SetPSOMultipleData{channel} error code is {ret}: {Wmx3Lib_EventCtl.ErrorToString(ret)}')

# Check and stop PSO if already enabled
for channel in range(3):
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(channel)
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(channel)
        sleep(0.01)

# Start PSO for each channel
for channel in range(3):
    ret = Wmx3Lib_EventCtl.StartPSO(channel)
    if ret != 0:
        print(f'StartPSO{channel} error code is {ret}: {Wmx3Lib_EventCtl.ErrorToString(ret)}')

# Execute command to move to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error code is {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')

# Wait for the axis to stop moving
Wmx3Lib_cm.motion.Wait(2)

# Stop PSO for each channel
for channel in range(3):
    Wmx3Lib_EventCtl.StopPSO(channel)
