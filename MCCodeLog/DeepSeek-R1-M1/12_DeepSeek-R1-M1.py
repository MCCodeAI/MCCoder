
# Axes = [12]
# IOInputs = []
# IOOutputs = []

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

# Rotate the motor with sinusoidal profile
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1 second
sleep(1)

# Stop axis motion
Wmx3Lib_cm.motion.Stop(12)

# Wait for axis to completely stop
Wmx3Lib_cm.motion.Wait(12)
