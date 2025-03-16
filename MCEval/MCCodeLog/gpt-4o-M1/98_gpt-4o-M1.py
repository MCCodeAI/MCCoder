
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Set the Trigger Flight Recorder On Amp Alarm parameter of Axis 8 to false
flightRecorderParam = Config_FlightRecorderParam()
ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
flightRecorderParam.triggerFlightRecorderOnAmpAlarm = False
ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)

if ret != 0:
    print('Set triggerFlightRecorderOnAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Check if the parameter is set correctly
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    if flightRecorderParam.triggerFlightRecorderOnAmpAlarm == False:
        # Move Axis 8 to 88
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 8
        posCommand.target = 88
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        Wmx3Lib_cm.motion.Wait(8)
    else:
        # Move Axis 8 to -88
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 8
        posCommand.target = -88
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        Wmx3Lib_cm.motion.Wait(8)
