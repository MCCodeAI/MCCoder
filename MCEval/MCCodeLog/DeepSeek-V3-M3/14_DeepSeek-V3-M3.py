
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Jog Axis 4 for 120 milliseconds with a velocity of 90 using a TimeAccTrapezoidal profile
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.TimeAccTrapezoidal  # Corrected attribute name
jogCommand.axis = 4
jogCommand.profile.velocity = 90
jogCommand.profile.accTimeMilliseconds = 20
jogCommand.profile.decTimeMilliseconds = 20

# Rotate the motor at the specified speed.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Jogging for 120 milliseconds
sleep(0.12)

# Stop the axis after jogging
Wmx3Lib_cm.motion.Stop(4)

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(4)
