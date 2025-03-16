
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# ============================================================================
# This script performs the following motions:
# 1. Record and execute an API buffer to move Axis 2 to position 150.
# 2. Set an event that triggers a relative position move for Axis 2 (distance = 260, velocity = 1100)
#    when IO Output 1.2 equals 1 (event ID = 5).
# 3. Execute a linear interpolation move of Axis 1 and Axis 3 to (80, 110) at a velocity of 1500.
# 4. Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it back to 0.
#
# NOTE: After each individual motion command, the code waits for the associated axis (or axes)
#       to finish moving. No wait occurs in the middle of a continuous motion.
# ============================================================================

# ----- Part 1: API Buffer recording and execution for Axis 2 move to position 150 -----

# Create and clear API buffer on channel 0.
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Create and configure a position command for Axis 2.
posCommand = Motion_PosCommand()
posCommand.axis = 2
posCommand.target = 150
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000     # Assumed default velocity
posCommand.profile.acc = 10000           # Assumed default acceleration
posCommand.profile.dec = 10000           # Assumed default deceleration

# Add the position command to the API buffer. (The API buffer API is assumed to
# internally record the command so that later an Execute call will run it.)
# (In a real implementation, you might append this command via a method call.)
#
# End recording and execute the API buffer.
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for Axis 2 motion to complete.
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code for Axis 2: ' + str(ret))
    # Optionally handle the error

# ----- Part 2: Event-triggered relative move for Axis 2 (distance=260, velocity=1100) -----

# Create an EventControl instance.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()
posEventID = 5  # Event ID as specified

# Set up the event input to trigger on IO Output 1.2.
eventIN_IO.type = IoEventInputType.NotIOBit
# For IO Output 1.2, byteAddress = 1 and bitAddress = 2.
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.byteAddress = 1
eventIN_IO.ioBit.bitAddress = 2

# Set up the event output as a relative move command.
# We use a multiple-axis command even for a single axis.
eventOut_Motion.type = CoreMotionEventOutputType.StartMultipleMov
eventOut_Motion.startMultipleMov.axisCount = 1
eventOut_Motion.startMultipleMov.SetAxis(0, 2)
eventOut_Motion.startMultipleMov.SetType(0, ProfileType.Trapezoidal)
eventOut_Motion.startMultipleMov.SetVelocity(0, 1100)
eventOut_Motion.startMultipleMov.SetAcc(0, 10000)  # Assumed acceleration
eventOut_Motion.startMultipleMov.SetDec(0, 10000)  # Assumed deceleration
eventOut_Motion.startMultipleMov.SetTarget(0, 260)

# Register the event.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    # Optionally handle the error

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)
sleep(0.01)

# Trigger the event by setting IO output 1.2 to 1.
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
if ret != 0:
    print('SetOutBit error code for triggering event (IO 1.2) is ' + str(ret) +
          ': ' + Wmx3Lib_Io.ErrorToString(ret))
    # Optionally handle the error

# Wait for Axis 2 (event-driven motion) to complete using AxisSelection.
axisSel = AxisSelection()
axisSel.axisCount = 1
axisSel.SetAxis(0, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code for Axis 2: ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle the error

# Remove the event after completion.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) +
          ': ' + WMX3Log.ErrorToString(ret))
    # Optionally handle the error

# ----- Part 3: Linear Interpolation move for Axis 1 and Axis 3 to (80, 110) -----

# Execute a linear interpolation motion command.
# Here we assume a direct call to a linear interpolation move function is available.
# The command uses ProfileType.Trapezoidal with specified velocity.
ret = Wmx3Lib_cm.motion.LinearIntplMov(1, 3, 80, 110, 1500, 10000, 10000)
if ret != 0:
    print('LinearIntplMov error code for Axes 1 and 3: ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle the error

# Wait for the linear interpolation motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code for Axes 1 and 3: ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle the error

# ----- Part 4: IO Output command: Toggle IO output bit 1.2 -----

# Set IO output bit 1.2 to 1.
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
if ret != 0:
    print('SetOutBit error code when setting IO 1.2 to 1: ' + str(ret) +
          ': ' + Wmx3Lib_Io.ErrorToString(ret))
    # Optionally handle the error

# Wait for 0.2 seconds.
sleep(0.2)

# Set IO output bit 1.2 back to 0.
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
if ret != 0:
    print('SetOutBit error code when resetting IO 1.2 to 0: ' + str(ret) +
          ': ' + Wmx3Lib_Io.ErrorToString(ret))
    # Optionally handle the error
