
# Axes = [3, 1, 2]
# Inputs = []
# Outputs = []

# Set the input event to monitor if the CompletedTime of Axis 3's movement is 300ms
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.CompletedTime
eventIN_Motion.completedTime.axis = 3
eventIN_Motion.completedTime.timeMilliseconds = 300
eventIN_Motion.completedTime.disableIdleAxisTrigger = 1

# Define the motion command for Axis 1
posCommand_Axis1 = Motion_PosCommand()
posCommand_Axis1.profile.type = ProfileType.Trapezoidal
posCommand_Axis1.axis = 1
posCommand_Axis1.target = 300
posCommand_Axis1.profile.velocity = 1000
posCommand_Axis1.profile.acc = 10000
posCommand_Axis1.profile.dec = 10000

# Define the motion command for Axis 3
posCommand_Axis3 = Motion_PosCommand()
posCommand_Axis3.profile.type = ProfileType.Trapezoidal
posCommand_Axis3.axis = 3
posCommand_Axis3.target = 2000
posCommand_Axis3.profile.velocity = 1000
posCommand_Axis3.profile.acc = 10000
posCommand_Axis3.profile.dec = 10000

# Define the motion command for Axis 2
posCommand_Axis2 = Motion_PosCommand()
posCommand_Axis2.profile.type = ProfileType.Trapezoidal
posCommand_Axis2.axis = 2
posCommand_Axis2.target = 2000
posCommand_Axis2.profile.velocity = 1000
posCommand_Axis2.profile.acc = 10000
posCommand_Axis2.profile.dec = 10000

# Execute command to move Axis 3 to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis3)
if ret != 0:
    print('StartPos error code for Axis 3 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 3 moves to the target position and stops
Wmx3Lib_cm.motion.Wait(3)

# Execute command to move Axis 1 to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis1)
if ret != 0:
    print('StartPos error code for Axis 1 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 moves to the target position and stops
Wmx3Lib_cm.motion.Wait(1)

# Execute command to move Axis 2 to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis2)
if ret != 0:
    print('StartPos error code for Axis 2 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 2 moves to the target position and stops
Wmx3Lib_cm.motion.Wait(2)
