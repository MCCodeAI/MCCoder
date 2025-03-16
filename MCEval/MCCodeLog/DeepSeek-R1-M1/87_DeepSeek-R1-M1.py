
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Stop log just in case logging is on.
ret = WMX3Log.StopLog(0)
sleep(0.01)

# Log the command position after applying compensation offsets.
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

# Set the pitch error compensation table for Axis 4
Wmx3Lib_comp = Compensation(Wmx3Lib)
piterror = PitchErrorCompensationData()
piterror.enable = 1
piterror.pitchInterval = 10
piterror.pitchCount = 11
piterror.pitchOriginIndex = 0
piterror.pitchOriginPosition = 0

# Add pitch compensation values
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

ret = Wmx3Lib_comp.SetPitchErrorCompensation(4, piterror)
if ret != 0:
    print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    return

# Move Axis 4 from 0 to 110 at speed 2000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 110
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops
Wmx3Lib_cm.motion.Wait(4)
