
# Axes = [1]
# IOInputs = []
# IOOutputs = []

def main():
    # Get the system status from the engine.
    # Using GetStatus() to retrieve the Engine State.
    ret, status = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Engine State: ' + str(status.engineState))
    
    # Determine target position for Axis 1 based on Engine State.
    # If the engine state is "Communicating", move Axis 1 to 111.1,
    # otherwise, move it to 0.1.
    if status.engineState == "Communicating":
        target = 111.1
    else:
        target = 0.1
    
    # Create the motion command for Axis 1.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    # Execute the absolute position command for Axis 1.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 1 stops moving before completing the operation.
    ret = Wmx3Lib_cm.motion.Wait(1)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
