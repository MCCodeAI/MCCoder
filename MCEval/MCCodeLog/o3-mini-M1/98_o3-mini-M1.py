
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# This script sets the "Trigger Flight Recorder On Amp Alarm" parameter (a System parameter)
# for Axis 8 to False. It then reads back the parameter to verify if it was set correctly.
# If the parameter is indeed False, it commands Axis 8 to move to 88; otherwise, it moves Axis 8 to -88.
# After issuing a motion command, the script waits until the axis stops moving.

def set_trigger_flight_recorder_on_amp_alarm(flag):
    """
    Sets the Trigger Flight Recorder On Amp Alarm parameter.
    flag: bool - the value to set (False in this case).
    Returns True if the parameter was set successfully, False otherwise.
    """
    # Get current flight recorder parameters (System target)
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    if ret != 0:
        print("Error getting flight recorder parameters. Error code:", ret)
        return False

    # Set the parameter to the specified flag value.
    flightRecorderParam.triggerFlightRecorderOnAmpAlarm = flag
    ret, paramError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
    if ret != 0:
        print("Error setting Trigger Flight Recorder On Amp Alarm. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        return False

    return True

def check_trigger_flight_recorder_on_amp_alarm(expected_flag):
    """
    Reads back the Trigger Flight Recorder On Amp Alarm parameter and checks if it matches expected_flag.
    Returns True if it matches, False otherwise.
    """
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    if ret != 0:
        print("Error reading flight recorder parameters. Error code:", ret)
        return False

    return flightRecorderParam.triggerFlightRecorderOnAmpAlarm == expected_flag

def move_axis(axis, target, velocity=1000, acc=10000, dec=10000):
    """
    Moves the specified axis to the given target position using a trapezoidal profile.
    After issuing the motion command, it waits until the axis stops.
    """
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = target
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = acc
    posCommand.profile.dec = dec

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))
    # Wait for the axis to stop moving
    Wmx3Lib_cm.motion.Wait(axis)

def main():
    axis = 8

    # Step 1: Set the parameter to False.
    if not set_trigger_flight_recorder_on_amp_alarm(False):
        return

    # Step 2: Check if the parameter is set correctly.
    if check_trigger_flight_recorder_on_amp_alarm(False):
        # If parameter is set to False as expected, move Axis 8 to 88.
        target_position = 88
    else:
        # Otherwise, move Axis 8 to -88.
        target_position = -88

    # Step 3: Command Axis 8 to move to the determined target position.
    move_axis(axis, target_position)

if __name__ == '__main__':
    main()
