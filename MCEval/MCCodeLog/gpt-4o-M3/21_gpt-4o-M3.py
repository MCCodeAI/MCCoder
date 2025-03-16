
# Axes = [1, 2]
# Inputs = []
# Outputs = []

class Motion_LinearIntplCommand:
    def __init__(self):
        self.axisCount = 0
        self.axes = []
        self.profile = Profile()
        self.targets = {}

    def SetAxis(self, index, axis):
        if index < len(self.axes):
            self.axes[index] = axis
        else:
            self.axes.append(axis)

    def SetTarget(self, axis, position):
        self.targets[axis] = position

class Profile:
    def __init__(self):
        self.type = None
        self.velocity = 0
        self.acc = 0
        self.dec = 0

class ProfileType:
    Trapezoidal = "Trapezoidal"

class AxisSelection:
    def __init__(self):
        self.axisCount = 0
        self.axes = []

    def SetAxis(self, index, axis):
        if index < len(self.axes):
            self.axes[index] = axis
        else:
            self.axes.append(axis)

class Wmx3Lib_cm:
    class motion:
        @staticmethod
        def StartLinearIntplPos(lin):
            # Simulate starting the motion
            print(f"Starting linear interpolation for axes {lin.axes} to positions {lin.targets} with velocity {lin.profile.velocity}")
            return 0  # Simulate success

        @staticmethod
        def Wait_AxisSel(axisSel):
            # Simulate waiting for motion to complete
            print(f"Waiting for axes {axisSel.axes} to stop moving")
            return 0  # Simulate success

# Create a linear interpolation command
lin = Motion_LinearIntplCommand()

# Set up the axes
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 2)

# Define the motion profile
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000

# Set the target positions
lin.SetTarget(1, 100)
lin.SetTarget(2, 150)

# Start the linear interpolation motion
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret))
    exit()

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret))
    exit()
