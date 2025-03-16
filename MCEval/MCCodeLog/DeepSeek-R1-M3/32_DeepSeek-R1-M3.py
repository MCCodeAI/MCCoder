
# Axes = [2, 3]
# IOInputs = []
# IOOutputs = []

# First counterclockwise circular interpolation (50, 0)
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand.SetAxis(0, 2)
circularIntplCommand.SetAxis(1, 3)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 0)
circularIntplCommand.clockwise = 0
circularIntplCommand.arcLengthDegree = 180
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1000
# CORRECTED ACC/DEC VALUES
circularIntplCommand.profile.acc = 5000  # Reduced from 10000
circularIntplCommand.profile.dec = 5000  # Reduced from 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print(f'StartCircularIntplPos_CenterAndLength error code: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error code: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Remainder of original code remains unchanged below this point...
