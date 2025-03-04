
#WMX3 python library
from WMX3ApiPython import *
from time import *

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    
    # Initialize WMX3
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret != 0:
        print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    
    Wmx3Lib.SetDeviceName('WMX3initTest')
    
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret != 0:
        print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    
    # Create a command value for absolute position command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    # Start absolute position command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    
    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(0)
    
    # Close WMX3
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret != 0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    
    ret = Wmx3Lib.CloseDevice()
    if ret != 0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

if __name__ == '__main__':
    main()
