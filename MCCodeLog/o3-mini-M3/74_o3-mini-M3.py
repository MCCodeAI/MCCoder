
import time  # Use time.sleep to avoid shadowing issues

# ... (other initialization code remains unchanged)

# Free and then create the path interpolation with look-ahead buffer on channel 0
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Configure the look-ahead channel for 4 axes (3 primary axes + 1 auxiliary)
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 4
conf.SetAxis(0, 4)
conf.SetAxis(1, 6)
conf.SetAxis(2, 8)
conf.SetAxis(3, 9)  # Auxiliary axis
conf.compositeVel = 1000
conf.compositeAcc = 4000
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Create the look-ahead path command and define its segments
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 2

# First segment: Circular interpolation defined by a through point.
point1 = AdvMotion_PathIntplLookaheadCommandPoint()
point1.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEnd3DCircular
point1.throughAndEnd3DCircular.axisCount = 3
point1.throughAndEnd3DCircular.SetAxis(0, 4)
point1.throughAndEnd3DCircular.SetAxis(1, 6)
point1.throughAndEnd3DCircular.SetAxis(2, 8)
point1.throughAndEnd3DCircular.SetThroughPos(0, 80)
point1.throughAndEnd3DCircular.SetThroughPos(1, 30)
point1.throughAndEnd3DCircular.SetThroughPos(2, 10)
point1.throughAndEnd3DCircular.SetEndPos(0, 100)
point1.throughAndEnd3DCircular.SetEndPos(1, 100)
point1.throughAndEnd3DCircular.SetEndPos(2, 0)
point1.throughAndEnd3DCircular.auxiliaryAxisCount = 1
point1.throughAndEnd3DCircular.SetAuxiliaryAxis(0, 9)
point1.throughAndEnd3DCircular.SetAuxiliaryTarget(0, 50)
path.SetPoint(0, point1)

# Second segment: Circular interpolation defined by a center point.
point2 = AdvMotion_PathIntplLookaheadCommandPoint()
point2.type = AdvMotion_PathIntplLookaheadSegmentType.CenterAndEnd3DCircular
point2.centerAndEnd3DCircular.axisCount = 3
point2.centerAndEnd3DCircular.SetAxis(0, 4)
point2.centerAndEnd3DCircular.SetAxis(1, 6)
point2.centerAndEnd3DCircular.SetAxis(2, 8)
point2.centerAndEnd3DCircular.SetCenterPos(0, 30)
point2.centerAndEnd3DCircular.SetCenterPos(1, 80)
point2.centerAndEnd3DCircular.SetCenterPos(2, 10)
point2.centerAndEnd3DCircular.SetEndPos(0, 0)
point2.centerAndEnd3DCircular.SetEndPos(1, 0)
point2.centerAndEnd3DCircular.SetEndPos(2, 0)
point2.centerAndEnd3DCircular.auxiliaryAxisCount = 1
point2.centerAndEnd3DCircular.SetAuxiliaryAxis(0, 9)
point2.centerAndEnd3DCircular.SetAuxiliaryTarget(0, -50)
path.SetPoint(1, point2)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Wait for the path interpolation to complete.
Wmx3Lib_cm.motion.Wait(4)  # Initiate wait for the motion on an example primary axis (Axis 4)
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
    time.sleep(0.1)  # Use time.sleep to ensure correct pause duration
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if timeoutCounter > 500:
    print('PathIntplLookahead Running timeout.!')
    exit(1)

ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)
