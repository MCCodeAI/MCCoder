
# Axes = [2, 4]
# Inputs = []
# Outputs = []

# Define the motion command for absolute linear interpolation
class Motion_LinearIntplCommand:
    def __init__(self):
        self.axisCount = 0
        self.profile = Profile()
        self.targets = {}

    def SetAxis(self, index, axis):
        pass

    def SetTarget(self, axis, position):
        self.targets[axis] = position

class Profile:
    def __init__(self):
        self.type = None
        self.velocity = 0
        self.acc = 0
        self.jerkAcc = 0

class ProfileType:
    JerkLimited = 0

class AxisSelection:
    def __init__(self):
        self.axisCount = 0

    def SetAxis(self, index, axis):
        pass

# Create a linear interpolation command
lin = Motion_LinearIntplCommand()

# Set the number of axes involved
lin.axisCount = 2

# Assign axes 2 and 4
lin.SetAxis(0, 2)
lin.SetAxis(1, 4)

# Define the motion profile
lin.profile.type = ProfileType.JerkLimited
lin.profile.velocity = 800
lin.profile.acc = 8000
lin.profile.jerkAcc = 20000

# Set target positions for axes
lin.SetTarget(2, -100)
lin.SetTarget(4, -50)

# Start the linear interpolation motion
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
