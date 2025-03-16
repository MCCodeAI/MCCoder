
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = [0.6]

# The following code executes a path interpolation with look-ahead for Axis 3 and Axis 5 at a velocity of 2400.
# The motion sequence is:
#   1. When the completed distance reaches 50, set IO output 0.6 to 1.
#   2. When the remaining distance is 30, set IO output 0.6 to 0.
#   3. Perform a linear interpolation to the target position (100, 200).
#
# Note: This code waits for the axes to stop after each motion command before proceeding, as required.
#
# Please note: This script assumes that classes and functions such as AdvancedMotion, AdvMotion_PathIntplLookaheadCommand,
# AdvMotion_PathIntplLookaheadConfiguration, etc., are available in your environment. No motion libraries are imported here.

from time import sleep

# Initialize AdvancedMotion object (assumes Wmx3Lib is defined in the context)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create an empty path interpolation command object
path = AdvMotion_PathIntplLookaheadCommand()

# Free any existing path interpolation buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# Create the path interpolation with look-ahead buffer with composite velocity 2400
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2400)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code: ' + str(ret) + ' : ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with look-ahead channel for Axis 3 and Axis 5.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 2400
conf.compositeAcc = 2000    # Using a default acceleration value (adjust if necessary)
conf.sampleDistance = 100   # Sample distance can be adjusted as needed
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code: ' + str(ret) + ' : ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Prepare the path with 3 command points
path.numPoints = 3

# Point 0: Set IO output 0.6 to 1 when completed distance equals 50.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0
point.setOutputBit.bitAddress = 6  # represents IO output "0.6"
point.setOutputBit.value = 1
point.setOutputBit.triggerValue = 50
point.setOutputBit.type = AdvMotion_PathIntplOutputType.CompletedDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(0, point)

# Point 1: Set IO output 0.6 to 0 when remaining distance equals 30.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0
point.setOutputBit.bitAddress = 6  # represents IO output "0.6"
point.setOutputBit.value = 0
point.setOutputBit.triggerValue = 30
point.setOutputBit.type = AdvMotion_PathIntplOutputType.RemainingDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(1, point)

# Point 2: Linear interpolation to the target coordinates (100, 200).
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 100)
point.linear.SetTarget(1, 200)
path.SetPoint(2, point)

# Add the prepared path commands to the look-ahead channel buffer.
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code: ' + str(ret) + ' : ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Start the path interpolation with look-ahead.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code: ' + str(ret) + ' : ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the path interpolation to complete.
Wmx3Lib_cm.motion.Wait(5)  # The wait time can be adjusted based on expected motion duration.
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if timeoutCounter > 500:
    print('PathIntplLookahead Running timeout!')
    exit()

# Free the path interpolation with look-ahead buffer (typically done at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code: ' + str(ret) + ' : ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
