
# Axes = [10]
# IOInputs = []
# IOOutputs = []

def main():
    axis = 10

    # ----------------------------------------------------------------
    # Set the In Pos Width parameter of Axis 10 to 0.234
    # ----------------------------------------------------------------
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    if ret != 0:
        print("Error getting feedback parameters. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    feedbackParam.inPosWidth = 0.234
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if ret != 0:
        print("Error setting inPosWidth. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Read back the parameter to verify
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    if ret != 0:
        print("Error re-reading feedback parameters. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # ----------------------------------------------------------------
    # Check if In Pos Width equals 0.234; then move Axis 10 accordingly
    # If equality is true, move to 234, otherwise move to -234.
    # ----------------------------------------------------------------
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.velocity = 1000  # Setting velocity value for the motion command

    if feedbackParam.inPosWidth == 0.234:
        posCommand.target = 234
    else:
        posCommand.target = -234

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 10 stops moving before finishing the command
    Wmx3Lib_cm.motion.Wait(0)

if __name__ == "__main__":
    main()
