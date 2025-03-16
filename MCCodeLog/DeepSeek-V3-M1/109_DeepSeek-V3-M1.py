
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# Initialize the AdvancedMotion object
adv = AdvancedMotion(Wmx3Lib)

# Create a path interpolation command object
path = AdvMotion_PathIntplCommand()

# Set the axes for the path interpolation
path.SetAxis(0, 2)  # Axis 2
path.SetAxis(1, 9)  # Axis 9

# Enable constant profile for the entire path
path.enableConstProfile = 1

# Define the motion profile
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1200
path.profile.acc = 10000
path.profile.dec = 10000

# Set the number of points in the path
path.numPoints = 4

# 1st segment: Linear interpolation to (-50, -50)
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -50)
path.SetTarget(1, 0, -50)

# 2nd segment: Clockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -100)
path.SetTarget(1, 1, -100)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, -1)  # -1 for clockwise

# 3rd segment: Linear interpolation to (50, 50)
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 50)
path.SetTarget(1, 2, 50)

# 4th segment: Counterclockwise circular interpolation to (-100, -100) with center at (0, 0)
path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -100)
path.SetTarget(1, 3, -100)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, 1)  # 1 for counterclockwise

# Start the path interpolation motion
ret = adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start an absolute linear interpolation to position (100, 200) with velocity 1000
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)  # Set target of Axis 2 to 100
lin.SetTarget(1, 200)  # Set target of Axis 9 to 200

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion with center position (100, 100), arc length 180, and velocity 1200
circ = Motion_CircularIntplCommand()
circ.axisCount = 2
circ.SetAxis(0, 2)
circ.SetAxis(1, 9)

circ.profile.type = ProfileType.Trapezoidal
circ.profile.velocity = 1200
circ.profile.acc = 10000
circ.profile.dec = 10000

circ.SetCenterPos(0, 100)  # Center X position
circ.SetCenterPos(1, 100)  # Center Y position
circ.SetTarget(0, 100)  # Target X position
circ.SetTarget(1, 200)  # Target Y position
circ.SetDirection(1)  # 1 for clockwise

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circ)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 9 and 2 to (100, 200)
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)  # Set target of Axis 2 to 100
lin.SetTarget(1, 200)  # Set target of Axis 9 to 200

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
