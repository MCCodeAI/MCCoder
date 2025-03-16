
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Create a position command object for Axis 5
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.velocity = 1000  # Default velocity value from context examples
posCommand.profile.acc = 10000      # Default acceleration value
posCommand.profile.dec = 10000      # Default deceleration value

# List of relative movement distances
movement_distances = [50, -50, 100, -100]

# Execute each movement with blocking wait
for distance in movement_distances:
    posCommand.target = distance
    
    # Start relative movement command
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print(f'StartMov error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        return
    
    # Blocking wait until Axis 5 stops
    Wmx3Lib_cm.motion.Wait(5)
