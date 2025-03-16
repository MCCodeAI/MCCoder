
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Create instances for motion command and trigger command
lin = Motion_LinearIntplCommand()
trig = Trigger()

# Configure the interpolation command for 2 axes:
# Map index 0 to Axis 3 and index 1 to Axis 6.
lin.axisCount = 2
lin.SetAxis(0, 3)
lin.SetAxis(1, 6)

# Set the motion profile parameters: trapezoidal profile with velocity=1000 and acceleration/deceleration=10000.
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the first absolute target position: (200 on Axis 3, 100 on Axis 6).
lin.SetTarget(0, 200)
lin.SetTarget(1, 100)

# Start the absolute position linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for 1 millisecond before setting up the trigger motion.
sleep(0.001)

# Prepare the second interpolation target: (-50 on Axis 3, -100 on Axis 6).
lin.SetTarget(0, -50)
lin.SetTarget(1, -100)

# Set up the trigger: when the completed distance of Axis 3 (mapped to index 0) reaches 100.
trig.triggerAxis = 0
trig.triggerType = TriggerType.CompletedDistance
trig.triggerValue = 100

# Start the triggered interpolation command with the new target.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for both Axis 3 and Axis 6 to complete motion before ending the script.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
