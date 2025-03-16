
# Axes = [5, 7]
# IOInputs = []
# IOOutputs = []

# Initialize variables
j = 0
velocity = 1000

# Create a command for relative path interpolation
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 7)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = velocity
lin.profile.acc = 10000
lin.profile.dec = 10000

# Loop to add linear interpolation points while j < 5
while j < 5:
    # Set target positions for relative motion
    lin.SetTarget(0, 10 * j)
    lin.SetTarget(1, -10 * j)
    
    # Start relative position linear interpolation motion command
    ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
    if ret != 0:
        print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for the motion to complete
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 5)
    axisSel.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Increment j by 1
    j += 1
