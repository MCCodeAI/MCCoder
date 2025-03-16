
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Set the Trigger Flight Recorder On Amp Alarm parameter of Axis 8 to False
axis = 8

# Read the current values of parameters
flightRecorderParam = Config_FlightRecorderParam()
ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
if ret != 0:
    print('GetFlightRecorderParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set the Trigger Flight Recorder On Amp Alarm parameter to False
flightRecorderParam.triggerFlightRecorderOnAmpAlarm = False

# Set the updated parameters
ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
if ret != 0:
    print('SetFlightRecorderParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if the Trigger Flight Recorder On Amp Alarm parameter is set correctly
ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
if ret != 0:
    print('GetFlightRecorderParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if flightRecorderParam.triggerFlightRecorderOnAmpAlarm == False:
    # Move Axis 8 to 88
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 88
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 8 to -88
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -88
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
