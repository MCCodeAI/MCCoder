
# Axes = [11]
# IOInputs = []
# IOOutputs = []

# Jog Axis 11 for 1.1 seconds with a velocity of 100 and an acceleration of 1000, then stop with a deceleration of 3000.

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 11
jogCommand.profile.velocity = 100
jogCommand.profile.acc = 1000
jogCommand.profile.dec = 3000

# Rotate the motor at the specified speed.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1.1 seconds
sleep(1.1)

# Stop the jog motion
Wmx3Lib_cm.motion.Stop(11)

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(11)
