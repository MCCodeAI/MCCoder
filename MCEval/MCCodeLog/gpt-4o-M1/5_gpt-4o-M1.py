
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Define a function to move Axis 5 to a specified position at a given speed
def move_axis_5_to_position(position, speed):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = position
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
    # Move Axis 5 to position 66.6 at a speed of 900
    move_axis_5_to_position(66.6, 900)
    
    # Move Axis 5 back to position 0 at a speed of 900
    move_axis_5_to_position(0, 900)
