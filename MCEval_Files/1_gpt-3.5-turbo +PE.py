
#WMX3 python library
from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    print('Program begin.')
    sleep(1)

    # Create devices. 
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret!=0:
        print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    # Set Device Name.
    Wmx3Lib.SetDeviceName('WMX3initTest')

    # Start Communication.
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret!=0:
        print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    #Clear every servo/motor/amplifier's alarm
    timeoutCounter=0
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (not CmStatus.GetAxesStatus(0).ampAlarm):
            break
        ret = Wmx3Lib_cm.axisControl.ClearAmpAlarm(0)
        sleep(0.5)
        timeoutCounter=timeoutCounter+1
        if(timeoutCounter > 5):
            break
    if(timeoutCounter > 5):
        print('Clear axis alarm fails!')

    # Set servo on for Axis 0. 
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).servoOn):
            break
        sleep(0.1)

    #Sleep is a must between SetServoOn and Homing
    sleep(0.1) 
    # Homing
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(0)
    homeParam.homeType = Config_HomeType.CurrentPos

    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(0, homeParam)

    ret = Wmx3Lib_cm.home.StartHome(0)
    if ret!=0:
        print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(0)

    # Create a command value of target as 180.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    # Set servo off.
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 0)
    if ret!=0:
        print('SetServoOn to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

    # Stop Communication.
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret!=0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    # Close Device.
    ret = Wmx3Lib.CloseDevice()
    if ret!=0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    print('Program End.')

if __name__ == '__main__':
    main()
