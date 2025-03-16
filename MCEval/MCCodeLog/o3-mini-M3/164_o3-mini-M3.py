
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

#-------------------------------------------------------------------
# Step 1:
# Start an absolute position command for Axis 10 to move to position 800
# with a velocity of 600.
#-------------------------------------------------------------------

posCmd = Motion_PosCommand()
posCmd.axis = 10
posCmd.target = 800
posCmd.profile.type = ProfileType.Trapezoidal
posCmd.profile.velocity = 600
posCmd.profile.acc = 10000
posCmd.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCmd)
if ret != 0:
    print("Error in StartPos for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 10 stops moving.
axisSel = AxisSelection()
axisSel.axisCount = 1
axisSel.SetAxis(0, 10)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error in Wait_AxisSel for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
    exit()

#-------------------------------------------------------------------
# Step 2:
# Execute an absolute triggered position command for Axis 10.
# When the remaining distance (to the current target) becomes 200,
# trigger Axis 10 to move to position 300 with a velocity of 1000.
# Do not use an axis wait in the middle of this continuous motion.
#-------------------------------------------------------------------

trigCmd = Motion_TriggerPosCommand()
trigCmd.axis = 10
trigCmd.target = 300
trigCmd.profile.type = ProfileType.Trapezoidal
trigCmd.profile.velocity = 1000
trigCmd.profile.acc = 10000
trigCmd.profile.dec = 10000

trigger = Trigger()
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 200
trigCmd.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCmd)
if ret != 0:
    print("Error in StartPos_Trigger for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
    exit()

# (No axis wait here since the triggered command is part of a continuous motion.)

#-------------------------------------------------------------------
# Step 3:
# Set an event so that when Axis 10 reaches the position of 400,
# it triggers the movement of Axis 12 to position 80.
# Use wait(axis) for this event-driven motion.
#-------------------------------------------------------------------

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Configure the event input: trigger when Axis 10 equals position 400.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Configure the event output: start an absolute position command for Axis 12.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 80
eventOut_Motion.startSinglePos.velocity = 600
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Use event ID 0.
posEventID = 0
ret, eventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print("Error in SetEvent_ID:", ret)
    exit()

Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)
sleep(0.01)  # brief delay to ensure event is enabled

# At this point, when Axis 10 reaches position 400 the event will fire,
# and the motion command for Axis 12 will be executed.

# Wait for Axis 12 to complete its motion.
axisSel2 = AxisSelection()
axisSel2.axisCount = 1
axisSel2.SetAxis(0, 12)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel2)
if ret != 0:
    print("Error in Wait_AxisSel for Axis 12:", Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Optionally remove the event after the motion has completed.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print("Error in RemoveEvent:", ret)
    exit()
