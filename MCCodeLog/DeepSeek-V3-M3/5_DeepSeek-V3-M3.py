
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Function to move Axis 5 to a specified position and speed
def move_axis_5(target_position, speed):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = target_position
    posCommand.profile.velocity = speed
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(5)

# Repeat the cycle 3 times
for _ in range(3):
    # Move Axis 5 to position 66.6 at a speed of 900
    move_axis_5(66.6, 900)
    
    # Move Axis 5 back to position 0 at a speed of 900
    move_axis_5(0, 900)
