
# Axes = [8]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
tpos = Motion_TriggerPosCommand()
wait = Motion_WaitCondition()

# Set position command parameters
pos.axis = 8
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Set triggered position command parameters
tpos.axis = 8
tpos.profile.type = ProfileType.Trapezoidal
tpos.profile.velocity = 1000
tpos.profile.acc = 10000
tpos.profile.dec = 10000
tpos.trigger.triggerAxis = 8
tpos.trigger.triggerType = TriggerType.RemainingTime
tpos.trigger.triggerValue = 10

# Set wait condition parameters, waiting Axis 8 to be overridable
wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
wait.axisCount = 1
wait.SetAxis(8, 8)

# Execute motion to move axis by 30
pos.target = 30

ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to move axis by -30 when remaining time is 10ms
tpos.target = -30

ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
if ret != 0:
    print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until trigger motion executes
ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
if ret != 0:
    print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute motion to move axis by 60
pos.target = 60

ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is overridable
ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
if ret != 0:
    print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion to move axis by -60
tpos.target = -60

ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
if ret != 0:
    print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(8)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
