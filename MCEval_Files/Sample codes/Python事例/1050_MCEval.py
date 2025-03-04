#Set the feedback parameters for Axis 0. Set‘In Pos Width’to 1000,‘In Pos Width2’to 1000,‘In Pos Width3’to 1000,‘In Pos Width4’to 1000,‘In Pos Width5’to 1000,‘Velocity Monitor Source’to UseVelocityFeedback,‘Pos Set Width’to 1000,‘Delayed Pos Set Width’to 1000,‘Delayed Pos Set Milliseconds’to 0.
    # Axes = [0]

    # Example of Axis 0 Feedback Parameters
    axis = 0

    #In Pos Width      The width of a window centered at the target position of the current motion command. When the feedback position falls within this window, the axis is considered to be in position.
    #Variable Name:   inPosWidth
    #Type:            double
    #Unit:            user unit
    #Minimum Value:   0
    #Maximum Value:   274877906943
    #Default Value:   1000
    #Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.inPosWidth = 1000
    #Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if(ret!=0):
        print('Set inPosWidth error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #In Pos Width2    This parameter is the same as the In Pos Width parameter, except it affects the In Pos 2 status instead of the In Pos status.
    #Variable Name:   inPosWidth2
    #Type:            double
    #Unit:            user unit
    #Minimum Value:   0
    #Maximum Value:   274877906943
    #Default Value:   1000
    #Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.inPosWidth2 = 1000
    #Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if(ret!=0):
        print('Set inPosWidth2 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # In Pos Width3    This parameter is the same as the In Pos Width parameter, except it affects the In Pos 3 status instead of the In Pos status.
    # Variable Name:   inPosWidth3
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   1000
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.inPosWidth3 = 1000
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set inPosWidth3 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # In Pos Width4    This parameter is the same as the In Pos Width parameter, except it affects the In Pos 4 status instead of the In Pos status.
    # Variable Name:   inPosWidth4
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   1000
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.inPosWidth4 = 1000
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set inPosWidth4 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # In Pos Width5    This parameter is the same as the In Pos Width parameter, except it affects the In Pos 5 status instead of the In Pos status.
    # Variable Name:   inPosWidth5
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   1000
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.inPosWidth5 = 1000
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set inPosWidth5 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Monitor Source    This parameter determines whether the Actual Velocity status is calculated from the position feedback, or is obtained directly from the servo velocity feedback.
    # Variable Name:   velocityMonitorSource
    # Type:            VelocityMonitorSource
    # Default Value:   UseVelocityFeedback
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.velocityMonitorSource = Config_VelocityMonitorSource.UseVelocityFeedback
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set velocityMonitorSource error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Pos Set Width    The width of a window centered at the target position of the current motion command. When the feedback position falls within this window and the cyclic command position is equal to the target position (the command generation has finished), the Pos Set status is set to TRUE.
    # Variable Name:   posSetWidth
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   1000
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.posSetWidth = 1000
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set posSetWidth error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Delayed Pos Set Width     The width of a window centered at the target position of the current motion command. After the cyclic command position becomes equal to the target position (the command generation has finished), when the feedback position falls within this window for Delayed Pos Set Milliseconds amount of time continuously, the Delayed Pos Set status is set to TRUE.
    # Variable Name:   delayedPosSetWidth
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   1000
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.delayedPosSetWidth = 1000
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set delayedPosSetWidth error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Delayed Pos Set Milliseconds     The amount of time that the feedback position must be within the Delayed Pos Set Width of the target position continuously before the Delayed Pos Set status is set to TRUE.
    #                                   If this parameter is set to 0, the Delayed Pos Set status is set to TRUE immediately when the feedback position goes within the Delayed Pos Set Width of the target position after the command generation has finished.
    # Variable Name:   delayedPosSetMilliseconds
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    feedbackParam = Config_FeedbackParam()
    ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
    feedbackParam.delayedPosSetMilliseconds = 0
    # Write the updated values of parameters
    ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
    if (ret != 0):
        print('Set delayedPosSetMilliseconds error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


