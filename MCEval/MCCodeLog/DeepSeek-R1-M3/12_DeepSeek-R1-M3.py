
# Axes = [12]
# IOInputs = []
# IOOutputs = []

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

sleep(1)

Wmx3Lib_cm.motion.Stop(12)
Wmx3Lib_cm.motion.Wait(12)
