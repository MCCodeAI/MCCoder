
# -*- coding: utf-8 -*-
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = []

import time

# ------------------------------
# Configure the Event for Triggering Axis 1 Motion
# ------------------------------
# Create event control, event input, and event output instances
# (Assume these classes and objects are defined in the motion API's environment)
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Set the event input: Monitor CompletedTime for Axis 3 equals 300ms.
eventIN_Motion.inputFunction = CoreMotionEventInputType.CompletedTime
eventIN_Motion.completedTime.axis = 3
eventIN_Motion.completedTime.timeMilliseconds = 300
eventIN_Motion.completedTime.disableIdleAxisTrigger = 1

# Set the event output: When the condition is met, trigger a linear interpolation command for Axis 1.
eventOut_Motion.type = CoreMotionEventOutputType.LinearIntplPos
eventOut_Motion.linearIntplPos.axisCount = 1
eventOut_Motion.linearIntplPos.SetAxis(0, 1)  # Map command slot index 0 to Axis 1.
eventOut_Motion.linearIntplPos.type = ProfileType.Trapezoidal
eventOut_Motion.linearIntplPos.velocity = 1000
eventOut_Motion.linearIntplPos.acc = 10000
eventOut_Motion.linearIntplPos.dec = 10000
eventOut_Motion.linearIntplPos.SetTarget(0, 300)

# Use an event ID (here we choose 1)
eventID = 1
ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print("SetEvent_ID error code:", ret)
    exit(1)

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)
# A short delay to ensure the event is registered.
time.sleep(0.01)

# ------------------------------
# Start the Continuous Motion for Axis 2 and Axis 3
# ------------------------------
# Prepare a multi-axis linear interpolation command to move Axis 2 and Axis 3 concurrently.
multiPosCommand = Motion_LinearIntplPosCommand()
multiPosCommand.axisCount = 2
multiPosCommand.linearIntplPos.type = ProfileType.Trapezoidal
multiPosCommand.linearIntplPos.velocity = 1000
multiPosCommand.linearIntplPos.acc = 10000
multiPosCommand.linearIntplPos.dec = 10000

# Map the two command slots to the corresponding axes: first to Axis 2, second to Axis 3.
multiPosCommand.linearIntplPos.SetAxis(0, 2)
multiPosCommand.linearIntplPos.SetAxis(1, 3)

# Set both target positions to 2000.
multiPosCommand.linearIntplPos.SetTarget(0, 2000)
multiPosCommand.linearIntplPos.SetTarget(1, 2000)

# Start the continuous motion for Axis 2 and Axis 3.
ret = Wmx3Lib_cm.motion.StartMov_LinearIntpl(multiPosCommand)
if ret != 0:
    print("StartMov_LinearIntpl error code:", ret)
    exit(1)

# Since this is a continuous motion command for Axis 2 and Axis 3,
# we do not wait in the middle of the command, but we wait after issuing it.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code for Axis 2 and 3:", ret)
    exit(1)

# ------------------------------
# Wait for the Triggered Motion (Axis 1) to Complete
# ------------------------------
# The event set above triggers a motion command for Axis 1. After the command starts,
# wait until Axis 1 stops moving.
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print("Wait error code for Axis 1:", ret)
    exit(1)

# ------------------------------
# Remove the Event (cleanup)
# ------------------------------
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print("RemoveEvent error code:", ret)
    exit(1)
