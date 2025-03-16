
# Axes = [13]
# IOInputs = []
# IOOutputs = []

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 13
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

for _ in range(4):
    # Jog forward at 90 velocity
    jogCommand.profile.velocity = 90
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    sleep(1)
    Wmx3Lib_cm.motion.Stop(13)
    Wmx3Lib_cm.motion.Wait(13)
    
    # Jog backward at -90 velocity
    jogCommand.profile.velocity = -90
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    sleep(1)
    Wmx3Lib_cm.motion.Stop(13)
    Wmx3Lib_cm.motion.Wait(13)
