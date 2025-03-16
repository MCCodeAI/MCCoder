
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

pvti = Motion_PVTIntplCommand()
pvtparameter3 = Motion_PVTPoint()
pvtparameter6 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 6)
pvti.SetPointCount(0, 5)
pvti.SetPointCount(1, 5)

# Define point data
points = [
    (0, 0, 0, 0, 0, 0),
    (10, 100, 100, 20, 200, 100),
    (20, 200, 200, 60, 400, 200),
    (30, 100, 300, 100, 200, 300),
    (60, 0, 400, 80, 0, 400)
]

for i, (pos3, vel3, time3, pos6, vel6, time6) in enumerate(points):
    pvtparameter3.pos = pos3
    pvtparameter3.velocity = vel3
    pvtparameter3.timeMilliseconds = time3
    pvtparameter6.pos = pos6
    pvtparameter6.velocity = vel6
    pvtparameter6.timeMilliseconds = time6
    pvti.SetPoints(0, i, pvtparameter3)
    pvti.SetPoints(1, i, pvtparameter6)

ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
