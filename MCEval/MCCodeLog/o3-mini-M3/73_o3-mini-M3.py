
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = [0.6]

# Create an instance for advanced motion
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation with look-ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# Create the path interpolation with look-ahead buffer with composite velocity of 2400
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2400)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with look-ahead channel for Axis 3 and Axis 5
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 2400
conf.compositeAcc = 2000  # Use an appropriate composite acceleration value
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Define the sequence of path interpolation commands
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 3

# First sequence: When completed distance is 50, set IO output 0.6 to 1.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0          # Byte 0
point.setOutputBit.bitAddress = 6             # Bit 6 represents IO output 0.6
point.setOutputBit.value = 1                  # Set the output to 1
point.setOutputBit.triggerValue = 50          # Trigger when completed distance is 50
point.setOutputBit.type = AdvMotion_PathIntplOutputType.CompletedDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(0, point)

# Second sequence: When remaining distance is 30, set IO output 0.6 to 0.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
point.setOutputBit.byteAddress = 0          # Byte 0
point.setOutputBit.bitAddress = 6             # Bit 6 represents IO output 0.6
point.setOutputBit.value = 0                  # Set the output to 0
point.setOutputBit.triggerValue = 30          # Trigger when remaining distance is 30
point.setOutputBit.type = AdvMotion_PathIntplOutputType.RemainingDist
point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
path.SetPoint(1, point)

# Third sequence: Linear interpolation to the target (100, 200) for Axis 3 and 5.
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 3)
point.linear.SetAxis(1, 5)
point.linear.SetTarget(0, 100)
point.linear.SetTarget(1, 200)
path.SetPoint(2, point)

# Add the path interpolation with look-ahead commands to the buffer
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Start the path interpolation with look-ahead execution
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the path interpolation to complete (i.e. wait until both axes stop moving)
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('PathIntplLookahead Running timeout.!')
        exit()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

# Free the look-ahead buffer after the motion completes
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
