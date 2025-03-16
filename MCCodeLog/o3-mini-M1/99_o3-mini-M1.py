
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def main():
    axis = 9

    # ---------------------------------------------------------------------------
    # Set the E-Stop Level 1 Type parameter for Axis 9 to DecServoOff.
    # ---------------------------------------------------------------------------
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    if ret != 0:
        print("Error retrieving E-Stop parameter for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    emergencyStopParam.eStopLevel1Type = Config_EStopLevel1Type.DecServoOff
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if ret != 0:
        print("Error setting E-Stop Level 1 Type for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # ---------------------------------------------------------------------------
    # Check if the parameter is set correctly.
    # ---------------------------------------------------------------------------
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    if ret != 0:
        print("Error retrieving E-Stop parameter for verification on Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # ---------------------------------------------------------------------------
    # Depending on the parameter value, move Axis 9:
    #   - If the parameter is DecServoOff, move to 99.9.
    #   - Otherwise, move to -99.9.
    # Use an S curve profile and wait until the axis stops moving after the command.
    # ---------------------------------------------------------------------------
    posCommand = Motion_PosCommand()
    posCommand.axis = axis
    posCommand.profile.type = ProfileType.SCurve
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    if emergencyStopParam.eStopLevel1Type == Config_EStopLevel1Type.DecServoOff:
        posCommand.target = 99.9
    else:
        posCommand.target = -99.9

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait for Axis 9 to finish moving before ending the script.
    Wmx3Lib_cm.motion.Wait(axis)


if __name__ == "__main__":
    main()
