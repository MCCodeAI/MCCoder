
# Axes = [12]
# Inputs = []
# Outputs = []

# Define the jog command for Axis 12
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin  # Corrected from Sine to Sin
jogCommand.axis = 12
jogCommand.profile.velocity = 90
jogCommand.profile.acc = 10000  # Assuming a default acceleration value
jogCommand.profile.dec = 10000  # Assuming a default deceleration value

# Start jogging the axis
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1 second
sleep(1)

# Stop the jog motion
Wmx3Lib_cm.motion.Stop(12)

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(12)
