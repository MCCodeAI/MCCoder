
# Axes = [1]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
trigPos = Motion_TriggerPosCommand()

# Execute initial absolute position command for Axis 1 to move to 66.6 at a velocity of 600.
pos.axis = 1
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 600
pos.profile.acc = 10000
pos.profile.dec = 10000
pos.profile.endVelocity = 600
pos.target = 66.6

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute the triggered position command:
# When the remaining distance for Axis 1 reaches 6.6, trigger it to move to -66.6 at a velocity of 1000.
trigPos.axis = 1
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = -66.6
trigPos.trigger.triggerAxis = 1
trigPos.trigger.triggerType = TriggerType.RemainingDistance
trigPos.trigger.triggerValue = 6.6

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to complete its motion.
Wmx3Lib_cm.motion.Wait(0)
