
# Axes = [13]
# IOInputs = []
# IOOutputs = []

import time

def jog_axis(axis, velocity, duration):
    # Create a jog command for the specified axis and velocity.
    jogCommand = Motion_JogCommand()
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.axis = axis
    jogCommand.profile.velocity = velocity
    jogCommand.profile.acc = 10000  # Using example acceleration value.
    jogCommand.profile.dec = 10000  # Using example deceleration value.

    # Start jogging the axis.
    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print("StartJog error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Jog for the specified duration.
    time.sleep(duration)

    # Stop jogging the specified axis.
    Wmx3Lib_cm.motion.Stop(axis)

    # Wait until the axis stops moving.
    Wmx3Lib_cm.motion.Wait(axis)

def main():
    axis = 13
    cycles = 4
    for _ in range(cycles):
        # Jog Axis 13 for 1 second with a velocity of 90.
        jog_axis(axis, 90, 1)
        # Jog Axis 13 for 1 second with a velocity of -90.
        jog_axis(axis, -90, 1)

if __name__ == "__main__":
    main()
