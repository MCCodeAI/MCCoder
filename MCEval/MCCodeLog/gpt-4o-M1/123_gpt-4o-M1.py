
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

# Initialize event control and motion command objects
eventIN_Motion = CoreMotionEventInput()
posCommand = Motion_PosCommand()

# Set the event input to monitor the RemainingDistance of Axis 0
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
eventIN_Motion.remainingDistance.axis = 0
eventIN_Motion.remainingDistance.distance = 1000
eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

# Define the motion command for Axis 1
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 800
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Start the motion for Axis 1 when the event is triggered
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to complete its motion
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define the motion command for Axis 0
posCommand.axis = 0
posCommand.target = 2000

# Start the motion for Axis 0
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 0 to complete its motion
ret = Wmx3Lib_cm.motion.Wait(0)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
