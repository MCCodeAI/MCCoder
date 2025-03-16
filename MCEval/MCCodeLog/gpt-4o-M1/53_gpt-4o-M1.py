
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

pvti = Motion_PVTIntplCommand()

pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 6)
pvti.SetPointCount(0, 5)
pvti.SetPointCount(1, 5)

# Define point data for Axis 3 and Axis 6
points = [
    (0, 0, 0, 0, 0, 0),
    (10, 100, 100, 20, 200, 100),
    (20, 200, 200, 60, 400, 200),
    (30, 100, 300, 100, 200, 300),
    (60, 0, 400, 80, 0, 400)
]

for i, (pos0, vel0, time0, pos1, vel1, time1) in enumerate(points):
    pvtparameter0.pos = pos0
    pvtparameter0.velocity = vel0
    pvtparameter0.timeMilliseconds = time0
    pvtparameter1.pos = pos1
    pvtparameter1.velocity = vel1
    pvtparameter1.timeMilliseconds = time1
    pvti.SetPoints(0, i, pvtparameter0)
    pvti.SetPoints(1, i, pvtparameter1)

# Start PVT interpolation
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 3 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
