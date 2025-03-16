
# Axes = [12]
# IOInputs = []
# IOOutputs = []

# Create a jog command for Axis 12 using a sin profile.
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Sin  # Use the sin profile for smooth sine motion
jogCommand.axis = 12
jogCommand.profile.velocity = 90

# Set acceleration parameters to valid values to avoid out-of-range errors.
jogCommand.profile.acceleration = 100    # Must be >0 and within the acceptable range
jogCommand.profile.deceleration = 100    # Similarly, set a proper deceleration value
jogCommand.profile.jerkAcc = 10          # Adjust jerk acceleration value to be within valid limits
jogCommand.profile.jerkDec = 10          # Adjust jerk deceleration accordingly

# Start jogging on Axis 12.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 1 second.
sleep(1)

# Stop the jog command for Axis 12.
Wmx3Lib_cm.motion.Stop(12)

# Wait until Axis 12 has completely stopped.
Wmx3Lib_cm.motion.Wait(12)
