
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to position 300.
posCommand = Motion_PosCommand()
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.type = ProfileType.Trapezoidal
# Use standard profile parameters (velocity, acceleration, deceleration) if needed.
posCommand.profile.velocity = 1000  
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error starting move for Axis 4: " + str(ret))
else:
    # Wait until Axis 4 stops moving.
    Wmx3Lib_cm.motion.Wait(4)

# Retrieve Axis 4 status.
# (Assume GetStatus returns a dict with key 'actual_pos')
status = Wmx3Lib_cm.motion.GetStatus(4)
actual_pos = status.get('actual_pos', None)
if actual_pos is None:
    print("Error: Could not retrieve actual position for Axis 4.")
else:
    # Decide next move based on the Actual Pos of Axis 4.
    if actual_pos == 200:
        # If actual position equals 200, move Axis 4 to position 50.
        posCommand = Motion_PosCommand()
        posCommand.axis = 4
        posCommand.target = 50
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.profile.velocity = 1000  
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print("Error moving Axis 4 to 50: " + str(ret))
        else:
            Wmx3Lib_cm.motion.Wait(4)
    else:
        # Otherwise, move Axis 4 to position -50.
        posCommand = Motion_PosCommand()
        posCommand.axis = 4
        posCommand.target = -50
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.profile.velocity = 1000  
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print("Error moving Axis 4 to -50: " + str(ret))
        else:
            Wmx3Lib_cm.motion.Wait(4)

# Move Axis 6 to position 111 using a TwoVelocityJerkRatio profile at a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.axis = 6
posCommand.target = 111
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio  # Use TwoVelocityJerkRatio profile.
posCommand.profile.velocity = 1000
# Set acceleration and deceleration as required.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error starting move for Axis 6: " + str(ret))
else:
    Wmx3Lib_cm.motion.Wait(6)
