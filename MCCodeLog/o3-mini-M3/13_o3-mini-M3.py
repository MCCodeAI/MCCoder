
# Axes = [13]
# IOInputs = []
# IOOutputs = []

def jog_axis_13_back_and_forth():
    # Create a jog command object for Axis 13.
    jogCommand = Motion_JogCommand()

    # Set common motion profile parameters.
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.profile.acc = 10000
    jogCommand.profile.dec = 10000
    jogCommand.axis = 13

    # Repeat the back-and-forth motion 4 times.
    for _ in range(4):
        # Jog Axis 13 with a positive velocity of 90 for 1 second.
        jogCommand.profile.velocity = 90
        ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
        if ret != 0:
            print('StartJog (velocity 90) error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Jogging for 1 second.
        sleep(1)

        # Stop the motion and wait until Axis 13 stops.
        Wmx3Lib_cm.motion.Stop(13)
        Wmx3Lib_cm.motion.Wait(13)

        # Jog Axis 13 with a negative velocity of -90 for 1 second.
        jogCommand.profile.velocity = -90
        ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
        if ret != 0:
            print('StartJog (velocity -90) error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Jogging for 1 second.
        sleep(1)

        # Stop the motion and wait until Axis 13 stops.
        Wmx3Lib_cm.motion.Stop(13)
        Wmx3Lib_cm.motion.Wait(13)

# Execute the jogging sequence.
jog_axis_13_back_and_forth()
