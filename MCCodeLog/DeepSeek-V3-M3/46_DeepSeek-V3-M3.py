
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Define the positions to move Axis 6 to
positions = [50, -50, 100, -100]

# Create a position command object
posCommand = Motion_PosCommand()
posCommand.axis = 6
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Loop through each position and move Axis 6
for position in positions:
    posCommand.target = position
    
    # Execute the motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait until the axis moves to the target position and stops
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
