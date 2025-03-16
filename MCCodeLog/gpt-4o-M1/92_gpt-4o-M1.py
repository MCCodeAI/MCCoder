
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Define the axis number
axis = 10

# Set the In Pos Width parameter for Axis 10
feedbackParam = Config_FeedbackParam()
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
feedbackParam.inPosWidth = 0.234
ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)

if ret != 0:
    print('Set inPosWidth error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Verify if the In Pos Width is set correctly
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    if feedbackParam.inPosWidth == 0.234:
        # Move Axis 10 to position 234
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = axis
        posCommand.target = 234
        posCommand.profile.velocity = 1000  # Example velocity
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        else:
            # Wait until the axis moves to the target position and stops
            Wmx3Lib_cm.motion.Wait(axis)
    else:
        # Move Axis 10 to position -234
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = axis
        posCommand.target = -234
        posCommand.profile.velocity = 1000  # Example velocity
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        else:
            # Wait until the axis moves to the target position and stops
            Wmx3Lib_cm.motion.Wait(axis)
