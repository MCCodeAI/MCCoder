
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get system status
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if engine state is communicating
if CmStatus.engineState == EngineState.Communicating:
    # Move Axis 1 to 111.1
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = 111.1
    posCommand.profile.velocity = 1000  # Example velocity value
    posCommand.profile.acc = 10000     # Example acceleration value
    posCommand.profile.dec = 10000     # Example deceleration value
    
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 1 to 0.1
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = 0.1
    posCommand.profile.velocity = 1000  # Example velocity value
    posCommand.profile.acc = 10000     # Example acceleration value
    posCommand.profile.dec = 10000     # Example deceleration value
    
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait for the motion to complete
Wmx3Lib_cm.motion.Wait(1)
