
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = []

# Define the path points for the pentastar
path_points = [
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

# Initialize the motion control library
# Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create the path interpolation buffer
# ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1500)
# if ret != 0:
#     print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
#     return

# Configure the path interpolation
# conf = AdvMotion_PathIntplLookaheadConfiguration()
# conf.axisCount = 2
# conf.SetAxis(0, 7)
# conf.SetAxis(1, 8)
# conf.compositeVel = 1500
# conf.compositeAcc = 4000
# conf.stopOnEmptyBuffer = True

# ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
# if ret != 0:
#     print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
#     return

# Add the path points to the interpolation buffer
# path = AdvMotion_PathIntplLookaheadCommand()
# path.numPoints = len(path_points)

# for i, (x, y) in enumerate(path_points):
#     Point = AdvMotion_PathIntplLookaheadCommandPoint()
#     Point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
#     Point.linear.axisCount = 2
#     Point.linear.SetAxis(0, 7)
#     Point.linear.SetAxis(1, 8)
#     Point.linear.SetTarget(0, x)
#     Point.linear.SetTarget(1, y)
#     path.SetPoint(i, Point)

# ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
# if ret != 0:
#     print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
#     return

# Execute the path interpolation
# ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
# if ret != 0:
#     print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
#     return

# Wait for the path interpolation to complete
# Wmx3Lib_cm.motion.Wait(7)
# timeoutCounter = 0
# ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
# while True:
#     if pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
#         break
#     sleep(0.1)
#     timeoutCounter += 1
#     if timeoutCounter > 500:
#         break
#     ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
# if timeoutCounter > 500:
#     print('PathIntplLookahead Running timeout.!')
#     return

# Free the path interpolation buffer
# ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# if ret != 0:
#     print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
#     return
