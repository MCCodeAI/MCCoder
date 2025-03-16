
# Axes = [1]
# IOInputs = []
# IOOutputs = []

import time

def move_axis():
    # Get current axis status
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Get position command and actual position
    axis = 1
    pos_cmd = CmStatus.GetAxesStatus(axis).posCmd
    actual_pos = CmStatus.GetAxesStatus(axis).actualPos
    
    print(f'Current Position Command: {pos_cmd}')
    print(f'Current Actual Position: {actual_pos}')
    
    # Move axis to 101
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 101
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for axis to stop
    Wmx3Lib_cm.motion.Wait(axis)
    
    # Get new position command and actual position
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    pos_cmd = CmStatus.GetAxesStatus(axis).posCmd
    actual_pos = CmStatus.GetAxesStatus(axis).actualPos
    
    print(f'New Position Command: {pos_cmd}')
    print(f'New Actual Position: {actual_pos}')
    
    # Check if positions are the same
    if pos_cmd == actual_pos:
        print('Moving to 201')
        target = 201
    else:
        print('Moving to -201')
        target = -201
    
    # Move to final target
    posCommand.target = target
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for final movement to complete
    Wmx3Lib_cm.motion.Wait(axis)

if __name__ == "__main__":
    move_axis()
