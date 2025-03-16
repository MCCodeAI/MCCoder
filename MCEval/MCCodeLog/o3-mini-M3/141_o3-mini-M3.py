
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

import time

# Set up event control for triggering motion
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use Event ID 0 for this event
eventID = 0

# Configure the event input:
# When Axis 10 reaches the absolute position of 100, the event will be triggered.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Configure the event output:
# When the event is triggered, start an absolute position command for Axis 2 
# to move to -200 with specified profile parameters.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 2
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -200
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set event with the event control interface
ret, evtID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print("SetEvent_ID error code is", ret)
    exit()

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Sleep briefly to ensure event configuration is active
time.sleep(0.01)

# Start a base absolute position motion command for Axis 10.
# This motion, when passing through position 100, will trigger the event.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = 500    # This target is chosen to ensure Axis 10 passes through 100.
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 10 stops moving before proceeding.
Wmx3Lib_cm.motion.Wait(10)

# After the base motion is complete, remove the event.
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print("RemoveEvent error code is", ret, Wmx3Lib.ErrorToString(ret))
    exit()
