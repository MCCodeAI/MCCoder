
# Axes = [11]
# IOInputs = []
# IOOutputs = []

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 11
jogCommand.profile.velocity = 100
jogCommand.profile.acc = 1000
jogCommand.profile.dec = 3000

ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

sleep(1.1)

Wmx3Lib_cm.motion.Stop(11)
Wmx3Lib_cm.motion.Wait(11)
