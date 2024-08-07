# Write python code to Start a relative position linear interpolation motion command of Axis 0 and 1 with  (200, -150) distance with 1000 velocity.
    # Axes = [0, 1]
    
    # Create a command value of relative distance of (200, -150).
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2 
    lin.SetAxis(0,0)
    lin.SetAxis(1,1) 

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    lin.SetTarget(0,200)  #Set target of Axis 0 to be 300
    lin.SetTarget(1,-150)  #Set target of Axis 1 to be 100

    # Start an relative position linear interpolation motion command.
    ret =Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
    if ret!=0:
            print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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
    
