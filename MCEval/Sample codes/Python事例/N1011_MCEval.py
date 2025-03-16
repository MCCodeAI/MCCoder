#Execute an absolute interpolation motion command to control Axis 0 and Axis 1, moving linearly to (0, 200) at a speed of 100 units per second. When the linear interpolation begins to decelerate, Axis 0 and Axis 1 should linearly interpolate to (200, 200) at the same speed of 100 units per second. Upon the next deceleration phase, Axis 0 and Axis 1 should linearly interpolate back to (0, 200) at 100 units per second. Set event 0 to set output 0.0 to 1 at position (160, 200)and set event 1 to set output 0.0 to 0 at position (60, 200) Finally, when the linear interpolation begins to decelerate again, Axis 0 and Axis 1 should linearly interpolate to (0, 0) at 100 units per second.
   # Axes = [0，1]

    #The basic steps in executing blending motion using the API buffer is as follows:
    # 1.Execute a linear or circular interpolation.
    # 2.Wait until deceleration starts for the linear or circular interpolation. This is typically near the end of the interpolation.
    # 3.Execute the next linear or circular interpolation. Because the previous interpolation has not finished yet, the next interpolation will be executed as a blending type override.
    # 4.Repeat steps 2 and 3 until the end of the path.
    # 5.Set event 0 to set output 0.0 to 1 at position (160, 200)，Set event 1 to set output 0.0 to 0 at position (60, 200)
    # Record and execute an API buffer with :
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    cond=ApiBufferCondition()

    #  Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    cond =ApiBufferCondition()
    lin =Motion_LinearIntplCommand()

    #First linear interpolation (0, 0) -> (200, 0)
    lin.axisCount=2
    lin.SetAxis(0,0)
    lin.SetAxis(1,1)
    lin.profile.type=ProfileType.Trapezoidal
    lin.profile.velocity=100
    lin.profile.acc=1000
    lin.profile.dec=1000
    lin.SetTarget(0,200)
    lin.SetTarget(1,0)

    #Execute interpolation command to move to a specified absolute position.
    ret=Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Wait until the first linear interpolation starts deceleration
    cond.bufferConditionType=ApiBufferConditionType.DecelerationStarted
    cond.arg_decelerationStarted.axis=0
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    #Second linear interpolation (200, 0) -> (200, 200)
    lin.SetTarget(0,200)
    lin.SetTarget(1,200)
    #Execute interpolation command to move to a specified absolute position.
    ret=Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Wait until the second linear interpolation starts deceleration
    cond.bufferConditionType=ApiBufferConditionType.DecelerationStarted
    cond.arg_decelerationStarted.axis=0
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    #Third linear interpolation (200, 200) -> (0, 200)
    lin.SetTarget(0,0)
    lin.SetTarget(1,200)
    #Execute interpolation command to move to a specified absolute position.
    ret=Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    eventIN = CoreMotionEventInput()
    eventOut = IoEventOutput()
    opt = EventOption()

    # Event ID
    posEventID1 = 0
    posEventID2 = 1
    # RemoveEvent
    Wmx3Lib_EventCtl.ClearAllEvent()
    Wmx3Lib_buf.Sleep(5)
    Wmx3Lib_EventCtl.RemoveEvent(posEventID1)
    Wmx3Lib_EventCtl.RemoveEvent(posEventID2)
    # Set event 0 to set output 0.0 to 1 at position (160, 200)
    eventIN.inputFunction = CoreMotionEventInputType.CompletedDistance
    eventIN.completedDistance.axis = 0
    eventIN.completedDistance.distance = 40
    eventIN.completedDistance.disableIdleAxisTrigger = 1

    eventOut.type = IoEventOutputType.SetIOOutBit
    eventOut.setIOOutBit.bitAddress = 0
    eventOut.setIOOutBit.byteAddress = 0
    eventOut.setIOOutBit.invert = 0
    eventOut.setIOOutBit.setOffState = 0
    # Automatically clear the event after it is finished
    opt.singleShot = False
    opt.disableAfterActivate = False
    opt.enable = True

    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_Option(eventIN, eventOut, opt)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return
    # DisableEvent
    ret = Wmx3Lib_EventCtl.EnableEvent(posEventID1, 0)

    # Set event 1 to set output 0.0 to 0 at position (60, 200)
    # eventIN.type=CoreMotionEventInput.completedDistance
    eventIN.inputFunction = CoreMotionEventInputType.CompletedDistance
    eventIN.completedDistance.axis = 0
    eventIN.completedDistance.distance = 140
    eventIN.completedDistance.disableIdleAxisTrigger = 1

    eventOut.type = IoEventOutputType.SetIOOutBit
    eventOut.setIOOutBit.bitAddress = 0
    eventOut.setIOOutBit.byteAddress = 0
    # Set the output bit low
    eventOut.setIOOutBit.invert = 1
    eventOut.setIOOutBit.setOffState = 0
    opt.enable = True

    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_Option(eventIN, eventOut, opt)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return
    # DisableEvent
    Wmx3Lib_EventCtl.EnableEvent(posEventID2, 0)

    # EnableEvent
    Wmx3Lib_EventCtl.EnableEvent(posEventID1, 1)
    Wmx3Lib_EventCtl.EnableEvent(posEventID2, 1)

    # Wait until the third linear interpolation starts deceleration
    cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
    cond.arg_decelerationStarted.axis = 0
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    Wmx3Lib_EventCtl.EnableEvent(posEventID1, 0)
    Wmx3Lib_EventCtl.EnableEvent(posEventID2, 0)
    #Wait until the third linear interpolation starts deceleration
    cond.bufferConditionType=ApiBufferConditionType.DecelerationStarted
    cond.arg_decelerationStarted.axis=0
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    #Fourth linear interpolation (0, 200) -> (0, 0)
    lin.SetTarget(0,0)
    lin.SetTarget(1,0)
    #Execute interpolation command to move to a specified absolute position.
    ret=Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()

    #Drive the motion accumulated in the buffer so far.
    Wmx3Lib_buf.Execute(0)

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 0)
    axes.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

