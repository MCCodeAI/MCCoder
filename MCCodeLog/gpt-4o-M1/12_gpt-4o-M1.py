
# Axes = [12]
# IOInputs = []
# IOOutputs = []

# Create a jog command for Axis 12 with a sine profile
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sine
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000
jogCommand.profile.dec = 10000

# Start jogging the axis
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1 second
sleep(1)

# Stop jogging
Wmx3Lib_cm.motion.Stop(12)

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(12)
