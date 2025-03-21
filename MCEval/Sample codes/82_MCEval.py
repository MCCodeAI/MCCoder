# Write Python code to set the pitch error compensation table for Axis 0 with the following data points: (0, 10), (100, -10), (200, 15), (300, -15).The edgeDropoffDistance parameter is set to 50.Then, Axis 0 moves from -100 to the absolute position 300 at a speed of 100.
   # Axes = [0]

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

    #Set the pitch error compensation table for Axis 0 with the following data points: (0, 10), (100, -10), (200, 15), (300, -15).The edgeDropoffDistance parameter is set to 50.Then, Axis 0 moves from -100 to the absolute position 300 at a speed of 100.
    # Create a command value of target as -100.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = -100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    Wmx3Lib_comp=Compensation(Wmx3Lib)
    piterror=PitchErrorCompensationData()
    # 1:Enable pitch error compensation  0:Disable pitch error compensation
    piterror.enable=1
    # The distance between pitch points, in user units.
    piterror.pitchInterval=100
    #The number of pitch points
    piterror.pitchCount=4
    #The index of the pitch origin.
    piterror.pitchOriginIndex=0
    #The command position at the pitch origin, in user units.
    piterror.pitchOriginPosition=0
    #The distance beyond the first and last pitch points at which the offset reduces to 0, in user units. If this parameter is set to 0, the offset will not reduce to 0 at command positions beyond the first and last pitch points.
    piterror.edgeDropoffDistance=50

    #Add a pitch error compensation table.
    piterror.SetPitchCompensationValue(0,10)
    piterror.SetPitchCompensationValue(1,-10)
    piterror.SetPitchCompensationValue(2,15)
    piterror.SetPitchCompensationValue(3,-15)

    #Set the pitch compensation function for Axis 0.
    ret =Wmx3Lib_comp.SetPitchErrorCompensation(0,piterror)
    if ret != 0:
        print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
        return

    # Create a command value of target as 300.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 300
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)


