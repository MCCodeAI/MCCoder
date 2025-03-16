
# Axes = [4]
# IOInputs = []
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

# Create a command value of axis 4 moves to 60 at a speed of 1000, with acceleration and deceleration of 10000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 60

# Set parameters for position synchronous output channels
# Channel 0 - Equal comparison type
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
# Output to 5.1
PsoOut.byteAddress = 5
PsoOut.bitAddress = 1
# Channel 1 - PositiveDirection comparison type
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
# Output to 5.2
PsoOut.byteAddress = 5
PsoOut.bitAddress = 2
# Channel 2 - NegativeDirection comparison type
Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

# Set interval data for all channels
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.SetPSOIntervalData(channel, 0, 30, 5)
    if ret != 0:
        print(f'SetPSOIntervalData{channel} error code is {ret}: {Wmx3Lib_EventCtl.ErrorToString(ret)}')

# Check and stop running PSO channels
for channel in [0, 1, 2]:
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(channel)
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(channel)
        sleep(0.01)

# Start PSO for all channels
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.StartPSO(channel)
    if ret != 0:
        print(f'StartPSO{channel} error code is {ret}: {Wmx3Lib_EventCtl.ErrorToString(ret)}')

# Execute motion command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print(f'StartPos error code is {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
Wmx3Lib_cm.motion.Wait(4)

# Stop PSO after motion completes
for channel in [0, 1, 2]:
    Wmx3Lib_EventCtl.StopPSO(channel)
