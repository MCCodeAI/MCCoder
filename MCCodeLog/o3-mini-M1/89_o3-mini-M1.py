
# Axes = [9]
# IOInputs = []
# IOOutputs = [2.1]

# Create and configure a PSO function on Axis 9 using the LessThan comparator.
# The PSO will output at IO point 2.1 when the command position of Axis 9 is less than one
# of the specified comparison values (11, 22, 33). Then, Axis 9 will move to position 44
# with a speed of 1500, and acceleration and deceleration of 15000.

import time

# Initialize the event control and related objects.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu       = EventControl_PSOStatus()
PsoOut       = EventControl_PSOOutput()
PsoCompSor   = EventControl_ComparatorSource()

# Configure PSO output: set the IO output point at 2.1 for Axis 9.
PsoOut.outputType   = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress  = 2
PsoOut.bitAddress   = 1
PsoOut.invert       = 0

PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis       = 9

# Define the position comparison values.
points = [11, 22, 33]

# Create the motion command for Axis 9.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis         = 9
posCommand.profile.velocity = 1500
posCommand.profile.acc      = 15000
posCommand.profile.dec      = 15000
posCommand.target           = 44

# Configure the PSO channel using the LessThan comparison.
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.LessThan, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig error code:', ret, Wmx3Lib_EventCtl.ErrorToString(ret))

# Set the multiple data points for the PSO channel.
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, len(points), points)
if ret != 0:
    print('SetPSOMultipleData error code:', ret, Wmx3Lib_EventCtl.ErrorToString(ret))

# Check the PSO status and stop the channel if it's already active.
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(0)
    time.sleep(0.01)

# Start the PSO channel.
ret = Wmx3Lib_EventCtl.StartPSO(0)
if ret != 0:
    print('StartPSO error code:', ret, Wmx3Lib_EventCtl.ErrorToString(ret))

# Issue the motion command to move Axis 9.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code:', ret, Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 9 to complete its motion.
Wmx3Lib_cm.motion.Wait(9)

# Stop the PSO channel after the motion is complete.
Wmx3Lib_EventCtl.StopPSO(0)
