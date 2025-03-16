
# Axes = [10]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
tpos = Motion_TriggerPosCommand()
wait = Motion_WaitCondition()

# Set position command parameters
pos.axis = 10
tpos.axis = 10
tpos.trigger.triggerAxis = 10
tpos.trigger.triggerType = TriggerType.CompletedTime
tpos.trigger.triggerValue = 1000

# Set wait condition parameters
wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
wait.axisCount = 1
wait.SetAxis(0, 10)

# Define target positions and profiles
target_positions = [-10, 20, -30, 40, 0]
profiles = [
    ProfileType.TimeAccAdvancedS,
    ProfileType.TwoVelocityTrapezoidal,
    ProfileType.ConstantDec,
    ProfileType.ParabolicVelocity,
    ProfileType.JerkRatioFixedVelocityS
]

for i, (target, profile_type) in enumerate(zip(target_positions, profiles)):
    pos.profile.type = profile_type
    
    if profile_type == ProfileType.TimeAccAdvancedS:
        pos.profile.accTime = 500  # Acceleration time in milliseconds
        pos.profile.decTime = 500  # Deceleration time in milliseconds
    elif profile_type == ProfileType.TwoVelocityTrapezoidal:
        pos.profile.velocity = 1000  # First velocity
        pos.profile.secondVelocity = 2000  # Second velocity
    elif profile_type == ProfileType.JerkRatioFixedVelocityS:
        pos.profile.jerkAccRatio = 0.5
        pos.profile.jerkDecRatio = 0.5
        pos.profile.startingVelocity = 0
        pos.profile.endVelocity = 0
    
    pos.target = target

    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print(f'StartPos error code is {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        break

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print(f'Wait error code is {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        break
