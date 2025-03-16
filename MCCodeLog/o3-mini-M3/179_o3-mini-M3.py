
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to the position -580 at a speed of 100000, acceleration of 10000,
# deceleration of 20000, starting velocity of 0 and end velocity of 0 using a Sin profile.

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sin  # Corrected from ProfileType.Sine to ProfileType.Sin
posCommand.axis = 8
posCommand.target = -580
posCommand.profile.velocity = 100000
posCommand.profile.acc = 10000
posCommand.profile.dec = 20000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move Axis 8 to the target position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 8 stops moving.
    Wmx3Lib_cm.motion.Wait(8)
