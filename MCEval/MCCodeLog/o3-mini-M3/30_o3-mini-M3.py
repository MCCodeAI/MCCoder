
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

# Create an instance of AdvancedMotion using the provided library instance Wmx3Lib.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previous lookahead buffer on channel 10.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
# If the error code is not 0 and is not ChannelBufferMemoryNotAllocated (e.g. 65627), then report error.
if ret != 0 and ret != 65627:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Allocate buffer memory for the path interpolation with look-ahead on channel 10.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look-ahead channel.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 0)   # Set first axis as Axis 0.
conf.SetAxis(1, 1)   # Set second axis as Axis 1.
conf.compositeVel = 1500          # Set composite velocity.
conf.compositeAcc = 10000         # Use a default composite acceleration.
conf.sampleDistance = 100         # Set sample distance.
conf.stopOnEmptyBuffer = True     # Wait for motion to complete when the buffer empties.

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Create the path with four interpolation points.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

# First point: (50, 0) with smooth radius 2.5
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 2.5
path.SetPoint(0, point)

# Second point: (50, 50) with smooth radius 5
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 5
path.SetPoint(1, point)

# Third point: (0, 50) with smooth radius 10
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 10
path.SetPoint(2, point)

# Fourth point: (0, 0) with no smooth radius specified.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
# (No smooth radius value assigned for the last segment)
path.SetPoint(3, point)

# Add the path interpolation commands to channel 10.
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start the motion for the path interpolation on channel 10.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete by waiting for both Axis 0 and Axis 1 to stop.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free the path interpolation buffer for channel 10 after completion.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0 and ret != 65627:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
