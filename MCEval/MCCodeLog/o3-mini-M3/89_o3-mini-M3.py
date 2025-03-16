
import time

# Configure position synchronous output for Axis 9 using the LessThan comparison

# Create instances of the event control objects
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu = EventControl_PSOStatus()
PsoOut = EventControl_PSOOutput()
PsoCompSor = EventControl_ComparatorSource()

# Configure the IO output point for Axis 9 at 2.1 (byteAddress = 2, bitAddress = 1)
PsoOut.outputType = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress = 2
PsoOut.bitAddress = 1
PsoOut.invert = 0

# Set the comparator source to the position command of Axis 9
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis = 9

# Define the position comparison values for PSO: [11, 22, 33]
points = [11, 22, 33]

# Set up the PSO configuration on channel 0 with LessThan comparison type
ret = Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.LessThan, PsoCompSor, PsoOut, 0)
if ret != 0:
    print('SetPSOConfig error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Set the multiple data points for the PSO channel
ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, len(points), points)
if ret != 0:
    print('SetPSOMultipleData error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Check the PSO status and stop it if it is already running
ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
if PsoStu.enabled == 1:
    Wmx3Lib_EventCtl.StopPSO(0)
    time.sleep(0.01)

# Start the PSO channel
ret = Wmx3Lib_EventCtl.StartPSO(0)
if ret != 0:
    print('StartPSO error code: ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

# Create the motion command for Axis 9: move to position 44 with speed 1500 and acceleration/deceleration 15000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.profile.velocity = 1500
posCommand.profile.acc = 15000
posCommand.profile.dec = 15000
posCommand.target = 44

# <-- Correction: Ensure Axis 9 is servo on before starting the motion command.
ret, status = Wmx3Lib_cm.motion.GetStatus(9)
if not status.servoOn:
    ret = Wmx3Lib_cm.motion.ServoOn(9)
    if ret != 0:
        print('ServoOn error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Wait until the servo is fully engaged
    while True:
        ret, status = Wmx3Lib_cm.motion.GetStatus(9)
        if status.servoOn:
            break
        time.sleep(0.01)
        
# Execute the motion command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until Axis 9 stops moving (after the complete move)
Wmx3Lib_cm.motion.Wait(9)

# Stop the PSO after the axis has come to a complete stop
Wmx3Lib_EventCtl.StopPSO(0)
