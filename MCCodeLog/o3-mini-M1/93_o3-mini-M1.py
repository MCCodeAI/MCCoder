
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def set_home_position(axis, value):
    # Retrieve current homing parameters for the specified axis
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    if ret != 0:
        print("Error reading home parameters for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return ret
    # Set the home position to the desired value
    homeParam.homePosition = value
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if ret != 0:
        print("Error setting home position for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
    return ret

def perform_homing(axis):
    # Execute the homing command for the specified axis.
    ret = Wmx3Lib_cm.motion.StartHome(axis)
    if ret != 0:
        print("Error starting homing for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return ret
    # Wait until the homing motion completes.
    Wmx3Lib_cm.motion.Wait(axis)
    return ret

def main():
    axis = 3

    # Step 1: Set Home Position parameter to 8.8 on Axis 3.
    ret = set_home_position(axis, 8.8)
    if ret != 0:
        return

    # Step 2: Execute homing for Axis 3.
    ret = perform_homing(axis)
    if ret != 0:
        return

    # Step 3: After homing, change the Home Position parameter back to 0.
    ret = set_home_position(axis, 0)
    if ret != 0:
        return

if __name__ == "__main__":
    main()
