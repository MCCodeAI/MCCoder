
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to position 80 with a velocity of 900 and an end velocity of 800.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 80
posCommand.profile.velocity = 900
posCommand.profile.endVelocity = 800
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error during Axis 2 move to 80: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # You can handle the error accordingly.
    
# Wait until Axis 2 stops moving.
Wmx3Lib_cm.motion.Wait(2)

# Move Axis 2 to position 100 with a start velocity of 800.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 100
posCommand.profile.velocity = 900     # Continue with the same velocity profile if applicable.
posCommand.profile.startVelocity = 800  # Set the start velocity as specified.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error during Axis 2 move to 100: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Handle the error as necessary.
    
# Wait until Axis 2 stops moving.
Wmx3Lib_cm.motion.Wait(2)
