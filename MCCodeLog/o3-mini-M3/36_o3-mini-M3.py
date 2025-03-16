
# Axes = [6, 8]
# IOInputs = []
# IOOutputs = []

def record_and_execute_api_buffer():
    # Initialize API buffer for recording
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    
    # Clear the buffer on channel 0
    Wmx3Lib_buf.Clear(0)
    
    # Create a buffer for channel 0 with the specified size
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    
    # Start recording commands on channel 0
    Wmx3Lib_buf.StartRecordBufferChannel(0)
    
    # ---------------------------
    # Segment 1: Move Axis 6 to position 150
    # ---------------------------
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 150
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error for Axis 6: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the motion for Axis 6 completes (first segment)
    Wmx3Lib_buf.Wait(0)
    
    # ---------------------------
    # Segment 2: Move Axis 8 to position 180
    # ---------------------------
    posCommand.axis = 8
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error for Axis 8: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the motion for Axis 8 completes (second segment)
    Wmx3Lib_buf.Wait(1)
    
    # End the recording in the buffer
    Wmx3Lib_buf.EndRecordBufferChannel()
    
    # Execute all recorded commands in the API buffer on channel 0
    Wmx3Lib_buf.Execute(0)
    
    # Wait for both Axis 6 and Axis 8 to stop moving
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 6)
    axisSel.SetAxis(1, 8)
    
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Clean up API buffer resources on channel 0
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

# Execute the API buffer recording and execution
record_and_execute_api_buffer()
