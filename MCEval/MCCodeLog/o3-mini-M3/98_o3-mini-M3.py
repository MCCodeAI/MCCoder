
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# First, set the Trigger Flight Recorder On Amp Alarm parameter of Axis 8 to False.
# Then, check if the parameter is correctly set. If it is, move Axis 8 to position 88;
# otherwise, move Axis 8 to -88.

# Get the current flight recorder parameters from the system.
flightRecorderParam = Config_FlightRecorderParam()
ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
if ret != 0:
    print("Error getting flight recorder parameters: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error (e.g., exit or return)
    
# Set the Trigger Flight Recorder On Amp Alarm parameter to False.
flightRecorderParam.triggerFlightRecorderOnAmpAlarm = False
ret, flightRecorderParamError = Wmx3Lib_cm.config.SetFlightRecorderParam(flightRecorderParam)
if ret != 0:
    print("Error setting triggerFlightRecorderOnAmpAlarm to False: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error (e.g., exit or return)

# Read back the parameter to ensure it is set correctly.
ret, flightRecorderParam = Wmx3Lib_cm.config.GetFlightRecorderParam()
if ret != 0:
    print("Error re-getting flight recorder parameters: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error (e.g., exit or return)

# Decide the target position based on the parameter value.
if flightRecorderParam.triggerFlightRecorderOnAmpAlarm == False:
    targetPosition = 88
else:
    targetPosition = -88

# Prepare and execute the motion command for Axis 8.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal  # Use a trapezoidal profile.
posCommand.axis = 8
posCommand.target = targetPosition
posCommand.profile.velocity = 1000  # Specified velocity (example value).
posCommand.profile.acc = 10000      # Acceleration (example value).
posCommand.profile.dec = 10000      # Deceleration (example value).

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error moving Axis 8 to position " + str(targetPosition) + ": " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    
# Wait until Axis 8 stops moving after the motion command.
Wmx3Lib_cm.motion.Wait(8)
