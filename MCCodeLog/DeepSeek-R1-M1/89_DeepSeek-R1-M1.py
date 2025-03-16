
# Axes = [9]
# IOInputs = []
# IOOutputs = [2.1]

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Set the comparison axis 9 command position output to 2.1.
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 2
PsoOut.bitAddress = 1
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 9
# The comparison position values are: 11, 22, 33.
point = [11, 22, 33]

# Create a command value of axis 9 moves to position 44 at a speed of 1500, with an acceleration and deceleration of 15000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.profile.velocity = 1500
posCommand.profile.acc = 15000
posCommand.profile.dec = 15000
posCommand.target = 44

# Set parameters for a position synchronous output channel.
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.LessThan, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Set multiple data points for a position synchronous output channel.
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, 3, point)
if ret != 0:
    print('SetPSOMultipleData error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Get the channel status
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
# If the channel is already open, execute StopPSO.
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(0)
    sleep(0.01)

# StartPSO
ret = Wmx3Lib_EventCtl.StartPSO(0)
if ret != 0:
    print('StartPSO error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Execute command to move to a specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(9)

# StopPSO
Wmx3Lib_EventCtl.StopPSO(0)
