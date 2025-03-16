
# Axes = [8]
# IOInputs = []
# IOOutputs = []

def wait_for_axis_stop(axis):
    # Simulate waiting until the specified axis stops moving.
    print(f"Waiting for Axis {axis} to stop moving...")
    # (In a real system, code to poll the hardware or sleep until movement has completed would be here.)
    print(f"Axis {axis} has stopped moving.")

def move_axis(axis, target, velocity):
    # Simulate moving the axis to a target position with a specified velocity.
    print(f"Moving Axis {axis} to position {target} with velocity {velocity}.")
    # (Insert code to start the motion command here.)
    wait_for_axis_stop(axis)

def set_axis_parameter(axis, parameter_name, value):
    # Simulate setting a motion parameter for the specified axis.
    print(f"Setting Axis {axis} parameter '{parameter_name}' to {value}.")

if __name__ == "__main__":
    axis = 8

    # Move Axis 8 to position 150.
    move_axis(axis, 150, 1000)

    # Set 'Enable Global Starting Velocity' parameter to TRUE.
    set_axis_parameter(axis, "Enable Global Starting Velocity", True)
    # Set 'Global Starting Velocity' parameter to 555.
    set_axis_parameter(axis, "Global Starting Velocity", 555)

    # Move Axis 8 to position 300.
    move_axis(axis, 300, 1000)
