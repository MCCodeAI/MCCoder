
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
    exit()
sleep(0.1)

# Start log
ret = WMX3Log.StartLog(0)
if ret != 0:
    print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    exit()
sleep(0.01)

# Set the pitch error compensation table for Axis 4 with the following data points: 
# (0, 12), (100, -12), (200, 16), (300, -16)
Wmx3Lib_comp = Compensation(Wmx3Lib)
piterror = PitchErrorCompensationData()
piterror.enable = 1
piterror.pitchInterval = 100
piterror.pitchCount = 4
piterror.pitchOriginIndex = 0
piterror.pitchOriginPosition = 0

piterror.SetPitchCompensationValue(0, 12)
piterror.SetPitchCompensationValue(1, -12)
piterror.SetPitchCompensationValue(2, 16)
piterror.SetPitchCompensationValue(3, -16)

ret = Wmx3Lib_comp.SetPitchErrorCompensation(4, piterror)
if ret != 0:
    print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + WMX3Lib_comp.ErrorToString(ret))
    exit()

# Create a command value to move Axis 4 from 0 to the absolute position 300 at a speed of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the motion command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 4 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
