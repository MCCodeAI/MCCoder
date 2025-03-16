
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# List of target positions for Axis 4 (in sequence)
positions = [-10, 10, -10, 0]

# Iterate over each target position and execute the motion command.
for target in positions:
    # Create the position command for Axis 4 using the TwoVelocityTrapezoidal profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal  # Corrected profile type
    posCommand.axis = 4
    posCommand.target = target
    posCommand.profile.velocity = 1000
    # Assumed acceleration and deceleration constants; adjust if needed.
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    # Optional parameters for a two-velocity profile.
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0
    # Set the second velocity required for the two-velocity profile.
    posCommand.profile.secondVelocity = 5000  # Example value; change if needed

    # Execute the absolute position command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis stops moving before starting the next motion.
    Wmx3Lib_cm.motion.Wait(4)
