
# Axes = [9, 6]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create the path interpolation with look-ahead command
path = AdvMotion_PathIntplLookaheadCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# Create the path interpolation with look-ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look-ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()

conf.axisCount = 2
conf.SetAxis(0, 9)
conf.SetAxis(1, 6)
conf.compositeVel = 2000
conf.compositeAcc = 4000  # Assuming a default acceleration value
conf.stopOnEmptyBuffer = True
conf.sampleDistance = 50

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look-ahead commands
path.numPoints = 5

# Define the points for interpolation
points = [(200, 0), (200, 200), (0, 200), (0, 0), (200, 200)]

for i, (x, y) in enumerate(points):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 9)
    point.linear.SetAxis(1, 6)
    point.linear.SetTarget(0, x)
    point.linear.SetTarget(1, y)
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with look-ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look-ahead to complete
Wmx3Lib_cm.motion.Wait(9)
timeoutCounter = 0
# Wait until the path interpolation with look-ahead is in Stopped state
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if timeoutCounter > 500:
    print('PathIntplLookahead Running timeout.!')
    return

# Free the path interpolation with look-ahead buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
