
# Axes = [4]
# IOOutputs = [5.0, 5.1, 5.2]

# Initialize the event control and PSO components
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Configure the PSO output for Axis 4
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 4

# Set up the motion command for Axis 4
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 60

# Configure PSO channels with different comparison types
# Channel 0: Equal
PsoOut.byteAddress = 5
PsoOut.bitAddress = 0
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)

# Channel 1: PositiveDirection
PsoOut.byteAddress = 5
PsoOut.bitAddress = 1
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)

# Channel 2: NegativeDirection
PsoOut.byteAddress = 5
PsoOut.bitAddress = 2
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
        print(f'StartPSO{channel} error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Execute the motion command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 4 to complete the motion
Wmx3Lib_cm.motion.Wait(4)

# Stop PSO for each channel
for channel in range(3):
    Wmx3Lib_EventCtl.StopPSO(channel)
