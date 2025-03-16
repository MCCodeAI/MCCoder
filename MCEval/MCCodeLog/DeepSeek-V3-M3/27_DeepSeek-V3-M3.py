
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplLookaheadCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1500)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()

conf.axisCount = 2
conf.SetAxis(0, 7)
conf.SetAxis(1, 8)
conf.compositeVel = 1500
conf.compositeAcc = 4000
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look ahead commands
path.numPoints = 10

# Define the pentastar points
pentastar_points = [
    (0.00, 0.00),
    (22.45, -69.10),
    (95.11, -69.10),
    (36.33, -111.80),
    (58.78, -180.90),
    (0.00, -138.20),
    (-58.78, -180.90),
    (-36.33, -111.80),
    (-95.11, -69.10),
    (-22.45, -69.10)
]

for i in range(0, 10):
    Point = AdvMotion_PathIntplLookaheadCommandPoint()
    Point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    Point.linear.axisCount = 2
    Point.linear.SetAxis(0, 7)
    Point.linear.SetAxis(1, 8)
    Point.linear.SetTarget(0, pentastar_points[i][0])
    Point.linear.SetTarget(1, pentastar_points[i][1])
    path.SetPoint(i, Point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with look ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look ahead to complete
Wmx3Lib_cm.motion.Wait(7)
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

# Free the path interpolation with look ahead buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
