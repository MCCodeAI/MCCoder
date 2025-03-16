
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# First, move Axis 2 to 200.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error for Axis 2: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 2 reaches the target and stops.
Wmx3Lib_cm.motion.Wait(2)


# Next, move Axis 4 to 110.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error for Axis 4: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 reaches the target and stops.
Wmx3Lib_cm.motion.Wait(4)


# Now check if the difference between the commanded positions of Axis 2 and Axis 4 is 90.
# Based on our commands above, Axis 2 was commanded to 200 and Axis 4 to 110.
# So, diff = 200 - 110 = 90.
if (200 - 110) == 90:
    newTarget = 300
else:
    newTarget = 50

# Then, move both Axis 2 and Axis 4 to the new target.
# Start the command for Axis 2.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = newTarget
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error for Axis 2 to new target: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start the command for Axis 4.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = newTarget
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error for Axis 4 to new target: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until both Axis 2 and Axis 4 have reached their new target positions.
Wmx3Lib_cm.motion.Wait(2)
Wmx3Lib_cm.motion.Wait(4)
