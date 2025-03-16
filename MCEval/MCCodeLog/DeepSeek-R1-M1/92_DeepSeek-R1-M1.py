
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Set In Pos Width parameter for Axis 10
axis = 10

# Read current feedback parameters
feedbackParam = Config_FeedbackParam()
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
if ret != 0:
    print('GetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set In Pos Width to 0.234
feedbackParam.inPosWidth = 0.234

# Write updated parameters
ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
if ret != 0:
    print('Set inPosWidth error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify In Pos Width value
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
if ret != 0:
    print('GetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if feedbackParam.inPosWidth == 0.234:
    # Move Axis 10 to 234
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = 234
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion to complete
    Wmx3Lib_cm.motion.Wait(10)
else:
    # Move Axis 10 to -234
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = -234
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion to complete
    Wmx3Lib_cm.motion.Wait(10)
