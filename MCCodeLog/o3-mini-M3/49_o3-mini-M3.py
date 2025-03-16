
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set servo on for Axis 9 before starting any motion.
ret = Wmx3Lib_cm.axisControl.SetServoOn(9, 1)
if ret != 0:
    print('SetServoOn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Configure initial position command and trigger command for Axis 9.
pos = Motion_PosCommand()
tpos = Motion_TriggerPosCommand()
wait = Motion_WaitCondition()

# Set position command parameters for Axis 9.
pos.axis = 9
pos.profile.type = ProfileType.Trapezoidal
pos.profile.acc = 1000
pos.profile.dec = 1000
pos.target = 180
pos.profile.velocity = 30

# Start the initial continuous motion on Axis 9 (with velocity 30).
ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# In a continuous motion sequence we do not wait between trigger overrides.

# Configure triggered motion parameters for Axis 9.
tpos.axis = 9
tpos.profile.type = ProfileType.Trapezoidal
tpos.profile.acc = 1000
tpos.profile.dec = 1000
tpos.trigger.triggerAxis = 9
tpos.trigger.triggerType = TriggerType.CompletedTime
tpos.trigger.triggerValue = 700
tpos.target = 180

# Trigger override: Set velocity to 60 at 700ms.
tpos.profile.velocity = 60
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger (velocity 60) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Trigger override: Set velocity to 90 at 700ms.
tpos.profile.velocity = 90
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger (velocity 90) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Trigger override: Set velocity to 60 at 700ms.
tpos.profile.velocity = 60
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger (velocity 60 second override) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Trigger override: Set velocity to 30 at 700ms (final override).
tpos.profile.velocity = 30
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
if ret != 0:
    print('StartPos_Trigger (velocity 30 final override) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Finally, wait until Axis 9 stops moving after the continuous motion sequence is complete.
ret = Wmx3Lib_cm.motion.Wait(0)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
