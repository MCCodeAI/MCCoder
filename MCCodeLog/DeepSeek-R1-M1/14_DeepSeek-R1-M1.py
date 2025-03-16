
# Axes = [4]
# IOInputs = []
# IOOutputs = []

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.TimeAccAdvancedS
jogCommand.axis = 4
jogCommand.profile.velocity = 90
jogCommand.profile.accTimeMilliseconds = 20
jogCommand.profile.decTimeMilliseconds = 20
jogCommand.profile.jerkAccRatio = 0.5
jogCommand.profile.jerkDecRatio = 0.5
jogCommand.profile.startingVelocity = 0
jogCommand.profile.endVelocity = 0

# Execute jog command
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jog for 120 milliseconds
sleep(0.12)

# Stop axis and wait for motion to complete
Wmx3Lib_cm.motion.Stop(4)
Wmx3Lib_cm.motion.Wait(4)
