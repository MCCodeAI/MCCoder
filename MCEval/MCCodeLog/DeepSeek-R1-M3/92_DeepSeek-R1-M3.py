
# Axes = [10]
# IOInputs = []
# IOOutputs = []

def set_in_pos_width(axis, width):
    # Read current feedback parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    if ret != 0:
        print('GetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return ret
    
    # Set In Pos Width
    feedbackParam.inPosWidth = width
    
    # Write updated parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if ret != 0:
        print('SetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return ret
    
    return 0

def main():
    axis = 10
    target_width = 0.234
    target_pos = 234 if target_width == 0.234 else -234

    # Set In Pos Width
    ret = set_in_pos_width(axis, target_width)
    if ret != 0:
        return

    # Verify In Pos Width
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    if ret != 0:
        print('GetFeedbackParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    if feedbackParam.inPosWidth != target_width:
        print(f'In Pos Width not set correctly. Expected: {target_width}, Actual: {feedbackParam.inPosWidth}')
        target_pos = -234

    # Create motion command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = target_pos
    posCommand.profile.velocity = 1000  # Default velocity
    posCommand.profile.acc = 10000      # Default acceleration
    posCommand.profile.dec = 10000      # Default deceleration

    # Execute motion
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion to complete
    Wmx3Lib_cm.motion.Wait(axis)

if __name__ == "__main__":
    main()
