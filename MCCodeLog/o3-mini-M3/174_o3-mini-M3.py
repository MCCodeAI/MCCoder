
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def move_axis_3_advancedS():
    # Define the sequence of target positions: -20, 30, -40, and 0.
    target_positions = [-20, 30, -40, 0]
    
    # For each target position, create and configure the position command,
    # then execute the absolute move with Advanced-S profile and wait until the move is complete.
    for target in target_positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.AdvancedS
        posCommand.axis = 3
        posCommand.target = target
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000
        posCommand.profile.jerkAccRatio = 0.5
        posCommand.profile.jerkDecRatio = 0.5
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = 0

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until Axis 3 completes the move before issuing the next command.
        Wmx3Lib_cm.motion.Wait(3)

# Execute the sequence of moves.
move_axis_3_advancedS()
