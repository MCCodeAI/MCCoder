
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 1 sequentially to the following positions:
# 10, -10, 10, -10, 10, -10, 10, -10, 0
# Each move uses a TimeAccSCurve profile with:
#   velocity = 1000,
#   accTimeMilliseconds = 50,
#   decTimeMilliseconds = 50,
#   startingVelocity = 0,
#   endVelocity = 0
#
# It waits for the axis to stop moving after every single motion.

# List of target positions for Axis 1.
positions = [10, -10, 10, -10, 10, -10, 10, -10, 0]

for target in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 1 reaches its target position and stops.
    Wmx3Lib_cm.motion.Wait(1)
