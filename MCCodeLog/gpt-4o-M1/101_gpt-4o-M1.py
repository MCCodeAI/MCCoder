
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Write Python code to get the System status 'Engine State' for the entire system; If it is Communicating, move Axis 1 to 111.1, otherwise, move to 0.1.

# Read the current system status from the engine
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check the Engine State
print('Engine State : ' + str(CmStatus.engineState))
if CmStatus.engineState == 'Communicating':
    # Move Axis 1 to 111.1
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = 111.1
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000  # Example acceleration
    posCommand.profile.dec = 10000  # Example deceleration
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for the motion to complete
    ret = Wmx3Lib_cm.motion.Wait(1)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 1 to 0.1
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = 0.1
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000  # Example acceleration
    posCommand.profile.dec = 10000  # Example deceleration
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for the motion to complete
    ret = Wmx3Lib_cm.motion.Wait(1)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
