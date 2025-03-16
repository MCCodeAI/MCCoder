
# Axes = [0]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
trigPos = Motion_TriggerPosCommand()

# Execute initial absolute position command
pos.axis = 0
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 600
pos.profile.acc = 10000
pos.profile.dec = 10000
pos.profile.endVelocity = 600
pos.target = -66.6

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Setup and execute triggered motion command
trigPos.axis = 0
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = 66.6
trigPos.trigger.triggerType = TriggerType.RemainingTime
trigPos.trigger.triggerAxis = 0
trigPos.trigger.triggerValue = 100

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis completes all motions
Wmx3Lib_cm.motion.Wait(0)
