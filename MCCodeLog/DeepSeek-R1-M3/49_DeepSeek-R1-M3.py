
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
tpos.trigger.triggerValue = 700  # 700ms completed time trigger
tpos.target = 180

# Set wait condition parameters
wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
wait.axisCount = 1
wait.SetAxis(0, 9)

# Execute initial motion with 30 velocity
pos.profile.velocity = 30
ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print(f'StartPos error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()

# Velocity override sequence with trigger commands
velocity_sequence = [60, 90, 60, 30]
for velocity in velocity_sequence:
    tpos.profile.velocity = velocity
    
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
    if ret != 0:
        print(f'StartPos_Trigger error {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()
    
    # Wait for trigger condition after each command
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print(f'Wait_WaitCondition error {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()

# Final wait for motion completion
ret = Wmx3Lib_cm.motion.Wait(9)
if ret != 0:
    print(f'Final Wait error {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()
