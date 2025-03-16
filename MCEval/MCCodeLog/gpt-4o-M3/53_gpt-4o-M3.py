
# Axes = [3, 6]
# Inputs = []
# Outputs = []

class Motion_PVTIntplCommand:
    def __init__(self):
        self.axisCount = 0
        self.axes = []
        self.pointCounts = []
        self.points = {}

    def SetAxis(self, index, axis):
        if index < len(self.axes):
            self.axes[index] = axis
        else:
            self.axes.append(axis)

    def SetPointCount(self, axisIndex, count):
        if axisIndex < len(self.pointCounts):
            self.pointCounts[axisIndex] = count
        else:
            self.pointCounts.append(count)

    def SetPoints(self, axisIndex, pointIndex, point):
        if axisIndex not in self.points:
            self.points[axisIndex] = []
        if pointIndex < len(self.points[axisIndex]):
            self.points[axisIndex][pointIndex] = point
        else:
            self.points[axisIndex].append(point)

class Motion_PVTPoint:
    def __init__(self):
        self.pos = 0
        self.velocity = 0
        self.timeMilliseconds = 0

class Wmx3Lib_cm:
    class motion:
        @staticmethod
        def StartPVT_Intpl(pvti):
            # Simulate starting PVT interpolation
            print(f"Starting PVT interpolation for axes: {pvti.axes}")
            return 0  # Simulate success

        @staticmethod
        def Wait(axis):
            # Simulate waiting for axis to stop
            print(f"Waiting for axis {axis} to stop.")
            return 0  # Simulate success

class AxisSelection:
    def __init__(self):
        self.axisCount = 0
        self.axes = []

    def SetAxis(self, index, axis):
        if index < len(self.axes):
            self.axes[index] = axis
        else:
            self.axes.append(axis)

# Create PVT interpolation command
pvti = Motion_PVTIntplCommand()

# Define PVT points for Axis 3 and Axis 6
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

for i, (pos0, vel0, time0, pos1, vel1, time1) in enumerate(points):
    pvtparameter0 = Motion_PVTPoint()
    pvtparameter1 = Motion_PVTPoint()
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
    print('StartPVT_Intpl error code is ' + str(ret))
else:
    # Wait for the motion to complete
    ret = Wmx3Lib_cm.motion.Wait(3)
    if ret != 0:
        print('Wait error code is ' + str(ret))
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret))
