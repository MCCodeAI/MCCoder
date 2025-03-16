
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# <log ---------------------------------------------------------------------------

# Stop log just in case logging is on.
ret = WMX3Log.StopLog(0)
sleep(0.01)

# Log the command position after applying compensation offsets. This is necessary to compare if compensation works as expected.
cmLogIn_0.axisOptions.compCommandPos = 1

ret = WMX3Log.SetCustomLog(0, cmLogIn_0)
if ret != 0:
    print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
sleep(0.1)

# Start log
ret = WMX3Log.StartLog(0)
if ret != 0:
    print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
sleep(0.01)
# log> ---------------------------------------------------------------------------

# Set the pitch error compensation table for Axis 4 with the following data points: (0, 2), (10, 4), (20, 6), (30, 8), (40, 10), (50, 12), (60, 14), (70, 16), (80, 18), (90, 20), (100, -10).
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
