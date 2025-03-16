
# Axes = [5, 8]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to position 200
axis = 5
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = 200
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(axis)

# Get the Axis status for Axis 5
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if Pos Cmd is 200
if CmStatus.GetAxesStatus(axis).posCmd == 200:
    # Move Axis 5 to position 50
    posCommand.target = 50
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)

# Move Axis 8 to position 99 at a speed of 1000 using a TimeAccJerkRatio profile
axis = 8
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = axis
posCommand.target = 99
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(axis)
