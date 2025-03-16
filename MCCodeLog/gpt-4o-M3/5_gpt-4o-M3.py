
# Axes = [5]
# Inputs = []
# Outputs = []

# Define a function to move Axis 5 to a specified position at a given speed
def move_axis_5(target_position, speed):
    # Create a position command for Axis 5
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = target_position
    posCommand.profile.velocity = speed
    posCommand.profile.acc = 10000  # Assuming a default acceleration
    posCommand.profile.dec = 10000  # Assuming a default deceleration

    # Execute command to move to the specified absolute position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(5)

# Repeat the cycle 3 times
for _ in range(3):
    # Move Axis 5 to position 66.6 at speed 900
    move_axis_5(66.6, 900)
    # Move Axis 5 back to position 0 at speed 900
    move_axis_5(0, 900)
