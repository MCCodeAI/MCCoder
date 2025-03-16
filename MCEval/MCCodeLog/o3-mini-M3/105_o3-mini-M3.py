
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to position 180 using 1100 velocity.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 180
posCommand.profile.velocity = 1100
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 5 stops moving after the absolute move.
Wmx3Lib_cm.motion.Wait(5)

# Now perform 5 continuous relative moves of -10 distance each.
for i in range(5):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    # For a relative move, target is specified as the distance to move.
    posCommand.target = -10
    posCommand.profile.velocity = 1100
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print("StartMov error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait until the axis completes this relative move before starting the next.
    Wmx3Lib_cm.motion.Wait(5)
