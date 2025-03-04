"""#####PYTHON SAMPLE CODE#####
Currently, there are no parameters to set the jerk limit for path interpolation with look ahead.
This is a typical python code of  ts by creating and naming a device with 'CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)' and 'SetDeviceName('WMX3initTest')', then begins communication with 'StartCommunication(INFINITE)'. The script clears any amplifier alarms with 'ClearAmpAlarm(axis)' and activates the servo with 'SetServoOn(axis, 1)'. It executes a motion command using 'StartMov(posCommand)' and concludes by shutting down the servo and stopping communication with 'SetServoOn(axis, 0)' and 'StopCommunication(INFINITE)'. This structured approach ensures each component is correctly set up and terminated, ensuring safe and effective system operations.
"""
#WMX3 python library
from WMX3ApiPython import *
from time import *
import math

INFINITE = int(0xFFFFFFFF)

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
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

    # Set servo on for Axis 0,Axis 1.
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
    ret = Wmx3Lib_cm.axisControl.SetServoOn(1, 1)

    timeoutCounter = 0
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).servoOn&CmStatus.GetAxesStatus(1).servoOn):
            break
        sleep(0.5)
        timeoutCounter = timeoutCounter + 1
        if (timeoutCounter > 5):
            break
    if (timeoutCounter > 5):
        print('Set servo on fails!')
        return



    #Sleep is a must between SetServoOn and Homing
    sleep(0.1)
    # Homing
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(0)
    homeParam.homeType = Config_HomeType.CurrentPos

    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(0, homeParam)

    ret = Wmx3Lib_cm.home.StartHome(0)
    Wmx3Lib_cm.motion.Wait(0)

    pvt = Motion_PVTCommand()
    pvtparameter = Motion_PVTPoint()

    pvt.axis = 0
    pvt.pointCount = 5

    # Define point data
    pvtparameter.pos = 0
    pvtparameter.velocity = 0
    pvtparameter.timeMilliseconds = 0
    pvt.SetPoints(0, pvtparameter)

    pvtparameter.pos = 5500
    pvtparameter.velocity = 10000
    pvtparameter.timeMilliseconds = 1000
    pvt.SetPoints(1, pvtparameter)

    pvtparameter.pos = 20500
    pvtparameter.velocity = 20000
    pvtparameter.timeMilliseconds = 2000
    pvt.SetPoints(2, pvtparameter)

    pvtparameter.pos = 45000
    pvtparameter.velocity = 30000
    pvtparameter.timeMilliseconds = 3000
    pvt.SetPoints(3, pvtparameter)

    pvtparameter.pos = 60000
    pvtparameter.velocity = 0
    pvtparameter.timeMilliseconds = 4000
    pvt.SetPoints(4, pvtparameter)

    # Start PVT motion
    ret = Wmx3Lib_cm.motion.StartPVT(pvt)

    if ret != 0:
        print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

    sleep(100)

    # Set servo off.
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 0)
    if ret!=0:
        print('SetServoOn to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Stop Communication.
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret!=0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Close Device.
    ret = Wmx3Lib.CloseDevice()
    if ret!=0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    print('Program End.')

if __name__ == '__main__':
    main()
#End``