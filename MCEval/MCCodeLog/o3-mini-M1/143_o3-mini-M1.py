
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

#----------------------------------------------------------------------
# This script executes an absolute triggered position command:
# 1. Axis 10 is commanded to move to -1000 with a velocity of 600.
# 2. When the remaining distance for Axis 10 reaches 500, a triggered command
#    starts to move Axis 10 to -300 with a velocity of 1000.
# 3. An event is set so that when Axis 10 reaches the absolute position 100,
#    a motion command is triggered to move Axis 2 to -200 with a velocity of 1000.
#
# The script waits for the axis motion to complete after each separate motion.
#----------------------------------------------------------------------

# ----- Absolute motion command for Axis 10 -----
posCmd = Motion_PosCommand()
posCmd.axis = 10
posCmd.profile.type = ProfileType.Trapezoidal
posCmd.profile.velocity = 600
posCmd.profile.acc = 10000
posCmd.profile.dec = 10000
posCmd.profile.endVelocity = 600
posCmd.target = -1000

ret = Wmx3Lib_cm.motion.StartPos(posCmd)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Early exit if error encountered.
else:
    # Wait until Axis 10 stops before starting the trigger command.
    Wmx3Lib_cm.motion.Wait(10)


# ----- Triggered motion command for Axis 10 -----
trigCmd = Motion_TriggerPosCommand()
trigCmd.axis = 10
trigCmd.profile.type = ProfileType.Trapezoidal
trigCmd.profile.velocity = 1000
trigCmd.profile.acc = 10000
trigCmd.profile.dec = 10000
trigCmd.target = -300
# Set the trigger to start when the remaining distance on Axis 10 reaches 500
trigCmd.trigger.triggerType = TriggerType.RemainingDistance
trigCmd.trigger.triggerAxis = 10
trigCmd.trigger.triggerValue = 500

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCmd)
if ret != 0:
    print("StartPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Early exit if error encountered.
else:
    # Wait until Axis 10 completes its triggered motion.
    Wmx3Lib_cm.motion.Wait(10)


# ----- Set an event to trigger a motion command for Axis 2 -----
# The event will trigger when Axis 10 reaches the absolute position of 100.

# Configure the event input to monitor Axis 10 position equals 100.
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Configure the event output to start an absolute position command on Axis 2.
eventOut_Motion = CoreMotionEventOutput()
eventOut_Motion.type = CoreMotionEventOutputType.StartPos
# Assuming that the StartPos command parameters are provided within the event output structure.
eventOut_Motion.startPos.axis = 2
eventOut_Motion.startPos.profile.type = ProfileType.Trapezoidal
eventOut_Motion.startPos.profile.velocity = 1000
eventOut_Motion.startPos.profile.acc = 10000
eventOut_Motion.startPos.profile.dec = 10000
eventOut_Motion.startPos.profile.endVelocity = 1000
eventOut_Motion.startPos.target = -200

# Define an event ID for registration.
eventID = 0

ret, regEventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print("SetEvent_ID error code is " + str(ret))
else:
    # Enable the event so that it becomes active.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Wait until both Axis 10 and Axis 2 finish their motions.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 10)
axisSel.SetAxis(1, 2)

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# Optionally, remove the event after it has been triggered.
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print("RemoveEvent error code is " + str(ret) + ": " + Wmx3Lib.ErrorToString(ret))
