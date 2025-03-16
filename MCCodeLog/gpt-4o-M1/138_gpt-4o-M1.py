
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Define motion command and wait condition classes
pos = Motion_PosCommand()
wait = Motion_WaitCondition()

# Set axis number
pos.axis = 10

# Define a list of target positions and corresponding profiles
target_positions = [-10, 20, -30, 40, 0]
profiles = [
    ProfileType.TimeAccAdvancedS,
    ProfileType.TwoVelocityTrapezoidal,
    ProfileType.ConstantDec,
    ProfileType.ParabolicVelocity,
    ProfileType.JerkRatioFixedVelocityS
]

# Iterate over each target position and profile
for target, profile in zip(target_positions, profiles):
    # Set position command parameters
    pos.profile.type = profile
    pos.target = target

    # Execute motion command
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
