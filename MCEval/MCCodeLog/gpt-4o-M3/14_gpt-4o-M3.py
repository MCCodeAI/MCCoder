
# Axes = [4]
# Inputs = []
# Outputs = []

# Create a jog command for Axis 4
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.TimeAccTrapezoidal  # Corrected the profile type
jogCommand.axis = 4
jogCommand.profile.velocity = 90
jogCommand.profile.accTimeMilliseconds = 20
jogCommand.profile.decTimeMilliseconds = 20

# Start jogging the axis
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Jogging for 120 milliseconds
    sleep(0.12)

    # Stop the jog motion
    Wmx3Lib_cm.motion.Stop(4)

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(4)
