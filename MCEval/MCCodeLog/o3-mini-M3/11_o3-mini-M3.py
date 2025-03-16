
# Axes = [11]
# IOInputs = []
# IOOutputs = []

# Create a jog command for Axis 11.
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 11
jogCommand.profile.velocity = 100
jogCommand.profile.acc = 1000
jogCommand.profile.dec = 3000

# Start jogging Axis 11.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Continue jogging for 1.1 seconds.
sleep(1.1)

# Issue a stop command for Axis 11.
ret = Wmx3Lib_cm.motion.Stop(11)
if ret != 0:
    print('Stop error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 11 has fully stopped.
Wmx3Lib_cm.motion.Wait(11)
