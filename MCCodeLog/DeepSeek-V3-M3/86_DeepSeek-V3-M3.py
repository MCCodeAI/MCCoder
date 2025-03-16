
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Set the pitch error compensation table for Axis 4 with the following data points: (0, 12), (100, -12), (200, 16), (300, -16).
Wmx3Lib_comp = Compensation(Wmx3Lib)
piterror = PitchErrorCompensationData()
# 1: Enable pitch error compensation  0: Disable pitch error compensation
piterror.enable = 1
# The distance between pitch points, in user units.
piterror.pitchInterval = 100
# The number of pitch points
piterror.pitchCount = 4
# The index of the pitch origin.
piterror.pitchOriginIndex = 0
# The command position at the pitch origin, in user units.
piterror.pitchOriginPosition = 0
# Add a pitch error compensation table.
piterror.SetPitchCompensationValue(0, 12)
piterror.SetPitchCompensationValue(1, -12)
piterror.SetPitchCompensationValue(2, 16)
piterror.SetPitchCompensationValue(3, -16)

# Set the pitch compensation function for Axis 4.
ret = Wmx3Lib_comp.SetPitchErrorCompensation(4, piterror)
if ret != 0:
    print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    return

# Create a command value of target as 300.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
