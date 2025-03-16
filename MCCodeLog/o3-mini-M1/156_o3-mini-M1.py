
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Absolute triggered position command example:
#
# 1. Start an absolute position command for Axis 10:
#    • Move Axis 10 to position -800 with a velocity of 600.
# 2. Once moving, use a triggered command so that when the remaining distance (distance to target) of Axis 10 equals 200,
#    it will immediately move to position 300 with a velocity of 1000.
# 3. Additionally, set an event triggered command so that when Axis 10 reaches the position 100,
#    Axis 12 will start moving to -50.
# 4. After every motion command, wait until the axis completes its movement by using wait(axis).

# Note: This script assumes that objects such as Wmx3Lib_cm.motion, Motion_PosCommand, Motion_TriggerPosCommand,
# ProfileType, TriggerType, etc. are predefined in the motion control system environment.

# -----------------------------
# Step 1: Execute an absolute (non-triggered) position command for Axis 10.
posCommand = Motion_PosCommand()
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000   # using a default acceleration value
posCommand.profile.dec = 10000   # using a default deceleration value
posCommand.target = -800

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error on Axis 10 (to -800) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 10 to finish its motion.
Wmx3Lib_cm.motion.Wait(10)

# -----------------------------
# Step 2: Set up a triggered position command for Axis 10.
# When the remaining distance to the target becomes 200, trigger the move to position 300 with velocity 1000.
trigPos = Motion_TriggerPosCommand()
trigPos.axis = 10
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = 300

# Configure the trigger: trigger condition based on the remaining distance of Axis 10.
trigPos.trigger.triggerAxis = 10
trigPos.trigger.triggerType = TriggerType.RemainingDistance
trigPos.trigger.triggerValue = 200

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error on Axis 10 (to 300) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 10 to complete the triggered move.
Wmx3Lib_cm.motion.Wait(10)

# -----------------------------
# Step 3: Set an event triggered command for Axis 12.
# When Axis 10 reaches the absolute position of 100, trigger Axis 12 to move to -50.
eventTrigger = Motion_TriggerPosCommand()
eventTrigger.axis = 12
eventTrigger.profile.type = ProfileType.Trapezoidal
eventTrigger.profile.velocity = 600   # chosen velocity value for Axis 12
eventTrigger.profile.acc = 10000
eventTrigger.profile.dec = 10000
eventTrigger.target = -50

# Configure the trigger: trigger when Axis 10 equals position 100.
# (Assuming TriggerType.EqualPos is supported in this system.)
eventTrigger.trigger.triggerAxis = 10
eventTrigger.trigger.triggerType = TriggerType.EqualPos
eventTrigger.trigger.triggerValue = 100

ret = Wmx3Lib_cm.motion.StartPos_Trigger(eventTrigger)
if ret != 0:
    print('StartPos_Trigger error on Axis 12 (to -50) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 12 to finish its move.
Wmx3Lib_cm.motion.Wait(12)
