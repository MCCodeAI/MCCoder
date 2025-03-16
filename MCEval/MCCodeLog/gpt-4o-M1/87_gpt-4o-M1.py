
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Set the pitch error compensation table for Axis 4 with the specified data points.
Wmx3Lib_comp = Compensation(Wmx3Lib)
piterror = PitchErrorCompensationData()
# 1: Enable pitch error compensation  0: Disable pitch error compensation
piterror.enable = 1
# The distance between pitch points, in user units.
piterror.pitchInterval = 10
# The number of pitch points
piterror.pitchCount = 11
# The index of the pitch origin.
piterror.pitchOriginIndex = 0
# The command position at the pitch origin, in user units.
piterror.pitchOriginPosition = 0

# Add a pitch error compensation table.
piterror.SetPitchCompensationValue(0, 2)
piterror.SetPitchCompensationValue(1, 4)
piterror.SetPitchCompensationValue(2, 6)
piterror.SetPitchCompensationValue(3, 8)
piterror.SetPitchCompensationValue(4, 10)
piterror.SetPitchCompensationValue(5, 12)
piterror.SetPitchCompensationValue(6, 14)
piterror.SetPitchCompensationValue(7, 16)
piterror.SetPitchCompensationValue(8, 18)
piterror.SetPitchCompensationValue(9, 20)
piterror.SetPitchCompensationValue(10, -10)

# Set the pitch compensation function for Axis 4.
ret = Wmx3Lib_comp.SetPitchErrorCompensation(4, piterror)
if ret != 0:
    print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    return

# Create a command value of target as 110.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 110
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
