
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

def main():
    # Create an instance of the PVT Interpolation Command for two axes.
    pvti = Motion_PVTIntplCommand()
    
    # Configure the command with the two axes (Axis 3 and Axis 6)
    pvti.axisCount = 2
    pvti.SetAxis(0, 3)
    pvti.SetAxis(1, 6)
    
    # There are 5 points to be defined.
    pvti.SetPointCount(0, 5)
    pvti.SetPointCount(1, 5)
    
    # Create instances of a PVT point for each axis.
    pvtparameter0 = Motion_PVTPoint()  # For Axis 3
    pvtparameter1 = Motion_PVTPoint()  # For Axis 6

    # Define point 0: (0, 0, 0, 0, 0, 0)
    pvtparameter0.pos = 0
    pvtparameter0.velocity = 0
    pvtparameter0.timeMilliseconds = 0
    pvtparameter1.pos = 0
    pvtparameter1.velocity = 0
    pvtparameter1.timeMilliseconds = 0
    pvti.SetPoints(0, 0, pvtparameter0)
    pvti.SetPoints(1, 0, pvtparameter1)
    
    # Define point 1: (10, 100, 100, 20, 200, 100)
    pvtparameter0.pos = 10
    pvtparameter0.velocity = 100
    pvtparameter0.timeMilliseconds = 100
    pvtparameter1.pos = 20
    pvtparameter1.velocity = 200
    pvtparameter1.timeMilliseconds = 100
    pvti.SetPoints(0, 1, pvtparameter0)
    pvti.SetPoints(1, 1, pvtparameter1)
    
    # Define point 2: (20, 200, 200, 60, 400, 200)
    pvtparameter0.pos = 20
    pvtparameter0.velocity = 200
    pvtparameter0.timeMilliseconds = 200
    pvtparameter1.pos = 60
    pvtparameter1.velocity = 400
    pvtparameter1.timeMilliseconds = 200
    pvti.SetPoints(0, 2, pvtparameter0)
    pvti.SetPoints(1, 2, pvtparameter1)
    
    # Define point 3: (30, 100, 300, 100, 200, 300)
    pvtparameter0.pos = 30
    pvtparameter0.velocity = 100
    pvtparameter0.timeMilliseconds = 300
    pvtparameter1.pos = 100
    pvtparameter1.velocity = 200
    pvtparameter1.timeMilliseconds = 300
    pvti.SetPoints(0, 3, pvtparameter0)
    pvti.SetPoints(1, 3, pvtparameter1)
    
    # Define point 4: (60, 0, 400, 80, 0, 400)
    pvtparameter0.pos = 60
    pvtparameter0.velocity = 0
    pvtparameter0.timeMilliseconds = 400
    pvtparameter1.pos = 80
    pvtparameter1.velocity = 0
    pvtparameter1.timeMilliseconds = 400
    pvti.SetPoints(0, 4, pvtparameter0)
    pvti.SetPoints(1, 4, pvtparameter1)
    
    # Start the PVT Interpolation command.
    ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
    if ret != 0:
        print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for both Axis 3 and Axis 6 to finish moving.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 3)
    axisSel.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
