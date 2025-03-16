
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Create a command for an absolute move of Axis 1 to position 130.2
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 130.2
posCommand.profile.velocity = 1060
posCommand.profile.acc = 11000
posCommand.profile.dec = 11000

# Execute the absolute move command for Axis 1
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    raise Exception("Motion command failed.")

# Wait until Axis 1 stops moving before proceeding
Wmx3Lib_cm.motion.Wait(1)
