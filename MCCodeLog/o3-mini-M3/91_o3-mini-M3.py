
# Initialize PSO control objects for Axis 4 BEFORE using them
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu     = EventControl_PSOStatus()
PsoOut     = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Ensure PSO channels are stopped before configuration to avoid "Channel is enabled" errors
for channel in [0, 1, 2]:
    ret, psoStatus = Wmx3Lib_EventCtl.GetPSOStatus(channel)
    if psoStatus.enabled == 1:
        ret_stop = Wmx3Lib_EventCtl.StopPSO(channel)
        if ret_stop != 0:
            print(f'StopPSO channel {channel} error code is {ret_stop}: ' + Wmx3Lib_EventCtl.ErrorToString(ret_stop))
        sleep(0.01)

# Axes = [4]
# IOInputs = []
# IOOutputs = [5.0, 5.1, 5.2]

# Configure common PSO output attributes
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.invert     = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis       = 4

# ---------------------------
# Configure PSO Channel 0 with Equal comparison and IO output point 5.0
PsoOut.byteAddress = 5
PsoOut.bitAddress  = 0
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
if ret != 0:
    print(f'SetPSOConfig channel 0 error code is {ret}: ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# ---------------------------
# Configure PSO Channel 1 with PositiveDirection comparison and IO output point 5.1
PsoOut.byteAddress = 5
PsoOut.bitAddress  = 1
ret = Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print(f'SetPSOConfig channel 1 error code is {ret}: ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# ---------------------------
# Configure PSO Channel 2 with NegativeDirection comparison and IO output point 5.2
PsoOut.byteAddress = 5
PsoOut.bitAddress  = 2
ret = Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print(f'SetPSOConfig channel 2 error code is {ret}: ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# ---------------------------
# Set Interval position synchronization output parameters for all channels:
# rangeStart = 0, rangeEnd = 30, interval = 5
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.SetPSOIntervalData(channel, 0, 30, 5)
    if ret != 0:
        print(f'SetPSOIntervalData channel {channel} error code is {ret}: ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Start PSO on all three channels
for channel in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.StartPSO(channel)
    if ret != 0:
        print(f'StartPSO channel {channel} error code is {ret}: ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# ---------------------------
# Create a motion command to move Axis 4 to position 60
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis           = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc      = 10000
posCommand.profile.dec      = 10000
posCommand.target         = 60

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
# Wait until Axis 4 stops moving (wait after the complete motion)
Wmx3Lib_cm.motion.Wait(4)

# ---------------------------
# Stop PSO on all channels after motion is complete
for channel in [0, 1, 2]:
    Wmx3Lib_EventCtl.StopPSO(channel)
