
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

def main():
    # Create a Motion_LinearIntplCommand object for the motion command
    lin = Motion_LinearIntplCommand()
    
    # Specify that we are controlling two axes: Axis 1 and Axis 2.
    lin.axisCount = 2
    lin.SetAxis(0, 1)
    lin.SetAxis(1, 2)
    
    # Set the motion profile (using a trapezoidal profile)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    
    # Set target positions: Axis 1 to 100 and Axis 2 to 150.
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 150)
    
    # Start the absolute linear interpolation motion command.
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print("StartLinearIntplPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for the motion to complete on both axes by using a blocking wait command.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 2)
    
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
