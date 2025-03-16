
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Define the positions to move Axis 1 to
positions = [10, -10, 100, -100, 0]

# Define the motion parameters
speed = 1000
accTimeMilliseconds = 50
decTimeMilliseconds = 50
startingVelocity = 0
endVelocity = 0

# Loop through each position and move Axis 1
for position in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = position
    posCommand.profile.velocity = speed
    posCommand.profile.accTimeMilliseconds = accTimeMilliseconds
    posCommand.profile.decTimeMilliseconds = decTimeMilliseconds
    posCommand.profile.startingVelocity = startingVelocity
    posCommand.profile.endVelocity = endVelocity

    # Execute command to move from current position to specified absolute position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(1)
