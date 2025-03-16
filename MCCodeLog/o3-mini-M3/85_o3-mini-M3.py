
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

def main():
    # Instantiate the API buffer object for recording motions.
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    
    # Clear the buffer for channel 0 and create a new API buffer (using 5MB size).
    Wmx3Lib_buf.Clear(0)
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
    
    # Start recording the API buffer on channel 0.
    Wmx3Lib_buf.StartRecordBufferChannel(0)
    
    # Instantiate the condition and motion command objects.
    cond = ApiBufferCondition()
    lin = Motion_LinearIntplCommand()
    
    # Setup the two axes.
    lin.axisCount = 2
    lin.SetAxis(0, 3)
    lin.SetAxis(1, 6)
    
    # Set a common trapezoidal profile (velocity, acceleration, deceleration).
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    # -------- Segment 1: Linearly interpolate to (100, 0) --------
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 0)
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('Segment 1 error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until deceleration starts (using Axis 3 as reference) before issuing the next command.
    cond.bufferConditionType = ApiBufferConditionType.DecelerationStarted
    cond.arg_decelerationStarted.axis = 3
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)
    
    # -------- Segment 2: Linearly interpolate to (100, 100) --------
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 100)
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('Segment 2 error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    cond.arg_decelerationStarted.axis = 3
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)
    
    # -------- Segment 3: Linearly interpolate to (0, 100) --------
    lin.SetTarget(0, 0)
    lin.SetTarget(1, 100)
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('Segment 3 error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    cond.arg_decelerationStarted.axis = 3
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)
    
    # -------- Segment 4: Linearly interpolate to (0, 0) --------
    lin.SetTarget(0, 0)
    lin.SetTarget(1, 0)
    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('Segment 4 error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # End recording the API buffer.
    Wmx3Lib_buf.EndRecordBufferChannel()
    
    # Execute the API buffer that contains all the interpolation segments.
    Wmx3Lib_buf.Execute(0)
    
    # Wait for the motion to complete on both Axis 3 and Axis 6.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Clean up: halt and free the API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

if __name__ == '__main__':
    main()
