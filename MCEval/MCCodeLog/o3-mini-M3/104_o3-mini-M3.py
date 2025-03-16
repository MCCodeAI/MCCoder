
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to position 80 with a speed of 900 and an end velocity of 800.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 80
posCommand.profile.velocity = 900      # Set the moving speed
posCommand.profile.acc = 10000         # Example acceleration value
posCommand.profile.dec = 10000         # Example deceleration value
posCommand.profile.endVelocity = 800   # Set the end velocity

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error appropriately (e.g., exit or retry)
else:
    # Wait until Axis 2 stops moving after the absolute move.
    Wmx3Lib_cm.motion.Wait(2)  # Assuming Wait(2) waits for Axis 2

# Move Axis 2 to position 100 with a start velocity of 800.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 100
posCommand.profile.velocity = 900      # Define velocity profile as needed (if applicable)
posCommand.profile.acc = 10000         # Example acceleration value
posCommand.profile.dec = 10000         # Example deceleration value
posCommand.profile.startVelocity = 800   # Set the start velocity

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error appropriately (e.g., exit or retry)
else:
    # Wait until Axis 2 stops moving after the second move.
    Wmx3Lib_cm.motion.Wait(2)  # Assuming Wait(2) waits for Axis 2
