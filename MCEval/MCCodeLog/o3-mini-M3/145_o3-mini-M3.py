
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Create a position command instance for the motion profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccTrapezoidal
posCommand.axis = 8
posCommand.target = -99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
# Corrected deceleration time: use a positive value instead of -50.
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to the target absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Exit or handle error as needed.
else:
    # Wait until axis 8 stops moving.
    Wmx3Lib_cm.motion.Wait(8)
