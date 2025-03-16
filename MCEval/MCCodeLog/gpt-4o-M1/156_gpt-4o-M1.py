
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Define motion command classes
class Motion_PosCommand:
    def __init__(self):
        self.profile = Profile()
        self.axis = None
        self.target = None

class Profile:
    def __init__(self):
        self.type = None
        self.velocity = None
        self.acc = None
        self.dec = None

class Motion_TriggerPosCommand(Motion_PosCommand):
    def __init__(self):
        super().__init__()
        self.trigger = Trigger()

class Trigger:
    def __init__(self):
        self.triggerType = None
        self.triggerAxis = None
        self.triggerValue = None

# Define constants
class ProfileType:
    Trapezoidal = "Trapezoidal"

class TriggerType:
    DistanceToTarget = "DistanceToTarget"

# Mock motion control library
class Wmx3Lib_cm:
    class motion:
        @staticmethod
        def StartPos(command):
            print(f"Starting position command on axis {command.axis} to target {command.target} with velocity {command.profile.velocity}")
            return 0

        @staticmethod
        def StartPos_Trigger(command):
            print(f"Starting triggered position command on axis {command.axis} to target {command.target} with velocity {command.profile.velocity}")
            return 0

        @staticmethod
        def Wait(axis):
            print(f"Waiting for axis {axis} to stop.")
            return 0

# Start an absolute position command for Axis 10
posCommand = Motion_PosCommand()
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = -800

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret))
Wmx3Lib_cm.motion.Wait(10)

# Trigger Axis 10 to move to 300 when the distance to target is 200
trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 200

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret))
Wmx3Lib_cm.motion.Wait(10)

# Set an event to trigger Axis 12 to move to -50 when Axis 10 reaches position 100
trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 12
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 500
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = -50
trigPosCommand.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 100

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret))
Wmx3Lib_cm.motion.Wait(12)
