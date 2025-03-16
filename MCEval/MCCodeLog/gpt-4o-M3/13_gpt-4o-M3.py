
# Axes = [13]
# Inputs = []
# Outputs = []

from time import sleep

# Define a function to jog an axis with a specified velocity for a given duration
def jog_axis(axis, velocity, duration):
    jogCommand = Motion_JogCommand()
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.axis = axis
    jogCommand.profile.velocity = velocity
    jogCommand.profile.acc = 10000
    jogCommand.profile.dec = 10000

    # Start jogging the axis
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Jogging for the specified duration
    sleep(duration)

    # Stop jogging
    Wmx3Lib_cm.motion.Stop(axis)

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(axis)

# Jog Axis 13 back and forth 4 times
for _ in range(4):
    jog_axis(13, 90, 1)   # Jog forward
    jog_axis(13, -90, 1)  # Jog backward
