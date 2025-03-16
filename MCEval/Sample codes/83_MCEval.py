# Write Python code to set the positive direction BacklashCompensation for Axis 14. Then, Move Axis 14 from 0 to the absolute position 300 at a speed of 1000.
# Axes = [14]

    # <log ---------------------------------------------------------------------------

    # Stop log just in case logging is on.
    ret = WMX3Log.StopLog(0)
    sleep(0.01)

    # Log the command position after applying compensation offsets. This is necessary to compare if compensation works as expected.
    cmLogIn_0.axisOptions.compCommandPos = 1

    ret = WMX3Log.SetCustomLog(0, cmLogIn_0)
    if ret != 0:
        print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)

    # Start log
    ret = WMX3Log.StartLog(0)
    if ret != 0:
        print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.01)
    # log> ---------------------------------------------------------------------------

    # Set the positive direction BacklashCompensation for Axis 14. Then, Axis 14 moves from 0 to the absolute position 300 at a speed of 100.
    Wmx3Lib_comp = Compensation(Wmx3Lib)

    backlashcomp = BacklashCompensationData()
    # If 1, backlash compensation is enabled. If 0, backlash compensation is disabled.
    backlashcomp.enable = 1
    # If 1, positive backlash compensation is applied. If -1, negative backlash compensation is applied.
    backlashcomp.offsetDirection = 1
    # The maximum backlash compensation offset, in user units.
    backlashcomp.backlashHigh = 20
    # The minimum backlash compensation offset, in user units.
    backlashcomp.backlashLow = 5
    # The distance after reversing direction above which the maximum backlash compensation is applied, in user units.
    backlashcomp.distanceHigh = 200
    # The distance after reversing direction below which the minimum backlash compensation is applied, in user units.
    backlashcomp.distanceLow = 100

    # Set the BacklashCompensation for Axis 14.
    ret = Wmx3Lib_comp.SetBacklashCompensation(14, backlashcomp)
    if ret != 0:
        print('SetBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

    # Create a command value of target as 300.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 14
    posCommand.target = 300
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(14)

    # Disable Backlash Compensation is a necessary step! 
    ret = Wmx3Lib_comp.DisableBacklashCompensation(14)
    if ret != 0:
        print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return
