
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Set the In Pos Width parameter of Axis 10 to 0.234
axis = 10

# Read the current feedback parameters
feedbackParam = Config_FeedbackParam()
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
if ret != 0:
    print('GetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set the In Pos Width to 0.234
feedbackParam.inPosWidth = 0.234

# Write the updated feedback parameters
ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
if ret != 0:
    print('SetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if In Pos Width equals 0.234
if feedbackParam.inPosWidth == 0.234:
    # Move Axis 10 to 234
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 234
    posCommand.profile.velocity = 1000  # Assuming a default velocity
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 10 to -234
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -234
    posCommand.profile.velocity = 1000  # Assuming a default velocity
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
