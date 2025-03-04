#Set the Flight Recorder parameters for Axis 0. Set‘Enable Flight Recorder’to TRUE,‘Flight Recorder Time Stamp’to FALSE,‘Collect Axis Flight Recorder Data’to TRUE,‘Trigger Flight Recorder On Amp Alarm’to TRUE.
    # Axes = [0]


    # Example of Axis 0
    axis = 0
    # Enable Flight Recorder    This parameter determines whether flight recorder data should be saved to disk when one of the conditions for triggering the flight recorder is satisfied. The flight recorder data contains the position command and position feedback data of the axes for the last 5000 cycles (5 seconds for a 1ms Cycle Time Milliseconds) from when the flight recorder is triggered. The flight recorder is stored in the path specified by the user with SetFlightRecorderPath, or "C:\" by default, and has the file name "wmx_flight_recorder_ipt0.txt".
    # Variable Name:   enableFlightRecorder
    # Type:            bool
    # Default Value:   TRUE
    # Target:          System
    # Read the current values of parameters
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    flightRecorderParam.enableFlightRecorder = True
    # flightRecorderParam -> First return value: Error code, Second return value: param error
    ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
    if (ret != 0):
        print('Set flightRecorderParam  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Flight Recorder Time Stamp   This parameter determines whether the file name of the flight recorder data file should contain the date and time information of when the flight recorder was triggered. If this parameter is set to FALSE, the flight recorder data file will be overwritten each time the flight recorder is triggered (as the file name is the same). If this parameter is set to TRUE, the flight recorder data file name will become "[YYYY.MM.DD_HH.mm.SS]wmx_flight_recorder_ipt0.txt," where YY = year, MM = month, DD = day, HH = hour in 24-hour format, mm = minute, and SS = second.
    # Variable Name:   flightRecorderTimeStamp
    # Type:            bool
    # Default Value:   FALSE
    # Target:          System
    # Read the current values of parameters
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    flightRecorderParam.flightRecorderTimeStamp = True
    # flightRecorderParam -> First return value: Error code, Second return value: param error
    ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
    if (ret != 0):
        print('Set flightRecorderTimeStamp  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Collect Axis Flight Recorder Data    This parameter determines whether the file name of the flight recorder data file should contain the date and time information of when the flight recorder was triggered. If this parameter is set to FALSE, the flight recorder data file will be overwritten each time the flight recorder is triggered (as the file name is the same). If this parameter is set to TRUE, the flight recorder data file name will become "[YYYY.MM.DD_HH.mm.SS]wmx_flight_recorder_ipt0.txt," where YY = year, MM = month, DD = day, HH = hour in 24-hour format, mm = minute, and SS = second.
    # Variable Name:   collectAxisFlightRecorderData
    # Type:            bool
    # Default Value:   TRUE
    # Target:          Axis
    # Read the current values of parameters
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    flightRecorderParam.SetCollectAxisFlightRecorderData(axis,True)

    # flightRecorderParam -> First return value: Error code, Second return value: param error
    ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
    if (ret != 0):
        print('Set triggerFlightRecorderOnAmpAlarm   error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Trigger Flight Recorder On Amp Alarm   TRUE: The flight recorder will trigger when a servo amplifier alarm is detected in any axis (including axes that are not configured to collect flight recorder data).FALSE: The flight recorder will not be triggered by amp alarms.
    # Variable Name:   triggerFlightRecorderOnAmpAlarm
    # Type:            bool
    # Default Value:   TRUE
    # Target:          System
    # Read the current values of parameters
    flightRecorderParam = Config_FlightRecorderParam()
    ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
    flightRecorderParam.triggerFlightRecorderOnAmpAlarm = True
    # flightRecorderParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
    if (ret != 0):
        print('Set triggerFlightRecorderOnAmpAlarm  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

