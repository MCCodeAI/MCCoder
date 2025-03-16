
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Set the positive direction BacklashCompensation for Axis 8
Wmx3Lib_comp = Compensation(Wmx3Lib)

backlashcomp = BacklashCompensationData()
backlashcomp.enable = 1
backlashcomp.offsetDirection = 1
backlashcomp.backlashHigh = 11
backlashcomp.backlashLow = 4
backlashcomp.distanceHigh = 80
backlashcomp.distanceLow = 30

ret = Wmx3Lib_comp.SetBacklashCompensation(8, backlashcomp)
if ret != 0:
    print('SetBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    return

# Move Axis 8 from 0 to absolute position 122.6 at speed 2000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 122.6
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(8)

# Disable Backlash Compensation
ret = Wmx3Lib_comp.DisableBacklashCompensation(8)
if ret != 0:
    print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + Wmx3Lib_comp.ErrorToString(ret))
    return
