
# Axes = [13]
# IOInputs = []
# IOOutputs = []

# Jog Axis 13 for 1 second with a velocity of 90, then jog for 1 second with a velocity of -90, repeating this back-and-forth motion 4 times.

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 13
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

for _ in range(4):
    # Jog forward with velocity 90
    jogCommand.profile.velocity = 90
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Jogging for 1 second
    sleep(1)

    Wmx3Lib_cm.motion.Stop(13)
    Wmx3Lib_cm.motion.Wait(13)

    # Jog backward with velocity -90
    jogCommand.profile.velocity = -90
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Jogging for 1 second
    sleep(1)

    Wmx3Lib_cm.motion.Stop(13)
    Wmx3Lib_cm.motion.Wait(13)
