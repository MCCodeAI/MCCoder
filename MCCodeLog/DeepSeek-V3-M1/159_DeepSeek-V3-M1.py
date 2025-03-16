
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to position 200
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 200
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000      # Example acceleration
posCommand.profile.dec = 10000      # Example deceleration

# Execute command to move to a specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(5)

# Get the Axis status for Axis 5
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if the Pos Cmd status is 200
if CmStatus.GetAxesStatus(5).posCmd == 200:
    # Move Axis 5 to position 50
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 50
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000      # Example acceleration
    posCommand.profile.dec = 10000      # Example deceleration

    # Execute command to move to a specified absolute position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(5)
