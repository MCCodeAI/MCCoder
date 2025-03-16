
# Axes = [1]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
trigPos = Motion_TriggerPosCommand()

# Execute normal motion command
pos.axis = 1
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 600
pos.profile.acc = 10000
pos.profile.dec = 10000
pos.target = 66.6

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion command
trigPos.axis = 1
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = -66.6
trigPos.trigger.triggerType = TriggerType.RemainingDistance
trigPos.trigger.triggerAxis = 1
trigPos.trigger.triggerValue = 6.6

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StarttrigPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
