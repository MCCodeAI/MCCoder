
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create a motion command for a ConstantDec profile to move Axis 0 to position 10.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 0
posCommand.target = 10
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Execute command to move the axis to the target position using a ConstantDec profile.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed
else:
    # Wait until the axis stops moving after completing the motion.
    Wmx3Lib_cm.motion.Wait(0)
