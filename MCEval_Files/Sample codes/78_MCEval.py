# Write Python code to record and execute an API buffer with :Move Axis 3 to a relative position of 100 at a speed of 1000. Then it move to a relative position of -100. Auto Rewind is enabled. After executing, the api buffer will auto rewind and stop after 3s.
# Axes = [3]

    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    opt=ApiBufferOptions()

    #  Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    cond =ApiBufferCondition()

    # Add a position command to the API buffer.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 3
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified relative position.
    ret=Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Pause execution until both axes have finished motion
    Wmx3Lib_buf.Wait(3)

    #Add a position command to the API buffer
    posCommand.target =-100
    # Execute command to move to a specified relative position.
    ret=Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Pause execution until both axes have finished motion
    Wmx3Lib_buf.Wait(3)

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()

    #Set the API buffer execution options
    opt.autoRewind=True
    Wmx3Lib_buf.SetOptions(0,opt)

    # Drive the motion accumulated in the buffer so far.
    Wmx3Lib_buf.Execute(0)

    #After a delay of 10 seconds, a stop function is called to forcibly halt the execution.
    sleep(3)

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

