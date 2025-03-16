# Write python code to Execute an absolute position triggered circular interpolation motion command.Control Axis 0 and Axis 1 to perform a clockwise circular interpolation with a 50 radius to pisition (100, 0) at a velocity of 1000. Wait for 1 millisecond, then execute the trigger circular interpolation motion command. When the remaining distance of Axis 0 is 80, trigger Axis 0 and Axis 1 to perform a clockwise circular interpolation (200, 0).
    # Axes = [0, 1]

    cir = Motion_RadiusAndEndCircularIntplCommand()
    trig = Trigger()

    # Execute normal motion command
    cir.SetAxis(0, 0)
    cir.SetAxis(1, 1)

    cir.profile.type = ProfileType.Trapezoidal
    cir.profile.velocity = 1000
    cir.profile.acc = 10000
    cir.profile.dec = 10000

    cir.SetEndPos(0, 100)
    cir.SetEndPos(1, 0)

    cir.radius = 50
    cir.clockwise = 1

    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_RadiusAndEnd(cir)
    if ret != 0:
        print('StartCircularIntplPos_RadiusAndEnd error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    sleep(0.001)

    cir.SetEndPos(0, 200)
    cir.SetEndPos(1, 0)

    trig.triggerAxis = 0
    trig.triggerType = TriggerType.RemainingDistance
    trig.triggerValue = 80

    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_RadiusAndEnd_Trigger(cir, trig)
    if ret != 0:
        print('StartCircularIntplPos_RadiusAndEnd_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
