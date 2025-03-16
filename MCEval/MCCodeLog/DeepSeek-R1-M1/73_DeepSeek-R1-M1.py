
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = [0.6]

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplLookaheadCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# Create the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2400)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()

conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 2400
conf.compositeAcc = 2000  # Acceleration can be adjusted as needed
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look ahead commands
path.numPoints = 3

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0
point.setOutputBit.bitAddress = 6
point.setOutputBit.value = 1
point.setOutputBit.triggerValue = 50
point.setOutputBit.type = AdvMotion_PathIntplOutputType.CompletedDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(0, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0
point.setOutputBit.bitAddress = 6
point.setOutputBit.value = 0
point.setOutputBit.triggerValue = 30
point.setOutputBit.type = AdvMotion_PathIntplOutputType.RemainingDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(1, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 100)
point.linear.SetTarget(1, 200)
path.SetPoint(2, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start path interpolation with look ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look ahead to complete
Wmx3Lib_cm.motion.Wait(3)
timeoutCounter = 0
# Wait until the path interpolation with look ahead is in Stopped state
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if (pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped):
        break
    sleep(0.1)
    timeoutCounter = timeoutCounter + 1
    if (timeoutCounter > 500):
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if (timeoutCounter > 500):
    print('PathIntplLookahead Running timeout.!')
    return

# Free the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
