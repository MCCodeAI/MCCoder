
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation lookahead buffer for channel 10
Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)

# Allocate buffer memory for a path interpolation with lookahead channel with 1,000 points for Channel 10.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the configuration for the path interpolation with lookahead channel, specifying Axis 0 and Axis 1, with composite velocity of 1,500.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 0)
conf.SetAxis(1, 1)
conf.compositeVel = 1500
conf.compositeAcc = 20000
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add interpolation commands to the path interpolation with lookahead channel
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

# Define the points with their respective smooth radii
points = [
    (50, 0, 2.5),
    (50, 50, 5),
    (0, 50, 10),
    (0, 0, 0)
]

for i, (x, y, smooth_radius) in enumerate(points):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, x)
    point.linear.SetTarget(1, y)
    point.linear.smoothRadius = smooth_radius
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start the motion for the path interpolation with lookahead channel.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for a path interpolation with lookahead channel.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
