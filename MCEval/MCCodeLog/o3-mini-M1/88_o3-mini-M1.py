
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Set the positive direction Backlash Compensation for Axis 8 with:
#   Backlash High = 11, Backlash Low = 4,
#   Distance High = 80, Distance Low = 30.
# Then, move Axis 8 from 0 to the absolute position 122.6 at a speed of 2000.
def main():
    # Create an instance of the backlash compensation library
    Wmx3Lib_comp = Compensation(Wmx3Lib)

    # Configure the backlash compensation parameters for Axis 8.
    backlashcomp = BacklashCompensationData()
    backlashcomp.enable = 1                   # Enable backlash compensation.
    backlashcomp.offsetDirection = 1          # 1 for positive direction backlash compensation.
    backlashcomp.backlashHigh = 11            # Maximum backlash compensation offset.
    backlashcomp.backlashLow = 4              # Minimum backlash compensation offset.
    backlashcomp.distanceHigh = 80            # Distance after reversing direction for maximum compensation.
    backlashcomp.distanceLow = 30             # Distance after reversing direction for minimum compensation.

    ret = Wmx3Lib_comp.SetBacklashCompensation(8, backlashcomp)
    if ret != 0:
        print('SetBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

    # Create a motion command to move Axis 8 to the absolute position 122.6 with a velocity of 2000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 122.6
    posCommand.profile.velocity = 2000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 has reached the target position and stopped.
    Wmx3Lib_cm.motion.Wait(8)

    # Disable backlash compensation for Axis 8 once motion is complete.
    ret = Wmx3Lib_comp.DisableBacklashCompensation(8)
    if ret != 0:
        print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

if __name__ == '__main__':
    from time import sleep  # Import sleep if needed for additional timing adjustments.
    main()
