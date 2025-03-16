
# Axes = [9]
# IOInputs = []
# IOOutputs = []

import time

# Simulation dictionaries to store parameters and axis positions
axis_params = {9: {}}
axis_positions = {9: 0.0}

def wait_axis_stop(axis):
    # Simulate waiting for an axis to stop moving.
    time.sleep(1)  # In a real system, replace with actual wait logic.
    
def set_e_stop_level1_type(axis, value):
    # Simulate setting the E-Stop Level 1 Type parameter for the given axis.
    print(f"Setting E-Stop Level 1 Type for Axis {axis} to {value}")
    axis_params[axis]['eStopLevel1Type'] = value
    # Return 0 to indicate success in this simulation.
    return 0

def get_e_stop_level1_type(axis):
    # Simulate retrieving the current E-Stop Level 1 Type parameter for the given axis.
    return axis_params[axis].get('eStopLevel1Type', None)

def move_axis(axis, target, profile="default"):
    # Simulate moving an axis to a target position with a given motion profile.
    print(f"Moving Axis {axis} to position {target} with profile '{profile}'")
    # Simulate start of motion: update axis position.
    axis_positions[axis] = target
    # Wait until the axis stops moving.
    wait_axis_stop(axis)
    print(f"Axis {axis} reached position {target}")

def main():
    axis = 9
    
    # Set the E-Stop Level 1 Type parameter of Axis 9 to DecServoOff.
    ret = set_e_stop_level1_type(axis, "DecServoOff")
    if ret != 0:
        print(f"Error: Failed to set E-Stop Level 1 Type for Axis {axis}")
        return

    # Check if the parameter has been set correctly.
    current_setting = get_e_stop_level1_type(axis)
    print(f"Current E-Stop Level 1 Type for Axis {axis} is '{current_setting}'")
    
    # If set correctly, move Axis 9 to position 99.9 with the default motion profile.
    if current_setting == "DecServoOff":
        move_axis(axis, 99.9, profile="default")
    else:
        # Otherwise, move Axis 9 to -99.9 with an S curve profile.
        move_axis(axis, -99.9, profile="S curve")

if __name__ == "__main__":
    main()
