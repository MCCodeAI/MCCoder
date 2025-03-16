
# Axes = [4, 6, 8, 9]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create the path interpolation with look-ahead command
path = AdvMotion_PathIntplLookaheadCommand()

# Free any existing path interpolation with look-ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create a new path interpolation with look-ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look-ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 4
conf.SetAxis(0, 4)
conf.SetAxis(1, 6)
conf.SetAxis(2, 8)
conf.SetAxis(3, 9)
conf.compositeVel = 1000
conf.compositeAcc = 4000
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look-ahead commands
path.numPoints = 2

# First circular interpolation
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEnd3DCircular
point.throughAndEnd3DCircular.axisCount = 3
point.throughAndEnd3DCircular.SetAxis(0, 4)
point.throughAndEnd3DCircular.SetAxis(1, 6)
point.throughAndEnd3DCircular.SetAxis(2, 8)
point.throughAndEnd3DCircular.SetThroughPos(0, 80)
point.throughAndEnd3DCircular.SetThroughPos(1, 30)
point.throughAndEnd3DCircular.SetThroughPos(2, 10)
point.throughAndEnd3DCircular.SetEndPos(0, 100)
point.throughAndEnd3DCircular.SetEndPos(1, 100)
point.throughAndEnd3DCircular.SetEndPos(2, 0)
point.throughAndEnd3DCircular.auxiliaryAxisCount = 1
point.throughAndEnd3DCircular.SetAuxiliaryAxis(0, 9)
point.throughAndEnd3DCircular.SetAuxiliaryTarget(0, 50)
path.SetPoint(0, point)

# Second circular interpolation
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.CenterAndEndCircular
point.centerAndEndCircular.axisCount = 3
point.centerAndEndCircular.SetAxis(0, 4)
point.centerAndEndCircular.SetAxis(1, 6)
point.centerAndEndCircular.SetAxis(2, 8)
point.centerAndEndCircular.SetCenterPos(0, 30)
point.centerAndEndCircular.SetCenterPos(1, 80)
point.centerAndEndCircular.SetCenterPos(2, 10)
point.centerAndEndCircular.SetEndPos(0, 0)
point.centerAndEndCircular.SetEndPos(1, 0)
point.centerAndEndCircular.SetEndPos(2, 0)
point.centerAndEndCircular.auxiliaryAxisCount = 1
point.centerAndEndCircular.SetAuxiliaryTarget(0, -50)  # Corrected line
path.SetPoint(1, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start path interpolation with look-ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look-ahead to complete
Wmx3Lib_cm.motion.Wait(4)
timeoutCounter = 0
# Wait until the path interpolation with look-ahead is in Stopped state
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if (pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped):
        break
    sleep(0.1)
    timeoutCounter = timeoutCounter + 1
    if (timeoutCounter > 500):
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if (timeoutCounter > 500):
    print('PathIntplLookahead Running timeout.!')
    return

# Free the path interpolation with look-ahead buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
