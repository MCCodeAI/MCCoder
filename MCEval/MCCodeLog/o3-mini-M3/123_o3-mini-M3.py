
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

import time  # Use time.sleep, not a wildcard import, so as not to shadow sleep.

# -----------------------------------------------------------------------------
# Configure event to monitor Axis 0's remaining distance equals 1000,
# and when triggered, move Axis 1 to position 800 with a velocity of 1000.
# -----------------------------------------------------------------------------

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for this configuration
posEventID = 0

# Set the event input: monitor if Axis 0's remaining distance equals 1000.
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
eventIN_Motion.remainingDistance.axis = 0
eventIN_Motion.remainingDistance.distance = 1000
eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

# Set the event output: when triggered, execute a single position command on Axis 1.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 1
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 800
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print("SetEvent_ID error code is " + str(ret))
    # Depending on application, handle error appropriately.

# Enable the event trigger.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)
time.sleep(0.01)  # Wait a short time so the event is fully enabled.

# -----------------------------------------------------------------------------
# Command the motion for Axis 0.
# -----------------------------------------------------------------------------
# Create a position command to move Axis 0 to target position 2000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Depending on application, handle error appropriately.

# -----------------------------------------------------------------------------
# Wait for each motion to complete.
# -----------------------------------------------------------------------------
# Wait until Axis 0, which we explicitly commanded, finishes its movement.
Wmx3Lib_cm.motion.Wait(0)

# In parallel, the event may trigger a motion on Axis 1.
# After Axis 0 completes, ensure that Axis 1 finishes its triggered motion.
Wmx3Lib_cm.motion.Wait(1)

# -----------------------------------------------------------------------------
# Once all motions are done, remove the event trigger.
# -----------------------------------------------------------------------------
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print("RemoveEvent error code is " + str(ret))
    # Depending on application, handle error appropriately.
