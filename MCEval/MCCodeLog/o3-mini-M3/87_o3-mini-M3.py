
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Set the pitch error compensation table for Axis 4 with the following data points:
# (0,2), (10,4), (20,6), (30,8), (40,10), (50,12), (60,14), (70,16), (80,18), (90,20), (100,-10)
# Then, move it from 0 to 110 at a speed of 2000.

# Create the pitch error compensation data for Axis 4.
Wmx3Lib_comp = Compensation(Wmx3Lib)
piterror = PitchErrorCompensationData()

# Enable pitch error compensation.
piterror.enable = 1
# The distance between pitch points is 10 (user units) based on the provided points.
piterror.pitchInterval = 10
# The number of pitch points is 11.
piterror.pitchCount = 11
# The index of the pitch origin.
piterror.pitchOriginIndex = 0
# The command position at the pitch origin.
piterror.pitchOriginPosition = 0

# Set the pitch compensation values for each point.
piterror.SetPitchCompensationValue(0, 2)    # At position 0
piterror.SetPitchCompensationValue(1, 4)    # At position 10
piterror.SetPitchCompensationValue(2, 6)    # At position 20
piterror.SetPitchCompensationValue(3, 8)    # At position 30
piterror.SetPitchCompensationValue(4, 10)   # At position 40
piterror.SetPitchCompensationValue(5, 12)   # At position 50
piterror.SetPitchCompensationValue(6, 14)   # At position 60
piterror.SetPitchCompensationValue(7, 16)   # At position 70
piterror.SetPitchCompensationValue(8, 18)   # At position 80
piterror.SetPitchCompensationValue(9, 20)   # At position 90
piterror.SetPitchCompensationValue(10, -10) # At position 100

# Apply the pitch error compensation to Axis 4.
ret = Wmx3Lib_comp.SetPitchErrorCompensation(4, piterror)
if ret != 0:
    print('SetPitchErrorCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    # Exit if an error occurs.
    quit()

# Create a position command to move Axis 4 from its current position 0 to 110.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 110
posCommand.profile.velocity = 2000
# Set acceleration and deceleration as per system requirements.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the motion command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    quit()

# Wait until Axis 4 stops moving.
Wmx3Lib_cm.motion.Wait(4)
