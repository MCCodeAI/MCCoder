
import time

# Assume that the following classes, methods, and constants are provided
# by the motion control system API:
#   EventControl, EventControl_PSOStatus, EventControl_PSOOutput, EventControl_ComparatorSource,
#   EventControl_ComparisonType, EventControl_PSOOutputType, EventControl_ComparatorSourceType,
#   Motion_PosCommand, ProfileType, and the motion control module Wmx3Lib_cm.
#
# Do not import any motion libraries in this demo.

# Create objects for PSO configuration
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
PsoStu      = EventControl_PSOStatus()
PsoOut      = EventControl_PSOOutput()
PsoCompSor  = EventControl_ComparatorSource()

# Configure the PSO output for Axis 2.
# All three channels will use the same position synchronization data points.
points = [12, 24, 36]

# --- Configure Channel 0 (Equal) ---
PsoOut.outputType   = EventControl_PSOOutputType.IOOutput
PsoOut.byteAddress  = 3
PsoOut.bitAddress   = 0
PsoOut.invert       = 0
PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
PsoCompSor.axis     = 2
Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)

# --- Configure Channel 1 (PositiveDirection) ---
PsoOut.byteAddress  = 3
PsoOut.bitAddress   = 1
Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)

# --- Configure Channel 2 (NegativeDirection) ---
PsoOut.byteAddress  = 3
PsoOut.bitAddress   = 2
Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

# ----------------------------------------------------------------------
# Correction: Ensure PSO channels are disabled BEFORE calling
# SetPSOMultipleData since it returns error 90131 if the channel is enabled.
for ch in [0, 1, 2]:
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(ch)
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(ch)
        time.sleep(0.01)

# Set the PSO data points for each channel.
for ch in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(ch, 3, points)
    if ret != 0:
        print(f"SetPSOMultipleData{ch} error code is", ret, ":", Wmx3Lib_EventCtl.ErrorToString(ret))
# ----------------------------------------------------------------------

# Start the PSO channels.
for ch in [0, 1, 2]:
    ret = Wmx3Lib_EventCtl.StartPSO(ch)
    if ret != 0:
        print(f"StartPSO channel {ch} error code is", ret, ":", Wmx3Lib_EventCtl.ErrorToString(ret))

# ----------------------------------------------------------------------
# Correction: Ensure Axis 2 servo is turned on before starting motion.
# Wait for Axis 2 servo on state with a timeout.
counter = 1000
while counter > 0:
    # Assume GetStatus returns a tuple: (ret, status) where status has an attribute 'servoOn'
    ret, status = Wmx3Lib_cm.GetStatus(2)
    if ret == 0 and getattr(status, 'servoOn', False):
        break
    time.sleep(0.01)
    counter -= 1
if counter == 0:
    print("Axis 2 failed to turn servo on. Exiting motion command.")
else:
    # Create and configure the motion command for Axis 2.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis         = 2
    posCommand.profile.velocity = 1000
    posCommand.profile.acc      = 10000
    posCommand.profile.dec      = 10000
    posCommand.target           = 48

    # Execute the commanded motion for Axis 2.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))

    # Wait until Axis 2 has stopped moving.
    Wmx3Lib_cm.motion.Wait(2)

# After motion is complete, stop all PSO channels.
for ch in [0, 1, 2]:
    Wmx3Lib_EventCtl.StopPSO(ch)
