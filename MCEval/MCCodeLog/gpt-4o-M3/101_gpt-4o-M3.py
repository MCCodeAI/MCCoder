
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Function to get the system status and move Axis 1 based on the 'Engine State'
def move_axis_based_on_engine_state():
    # Get the current system status
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Check the 'Engine State'
    engine_state = CmStatus.engineState
    print('Engine State : ' + str(engine_state))

    # Create a command value for Axis 1
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1

    # Move Axis 1 based on the 'Engine State'
    if engine_state == 'Communicating':
        posCommand.target = 111.1
    else:
        posCommand.target = 0.1

    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move Axis 1
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(1)

# Call the function to execute the task
move_axis_based_on_engine_state()
