
# Axes = [10]
# IOInputs = []
# IOOutputs = []

axis = 10

# Set the In Pos Width of Axis 10 to 0.234.
feedbackParam = Config_FeedbackParam()
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
feedbackParam.inPosWidth = 0.234
ret, feedbackParamErr = Wmx3Lib_cm.config.SetFeedbackParam(axis, feedbackParam)
if ret != 0:
    print('Set In Pos Width error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Unrecoverable error: exit or return as desired.
    exit(1)

# Read back the In Pos Width parameter for verification.
ret, feedbackParam = Wmx3Lib_cm.config.GetFeedbackParam(axis)
if ret != 0:
    print('Get In Pos Width error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Check if the In Pos Width equals 0.234.
if abs(feedbackParam.inPosWidth - 0.234) < 1e-6:
    target_position = 234
else:
    target_position = -234

# Create a motion command to move Axis 10 to the target position.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = target_position
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the absolute move command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 10 has stopped moving.
Wmx3Lib_cm.motion.Wait(0)
