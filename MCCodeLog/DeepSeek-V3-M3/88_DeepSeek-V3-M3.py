
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Initialize the WMX3 library
Wmx3Lib = WMX3Api()
Wmx3Lib_cm = CoreMotion(Wmx3Lib)
Wmx3Lib_comp = Compensation(Wmx3Lib)

# Disable Backlash Compensation before setting new parameters
ret = Wmx3Lib_comp.DisableBacklashCompensation(8)
if ret != 0:
    print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    exit()

# Set the positive direction BacklashCompensation for Axis 8
backlashcomp = BacklashCompensationData()
backlashcomp.enable = 1
backlashcomp.offsetDirection = 1
backlashcomp.backlashHigh = 11
backlashcomp.backlashLow = 4
backlashcomp.distanceHigh = 80
backlashcomp.distanceLow = 30

# Set the BacklashCompensation for Axis 8
ret = Wmx3Lib_comp.SetBacklashCompensation(8, backlashcomp)
if ret != 0:
    print('SetBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    exit()

# Enable Backlash Compensation after setting new parameters
ret = Wmx3Lib_comp.EnableBacklashCompensation(8)
if ret != 0:
    print('EnableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    exit()

# Create a command value of target as 122.6
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 122.6
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(8)

# Disable Backlash Compensation after motion is complete
ret = Wmx3Lib_comp.DisableBacklashCompensation(8)
if ret != 0:
    print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    exit()
