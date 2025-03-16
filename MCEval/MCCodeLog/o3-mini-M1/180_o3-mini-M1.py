
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# The following script moves Axis 3 in a sequence of target positions:
# 1. Move to position 30
# 2. Move to position 0
# 3. Move to position 30
# 4. Move to position 0
#
# Each motion command uses the ConstantDec profile with a starting velocity of 100 and
# an end velocity of 0. The script waits for the axis to stop after each motion before
# sending the next command.

# List of target positions
targets = [30, 0, 30, 0]

for target in targets:
    # Create a new motion command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.ConstantDec
    posCommand.axis = 3
    posCommand.target = target
    posCommand.profile.startingVelocity = 100
    posCommand.profile.endVelocity = 0

    # Execute the position command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break  # Stop execution if a command fails

    # Wait until Axis 3 reaches the target position and stops moving
    Wmx3Lib_cm.motion.Wait(3)
