
# Axes = [5, 6, 3]
# Inputs = []
# Outputs = []

class AdvancedMotion:
    def __init__(self, lib):
        self.lib = lib

class AdvMotion_PathIntplWithRotationCommand:
    def __init__(self):
        self.numPoints = 0

    def SetPoint(self, index, point):
        pass

class AdvMotion_PathIntplWithRotationCommandPoint:
    def __init__(self):
        self.type = None
        self.profile = Profile()
        self.useLocalCenterOfRotation = 0
        self.localCenterOfRotationDirection = 0

    def SetTarget(self, axis, value):
        pass

    def SetLocalCenterOfRotation(self, axis, value):
        pass

class Profile:
    def __init__(self):
        self.type = None
        self.velocity = 0
        self.acc = 0
        self.dec = 0

class ProfileType:
    Trapezoidal = 0

class AdvMotion_PathIntplWithRotationConfiguration:
    def __init__(self):
        self.rotationalAxis = 0
        self.angleCorrectionProfile = Profile()
        self.disableXYRotationalMotion = 0

    def SetAxis(self, axis, value):
        pass

    def SetCenterOfRotation(self, axis, value):
        pass

class AdvMotion_PathIntplWithRotationState:
    Idle = 0

def execute_path_interpolation():
    Wmx3Lib_adv = AdvancedMotion(None)

    path = AdvMotion_PathIntplWithRotationCommand()

    conf = AdvMotion_PathIntplWithRotationConfiguration()
    conf.SetAxis(0, 5)  # Axis 5
    conf.SetAxis(1, 6)  # Axis 6
    conf.rotationalAxis = 3  # Rotational axis
    conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
    conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position
    conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
    conf.angleCorrectionProfile.velocity = 1000
    conf.angleCorrectionProfile.acc = 2000
    conf.angleCorrectionProfile.dec = 2000
    conf.disableXYRotationalMotion = 1

    path.numPoints = 4

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)
    point.SetTarget(1, 0)
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)
    point.SetTarget(1, 160)
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)
    point.SetTarget(1, 160)
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)
    point.SetTarget(1, 0)
    path.SetPoint(3, point)

    timeoutCounter = 0
    pathStatus = AdvMotion_PathIntplWithRotationState()
    while True:
        if pathStatus == AdvMotion_PathIntplWithRotationState.Idle:
            break
        sleep(0.1)
        timeoutCounter += 1
        if timeoutCounter > 500:
            break
    if timeoutCounter > 500:
        print('PathIntplWithRotation Running timeout.!')
        return

execute_path_interpolation()
