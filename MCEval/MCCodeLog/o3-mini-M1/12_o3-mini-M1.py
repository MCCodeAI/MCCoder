
# Axes = [12]
# IOInputs = []
# IOOutputs = []

# Create a jog command for Axis 12 using a sin profile.
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin  # Using sine profile as required
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000  # Default acceleration value
jogCommand.profile.dec = 10000  # Default deceleration value

# Start jogging on Axis 12
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error on Axis 12, code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jog for 1 second
sleep(1)

# Stop jogging and wait until Axis 12 stops moving
Wmx3Lib_cm.motion.Stop(12)
Wmx3Lib_cm.motion.Wait(12)
