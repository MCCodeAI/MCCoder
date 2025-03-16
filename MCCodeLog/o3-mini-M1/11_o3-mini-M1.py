
# Axes = [11]
# IOInputs = []
# IOOutputs = []

# Create and configure a jog command for Axis 11
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 11
jogCommand.profile.velocity = 100
jogCommand.profile.acc = 1000
# Set the deceleration value to be used when stopping the motion
jogCommand.profile.dec = 3000

# Start jogging Axis 11
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jog for 1.1 seconds
sleep(1.1)

# Stop Axis 11 (the deceleration parameter is applied as configured in the jog command)
Wmx3Lib_cm.motion.Stop(11)

# Wait until Axis 11 has stopped moving
Wmx3Lib_cm.motion.Wait(11)
