
# Axes = [10]
# IOInputs = []
# IOOutputs = []

def set_axis_polarity(axis, polarity):
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    if ret != 0:
        print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False
    
    axisParam.SetAxisPolarity(axis, polarity)
    
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if ret != 0:
        print('SetAxisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False
    
    return True

# Set Axis Polarity to -1
axis = 10
success = set_axis_polarity(axis, -1)

if success:
    # Check if Axis Polarity is set correctly
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    if ret == 0:
        current_polarity = axisParam.GetAxisPolarity(axis)
        if current_polarity == -1:
            print("Axis Polarity is set correctly to -1. Moving to 100.")
            
            # Move Axis 10 to 100
            posCommand = Motion_PosCommand()
            posCommand.profile.type = ProfileType.Trapezoidal
            posCommand.axis = axis
            posCommand.target = 100
            posCommand.profile.velocity = 1000
            posCommand.profile.acc = 10000
            posCommand.profile.dec = 10000
            
            ret = Wmx3Lib_cm.motion.StartPos(posCommand)
            if ret != 0:
                print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
                return
            
            # Wait until the axis stops
            Wmx3Lib_cm.motion.Wait(axis)
        else:
            print("Axis Polarity is not set correctly. Moving to -10.")
            
            # Move Axis 10 to -10
            posCommand = Motion_PosCommand()
            posCommand.profile.type = ProfileType.Trapezoidal
            posCommand.axis = axis
            posCommand.target = -10
            posCommand.profile.velocity = 1000
            posCommand.profile.acc = 10000
            posCommand.profile.dec = 10000
            
            ret = Wmx3Lib_cm.motion.StartPos(posCommand)
            if ret != 0:
                print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
                return
            
            # Wait until the axis stops
            Wmx3Lib_cm.motion.Wait(axis)
    else:
        print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    print("Failed to set Axis Polarity")
