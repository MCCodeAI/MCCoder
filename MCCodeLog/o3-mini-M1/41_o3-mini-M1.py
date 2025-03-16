
# Axes = [1]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
trigPos = Motion_TriggerPosCommand()

# Execute absolute position command on Axis 1 to move to 66.6 with a velocity of 600.
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

# Set up the triggered position command on Axis 1:
# When the remaining distance reaches 6.6, trigger Axis 1 to move to -66.6 with a velocity of 1000.
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
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 comes to a complete stop.
Wmx3Lib_cm.motion.Wait(0)
