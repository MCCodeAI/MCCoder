
# Axes = [2, 3]
# IOInputs = []
# IOOutputs = []

# This function executes a circular interpolation motion command and then waits for the axes to complete the motion.
def execute_motion(command):
    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(command)
    if ret != 0:
        print("StartCircularIntplPos_CenterAndLength error code is " + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait for the motion to complete on Axis 2 and 3.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False

    return True

# -------------------------------
# First Motion: Counterclockwise circular interpolation on Axis 2 and 3
# Center position: (50, 0), Arc length: 180 degrees, Velocity: 1000
# For counterclockwise motion, we set the "clockwise" flag to 0.
circularCommand1 = Motion_CenterAndLengthCircularIntplCommand()
circularCommand1.SetAxis(0, 2)
circularCommand1.SetAxis(1, 3)
circularCommand1.SetCenterPos(0, 50)
circularCommand1.SetCenterPos(1, 0)
circularCommand1.arcLengthDegree = 180
circularCommand1.profile.type = ProfileType.Trapezoidal
circularCommand1.profile.velocity = 1000
circularCommand1.profile.acc = 10000
circularCommand1.profile.dec = 10000
circularCommand1.clockwise = 0  # 0 for counterclockwise

if not execute_motion(circularCommand1):
    exit(1)

# -------------------------------
# Second Motion: Counterclockwise circular interpolation on Axis 2 and 3
# Center position: (75, 0), Arc length: 180 degrees (velocity remains 1000)
circularCommand2 = Motion_CenterAndLengthCircularIntplCommand()
circularCommand2.SetAxis(0, 2)
circularCommand2.SetAxis(1, 3)
circularCommand2.SetCenterPos(0, 75)
circularCommand2.SetCenterPos(1, 0)
circularCommand2.arcLengthDegree = 180
circularCommand2.profile.type = ProfileType.Trapezoidal
circularCommand2.profile.velocity = 1000
circularCommand2.profile.acc = 10000
circularCommand2.profile.dec = 10000
circularCommand2.clockwise = 0  # 0 for counterclockwise

if not execute_motion(circularCommand2):
    exit(1)

# -------------------------------
# Third Motion: Clockwise circular interpolation on Axis 2 and 3
# Center position: (25, 0), Arc length: 180 degrees (velocity remains 1000)
circularCommand3 = Motion_CenterAndLengthCircularIntplCommand()
circularCommand3.SetAxis(0, 2)
circularCommand3.SetAxis(1, 3)
circularCommand3.SetCenterPos(0, 25)
circularCommand3.SetCenterPos(1, 0)
circularCommand3.arcLengthDegree = 180
circularCommand3.profile.type = ProfileType.Trapezoidal
circularCommand3.profile.velocity = 1000
circularCommand3.profile.acc = 10000
circularCommand3.profile.dec = 10000
circularCommand3.clockwise = 1  # 1 for clockwise

if not execute_motion(circularCommand3):
    exit(1)

# -------------------------------
# Fourth Motion: Clockwise circular interpolation on Axis 2 and 3
# Center position: (50, 0), Arc length: 180 degrees (velocity remains 1000)
circularCommand4 = Motion_CenterAndLengthCircularIntplCommand()
circularCommand4.SetAxis(0, 2)
circularCommand4.SetAxis(1, 3)
circularCommand4.SetCenterPos(0, 50)
circularCommand4.SetCenterPos(1, 0)
circularCommand4.arcLengthDegree = 180
circularCommand4.profile.type = ProfileType.Trapezoidal
circularCommand4.profile.velocity = 1000
circularCommand4.profile.acc = 10000
circularCommand4.profile.dec = 10000
circularCommand4.clockwise = 1  # 1 for clockwise

if not execute_motion(circularCommand4):
    exit(1)
