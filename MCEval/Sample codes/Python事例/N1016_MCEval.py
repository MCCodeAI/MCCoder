#Set the negative direction BacklashCompensation for Axis 0.Then, Axis 0 moves from 300 to the absolute position 0 at a speed of 100.
    # Axes = [0]

    # <log ---------------------------------------------------------------------------
    WMX3Log = Log(Wmx3Lib)

    ret = WMX3Log.StopLog(0)
    sleep(0.01)

    axislist = [0]
    num = len(axislist)

    # Set Axis numbers and control variables of log
    cmLogIn_0 = CoreMotionLogInput()
    cmLogIn_0.axisSelection.axisCount = num
    for i in range(0, num):
        cmLogIn_0.axisSelection.SetAxis(i, axislist[i])

    # Control variables to log
    cmLogIn_0.axisOptions.commandPos = 1
    cmLogIn_0.axisOptions.compCommandPos=1
    cmLogIn_0.axisOptions.feedbackPos = 0
    cmLogIn_0.axisOptions.commandVelocity = 0
    cmLogIn_0.axisOptions.feedbackVelocity = 0

    # Set up log time
    option = LogChannelOptions()
    option.samplingPeriodInCycles = 1
    option.samplingTimeMilliseconds = 1000000

    ret = WMX3Log.SetLogOption(0, option)
    if ret != 0:
        print('SetLogOption error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)
    ret = WMX3Log.SetCustomLog(0, cmLogIn_0)
    if ret != 0:
        print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)

    # Set log file address
    path_0 = LogFilePath()
    WMX3Log.GetLogFilePath(0)
    path_0.dirPath = "C:\\"
    path_0.fileName = f"1016_MCEval_Log.txt"
    ret = WMX3Log.SetLogFilePath(0, path_0)
    if ret != 0:
        print('SetLogFilePath error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return

    # Start log
    ret = WMX3Log.StartLog(0)
    if ret != 0:
        print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.01)
    # log> ---------------------------------------------------------------------------
    #Set the negative direction BacklashCompensation for Axis 0.Then, Axis 0 moves from 0 to the absolute position 300 at a speed of 100.
    Wmx3Lib_comp=Compensation(Wmx3Lib)

    # Create a command value of target as 300.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 300
    posCommand.profile.velocity = 100
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    backlashcomp=BacklashCompensationData()
    ##If 1, backlash compensation is enabled. If 0, backlash compensation is disabled.
    backlashcomp.enable=1
    #If 1, positive backlash compensation is applied. If -1, negative backlash compensation is applied.
    backlashcomp.offsetDirection=-1
    #The maximum backlash compensation offset, in user units.
    backlashcomp.backlashHigh=20
    #The minimum backlash compensation offset, in user units.
    backlashcomp.backlashLow=5
    #The distance after reversing direction above which the maximum backlash compensation is applied, in user units.
    backlashcomp.distanceHigh=200
    #The distance after reversing direction below which the minimum backlash compensation is applied, in user units.
    backlashcomp.distanceLow=100

    #Set the BacklashCompensation for Axis 0.
    ret =Wmx3Lib_comp.SetBacklashCompensation(0,backlashcomp)
    if ret != 0:
        print('SetBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

    # Create a command value of target as 0.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 0
    posCommand.profile.velocity = 100
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    ret=Wmx3Lib_comp.DisableBacklashCompensation(0)
    if ret != 0:
        print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

    # <log ---------------------------------------------------------------------------
    sleep(0.1)
    # Stop log
    ret = WMX3Log.StopLog(0)
    if ret!=0:
        print('StopLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    # log> -

