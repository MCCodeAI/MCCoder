
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

import math

pvti = Motion_PVTIntplCommand()

axis4_point = Motion_PVTPoint()
axis5_point = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, 20)
pvti.SetPointCount(1, 20)

for i in range(20):
    theta = 2 * math.pi * i / 20
    x = -50 + 50 * math.cos(theta)
    y = 0 + 50 * math.sin(theta)
    time = i * 100

    axis4_point.pos = x
    axis4_point.velocity = 100
    axis4_point.timeMilliseconds = time

    axis5_point.pos = y
    axis5_point.velocity = 100
    axis5_point.timeMilliseconds = time

    pvti.SetPoints(0, i, axis4_point)
    pvti.SetPoints(1, i, axis5_point)

ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
