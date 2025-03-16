
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Create a command value for a relative position move on Axis 6.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the relative motion command.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle the error as required.
else:
    # Wait until Axis 6 comes to a stop after completing the motion.
    Wmx3Lib_cm.motion.Wait(6)
