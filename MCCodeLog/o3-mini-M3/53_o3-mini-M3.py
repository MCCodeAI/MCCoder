
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Create a PVT interpolation command for Axis 3 and Axis 6 with 5 points.
# Each point is provided in the format:
# (Position for Axis 3, Velocity for Axis 3, Time for Axis 3, Position for Axis 6, Velocity for Axis 6, Time for Axis 6)
#
# Point definitions:
#   Point 0: (0, 0, 0) and (0, 0, 0)
#   Point 1: (10, 100, 100) and (20, 200, 100)
#   Point 2: (20, 200, 200) and (60, 400, 200)
#   Point 3: (30, 100, 300) and (100, 200, 300)
#   Point 4: (60, 0, 400) and (80, 0, 400)

# Create a PVT interpolation command object (assumed to be provided by the motion control library)
pvti = Motion_PVTIntplCommand()

# Two separate PVT point structures for Axis 3 and Axis 6
pvtparameter_axis3 = Motion_PVTPoint()
pvtparameter_axis6 = Motion_PVTPoint()

# Set up the command for two axes: Axis 3 and Axis 6
pvti.axisCount = 2
pvti.SetAxis(0, 3)  # Map index 0 to Axis 3
pvti.SetAxis(1, 6)  # Map index 1 to Axis 6

# Specify that there will be 5 points for each axis
pvti.SetPointCount(0, 5)  # For Axis 3
pvti.SetPointCount(1, 5)  # For Axis 6

# -- Define each PVT point --
# Point 0
pvtparameter_axis3.pos = 0
pvtparameter_axis3.velocity = 0
pvtparameter_axis3.timeMilliseconds = 0
pvtparameter_axis6.pos = 0
pvtparameter_axis6.velocity = 0
pvtparameter_axis6.timeMilliseconds = 0
pvti.SetPoints(0, 0, pvtparameter_axis3)
pvti.SetPoints(1, 0, pvtparameter_axis6)

# Point 1
pvtparameter_axis3.pos = 10
pvtparameter_axis3.velocity = 100
pvtparameter_axis3.timeMilliseconds = 100
pvtparameter_axis6.pos = 20
pvtparameter_axis6.velocity = 200
pvtparameter_axis6.timeMilliseconds = 100
pvti.SetPoints(0, 1, pvtparameter_axis3)
pvti.SetPoints(1, 1, pvtparameter_axis6)

# Point 2
pvtparameter_axis3.pos = 20
pvtparameter_axis3.velocity = 200
pvtparameter_axis3.timeMilliseconds = 200
pvtparameter_axis6.pos = 60
pvtparameter_axis6.velocity = 400
pvtparameter_axis6.timeMilliseconds = 200
pvti.SetPoints(0, 2, pvtparameter_axis3)
pvti.SetPoints(1, 2, pvtparameter_axis6)

# Point 3
pvtparameter_axis3.pos = 30
pvtparameter_axis3.velocity = 100
pvtparameter_axis3.timeMilliseconds = 300
pvtparameter_axis6.pos = 100
pvtparameter_axis6.velocity = 200
pvtparameter_axis6.timeMilliseconds = 300
pvti.SetPoints(0, 3, pvtparameter_axis3)
pvti.SetPoints(1, 3, pvtparameter_axis6)

# Point 4
pvtparameter_axis3.pos = 60
pvtparameter_axis3.velocity = 0
pvtparameter_axis3.timeMilliseconds = 400
pvtparameter_axis6.pos = 80
pvtparameter_axis6.velocity = 0
pvtparameter_axis6.timeMilliseconds = 400
pvti.SetPoints(0, 4, pvtparameter_axis3)
pvti.SetPoints(1, 4, pvtparameter_axis6)

# Send the PVT interpolation command to start the motion.
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until motion is complete for both Axis 3 and Axis 6.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 3)
    axisSel.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
        print('PVT interpolation motion on Axis 3 and Axis 6 completed successfully.')
