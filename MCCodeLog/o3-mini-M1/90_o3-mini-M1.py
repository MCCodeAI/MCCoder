
# Axes = [2]
# IOInputs = []
# IOOutputs = [3.0, 3.1, 3.2]

# Instantiate the necessary control objects.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Configure the PSO output for Axis 2.
# For channel 0: use Equal comparison type and output point 3.0.
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 3      # Corresponds to output byte 3
PsoOut.bitAddress = 0         # Output bit 0 (i.e. 3.0)
PsoOut.invert = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 2           # Using Axis 2

# Define the position synchronization points.
dataPoints = [12, 24, 36]

# Create a motion command for Axis 2 to move to position 48.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 48

# Set PSO configuration for Channel 0 with Equal comparison type.
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
if ret != 0:
    print("SetPSOConfig channel 0 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))

# Set PSO configuration for Channel 1 with PositiveDirection comparison type.
# Update output point to 3.1.
PsoOut.byteAddress = 3
PsoOut.bitAddress = 1         # Output point 3.1
ret = Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print("SetPSOConfig channel 1 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))

# Set PSO configuration for Channel 2 with NegativeDirection comparison type.
# Update output point to 3.2.
PsoOut.byteAddress = 3
PsoOut.bitAddress = 2         # Output point 3.2
ret = Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)
if ret != 0:
    print("SetPSOConfig channel 2 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))

# Load the multiple data points for each PSO channel.
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, len(dataPoints), dataPoints)
if ret != 0:
    print("SetPSOMultipleData channel 0 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(1, len(dataPoints), dataPoints)
if ret != 0:
    print("SetPSOMultipleData channel 1 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(2, len(dataPoints), dataPoints)
if ret != 0:
    print("SetPSOMultipleData channel 2 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))

# Check and stop any active PSO on all channels before starting new configuration.
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(0)
    sleep(0.01)
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(1)
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(1)
    sleep(0.01)
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(2)
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(2)
    sleep(0.01)

# Start PSO on all channels.
ret = Wmx3Lib_EventCtl.StartPSO(0)
if ret != 0:
    print("StartPSO channel 0 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.StartPSO(1)
if ret != 0:
    print("StartPSO channel 1 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))
ret = Wmx3Lib_EventCtl.StartPSO(2)
if ret != 0:
    print("StartPSO channel 2 error:", str(ret), Wmx3Lib_EventCtl.ErrorToString(ret))

# Execute the motion command: move Axis 2 to position 48.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error:", str(ret), Wmx3Lib_cm.ErrorToString(ret))
# Wait until Axis 2 stops moving.
Wmx3Lib_cm.motion.Wait(2)

# Stop the PSO channels after motion is complete.
Wmx3Lib_EventCtl.StopPSO(0)
Wmx3Lib_EventCtl.StopPSO(1)
Wmx3Lib_EventCtl.StopPSO(2)
