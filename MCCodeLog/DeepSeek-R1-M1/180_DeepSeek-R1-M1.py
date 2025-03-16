
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to positions 30, 0, 30, and 0 using ConstantDec profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# List of target positions to move to
target_positions = [30, 0, 30, 0]

for target in target_positions:
    posCommand.target = target
    
    # Execute motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break
    
    # Wait until the axis reaches the target position and stops
    Wmx3Lib_cm.motion.Wait(3)
