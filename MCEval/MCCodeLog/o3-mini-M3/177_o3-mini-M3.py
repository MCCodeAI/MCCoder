
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Assume that Wmx3Lib, Wmx3Lib_EventCtl, Wmx3Lib_cm, WMX3Log and related classes
# (such as CoreMotionEventInput, CoreMotionEventOutput, Motion_PosCommand, ProfileType, etc.)
# are already defined and available in the runtime environment.
# Also assume that the sleep function is available (e.g., from time.sleep).

sleep(0.01)

# Create and configure the event that will trigger the motion of Axis 12
# when Axis 10 reaches the position of 100.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID is set to 0.
eventID = 0

# ----- Set the event input: when Axis 10 equals 100 -----
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# ----- Set the event output:
# Configure a single absolute motion command for Axis 12 to move to -50.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -50
eventOut_Motion.startSinglePos.velocity = 500
eventOut_Motion.startSinglePos.acc = 5000
eventOut_Motion.startSinglePos.dec = 5000

# Register the event.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    # Handle error if necessary.

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

sleep(0.01)  # Short delay to ensure the event is properly configured.

# ----- Start a motion command on Axis 10 that will trigger the event -----
# Here, Axis 10 is commanded to move far enough (to 200) so that it passes through 100.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 5000
posCommand.profile.dec = 5000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle error.

# Wait for the motion of Axis 10 to complete.
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error for Axis 10, error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle error.

# Wait for the triggered motion on Axis 12 to complete.
ret = Wmx3Lib_cm.motion.Wait(12)
if ret != 0:
    print('Wait error for Axis 12, error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally handle error.

# Remove the event after completion.
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    # Optionally handle error.
