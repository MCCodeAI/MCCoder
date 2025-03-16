
# Axes = [9]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
tpos = Motion_TriggerPosCommand()
wait = Motion_WaitCondition()

# Set position command parameters
pos.axis = 9
pos.profile.type = ProfileType.Trapezoidal
pos.profile.acc = 1000
pos.profile.dec = 1000
pos.target = 180

# Set triggered position command parameters
tpos.axis = 9
tpos.profile.type = ProfileType.Trapezoidal
tpos.profile.acc = 1000
tpos.profile.dec = 1000
tpos.trigger.triggerAxis = 9
tpos.trigger.triggerType = TriggerType.CompletedTime
tpos.trigger.triggerValue = 700
tpos.target = 180

# Set wait condition parameters
wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
wait.axisCount = 1
wait.SetAxis(0, 9)

# Execute motion to move axis forward 30
pos.profile.velocity = 30

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to change axis velocity to 60
tpos.profile.velocity = 60

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until trigger motion executes
ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
if ret != 0:
    print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to change axis velocity to 90
tpos.profile.velocity = 90

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until trigger motion executes
ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
if ret != 0:
    print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to change axis velocity to 60
tpos.profile.velocity = 60

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until trigger motion executes
ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
if ret != 0:
    print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to change axis velocity to 30
tpos.profile.velocity = 30
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(9)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
