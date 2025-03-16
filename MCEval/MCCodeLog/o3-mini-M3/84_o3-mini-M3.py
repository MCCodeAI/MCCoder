
# Axes = [8]
# IOInputs = [3.5]
# IOOutputs = []

def run_api_buffer():
    # Assuming Wmx3Lib and Wmx3Lib_cm are already defined and initialized 
    # in the system environment.
    
    # Create an API buffer instance.
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    
    # Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)
    
    # Define a condition based on IO input 3.5 being equal to 0.
    cond = ApiBufferCondition()
    cond.bufferConditionType = ApiBufferConditionType.IOInput
    # Set the IO input condition:
    cond.arg_ioInput.byteAddress = 3
    cond.arg_ioInput.bitAddress = 5
    cond.arg_ioInput.value = 0  # Checking if IO input 3.5 equals 0
    
    # Set the IF branch: When IO input 3.5 equals 0.
    Wmx3Lib_buf.FlowIf(cond)
    
    # Add a position command to move Axis 8 by a distance of 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 200
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for Axis 8 to complete the motion.
    Wmx3Lib_cm.motion.Wait(8)
    
    # Set the ELSE branch: When IO input 3.5 does not equal 0.
    Wmx3Lib_buf.FlowElse()
    
    # Modify the position command to move Axis 8 by a distance of -140.
    posCommand.axis = 8
    posCommand.target = -140
    
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for Axis 8 to complete the motion.
    Wmx3Lib_cm.motion.Wait(8)
    
    # End the conditional block.
    Wmx3Lib_buf.FlowEndIf()
    
    # End recording of the API buffer.
    Wmx3Lib_buf.EndRecordBufferChannel()
    
    # Execute the recorded API buffer.
    Wmx3Lib_buf.Execute(0)
    
    # Wait for Axis 8 to finish executing the buffer commands.
    Wmx3Lib_cm.motion.Wait(8)
    
    # Release API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

if __name__ == "__main__":
    run_api_buffer()
