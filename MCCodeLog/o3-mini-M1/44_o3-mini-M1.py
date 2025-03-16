
# Axes = [4, 5, 8]
# IOInputs = []
# IOOutputs = []

import time

def execute_triggered_linear_interpolation():
    # Create and configure the linear interpolation command for Axis 4 and Axis 5.
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    lin.SetAxis(0, 4)
    lin.SetAxis(1, 5)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 50)

    # Start the interpolation motion for Axis 4 and Axis 5.
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Poll the status of one of the interpolation axes (using Axis 4 as representative)
    # and trigger Axis 8 motion when the distance to target reaches 20.
    triggered = False
    while not triggered:
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if ret != 0:
            print('GetStatus error code: ' + str(ret))
            break

        # Assume the status object provides a remainingDistance value.
        # (In practice, replace this with the appropriate API call.)
        remaining = CmStatus.GetAxesStatus(4).remainingDistance
        if remaining <= 20:
            triggered = True
            break
        time.sleep(0.05)  # Poll every 50ms

    # Once the trigger condition is met, execute the axis move for Axis 8.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 200
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion of Axis 8 to complete.
    ret = Wmx3Lib_cm.motion.Wait_Axis(8)
    if ret != 0:
        print('Wait for Axis 8 error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Finally, wait for the interpolation motion on Axis 4 and 5 to complete.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 4)
    axisSel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Execute the triggered linear interpolation motion command.
execute_triggered_linear_interpolation()
