
# Axes = [12]
# IOInputs = []
# IOOutputs = []

# Jog Axis 12 for 1 second with a velocity of 90 using a sin profile.
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

# Rotate the motor at the specified speed.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1 second
sleep(1)

# Stop the jogging motion
Wmx3Lib_cm.motion.Stop(12)

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(12)
