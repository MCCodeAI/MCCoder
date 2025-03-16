
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Create an absolute position command to move Axis 1 to position 101 using a Trapezoidal profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal  # Corrected from Tixing to Trapezoidal
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 10
posCommand.profile.endVelocity = 0

# Execute the motion command to move to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis has completed its movement.
Wmx3Lib_cm.motion.Wait(1)
