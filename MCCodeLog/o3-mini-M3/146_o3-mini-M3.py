
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to the position 144 with velocity 1000, acceleration 10000, deceleration 10000, 
# starting velocity 30, and end velocity 0, using an S profile (Sine profile).
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sin  # Corrected from 'Sine' to 'Sin'
posCommand.axis = 4
posCommand.target = 144
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 4 reaches position 144 and stops.
    Wmx3Lib_cm.motion.Wait(4)

# Then move Axis 4 to the position 0 with the same motion parameters and S profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sin  # Corrected from 'Sine' to 'Sin'
posCommand.axis = 4
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 4 reaches position 0 and stops.
    Wmx3Lib_cm.motion.Wait(4)
