
# Define Axes
Axes = [0, 1, 2]


#WMX3 python library
from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    print('Program begin.')
    sleep(0.1)

    # Create devices. 
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret!=0:
        print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Set Device Name.
    Wmx3Lib.SetDeviceName('WMX3initTest')

    # Start Communication.
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret!=0:
        print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Import and set all the preset motion parameters.
    ret=Wmx3Lib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
    if ret != 0:
        print('ImportAndSetAll Parameters error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    sleep(0.5)
 
    # Clear alarms, set servos on, and perform homing for Axes
    for axis in Axes:
        # Clear the amplifier alarm
        timeoutCounter = 0
        while True:
            # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if not CmStatus.GetAxesStatus(axis).ampAlarm:
                break
            ret = Wmx3Lib_cm.axisControl.ClearAmpAlarm(axis)
            sleep(0.5)
            timeoutCounter += 1
            if timeoutCounter > 5:
                break
        if timeoutCounter > 5:
            print(f'Clear axis {axis} alarm fails!')
            return

        # Set servo on for Axis
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 1)
        timeoutCounter = 0
        while True:
            # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if (CmStatus.GetAxesStatus(axis).servoOn):
                break
            sleep(0.4)
            timeoutCounter += 1
            if (timeoutCounter > 5):
                break
        if (timeoutCounter > 5):
            print('Set servo on for axis {axis} fails!')
            return

        # Sleep is a must between SetServoOn and Homing
        sleep(0.1)

        # Homing
        homeParam = Config_HomeParam()
        ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
        homeParam.homeType = Config_HomeType.CurrentPos

        # SetHomeParam -> First return value: Error code, Second return value: param error
        ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)

        ret = Wmx3Lib_cm.home.StartHome(axis)
        if ret != 0:
            print(f'StartHome error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        Wmx3Lib_cm.motion.Wait(axis)

    # <log ---------------------------------------------------------------------------                                                                 
    WMX3Log = Log(Wmx3Lib)
                                 
    # Stop log just in case logging is on.
    ret = WMX3Log.StopLog(0)
    sleep(0.01)
                                     
    axislist = Axes                           
    num = len(axislist)

    # Set Axis numbers and control variables of log
    cmLogIn_0 = CoreMotionLogInput()
    cmLogIn_0.axisSelection.axisCount = num
    for i in range(0, num):
        cmLogIn_0.axisSelection.SetAxis(i, axislist[i])

    # Control variables to log
    cmLogIn_0.axisOptions.commandPos = 1
    cmLogIn_0.axisOptions.feedbackPos = 0
    cmLogIn_0.axisOptions.commandVelocity = 0
    cmLogIn_0.axisOptions.feedbackVelocity = 0

    # Set up log time
    option = LogChannelOptions()
    option.samplingPeriodInCycles = 1
    option.samplingTimeMilliseconds = 1000000
    option.precision = 3

    ret=WMX3Log.SetLogOption(0, option)
    if ret!=0:
        print('SetLogOption error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)
    ret = WMX3Log.SetCustomLog(0,cmLogIn_0)
    if ret!=0:
        print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)

    # Set log file address
    path_0 = LogFilePath()
    WMX3Log.GetLogFilePath(0)
    path_0.dirPath = "C:\\"
    path_0.fileName = f"43_MCEval_SampleCode_Log.txt"
    ret = WMX3Log.SetLogFilePath(0, path_0)
    if ret!=0:
        print('SetLogFilePath error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return

    # Start log
    ret = WMX3Log.StartLog(0)
    if ret!=0:
        print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.01)
    # log> ---------------------------------------------------------------------------   


# Write python code to Execute a 3D path interpolation of Axis 0, 1, and 2 with velocity 200. There are 21 segments. 1)Linear interpolation to (90,0,0); 2)Circular interpolation to (100,10,0) with center (97.071,10-7.071,0); 3)Linear interpolation to (100,90,0); 4)Circular interpolation to (90,100,0) with center (97.071,97.071,0); 5)Linear interpolation to (10,100,0); 6)Circular interpolation to (0,90,0) with center (10-7.071,97.071,0); 7)Linear interpolation to (0,0,0); 8)Linear interpolation to (90,0,0); 9)Circular interpolation to (100,0,-10) with center (97.071,0,-10+7.071); 10)Linear interpolation to (100,0,-90); 11)Circular interpolation to (90,0,-100) with center (97.071,0,-97.071); 12)Linear interpolation to (10,0,-100); 13)Circular interpolation to (0,0,-90) with center (10-7.071,0,-97.071); 14)Linear interpolation to (0,0,0); 15)Linear interpolation to (0,90,0);  16)Circular interpolation to (0,100,-10) with center (0,97.071,-10+7.071); 17)Linear interpolation to (0,100,-90); 18)Circular interpolation to (0,90,-100) with center (0,97.071,-97.071); 19)Linear interpolation to (0,10,-100); 20)Circular interpolation to (0,0,-90) with center (0,10-7.071,-97.071); 21)Linear interpolation to (0,0,0).
    # Axes = [0, 1, 2]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntpl3DCommand()

    path.SetAxis(0, 0)
    path.SetAxis(1, 1)
    path.SetAxis(2, 2)

    # Use single motion profile for entire path
    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 200
    profile.acc = 2000
    profile.dec = 2000
    path.SetProfile(0, profile)

    # Define linear and circular segments
    path.numPoints = 21

    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 90)
    path.SetTarget(1, 0, 0)
    path.SetTarget(2, 0, 0)

    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, 100)
    path.SetTarget(1, 1, 10)
    path.SetTarget(2, 1, 0)
    path.SetCircleIntermediateTarget(0, 1, 97.071)
    path.SetCircleIntermediateTarget(1, 1, 10 - 7.071)
    path.SetCircleIntermediateTarget(2, 1, 0)

    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 100)
    path.SetTarget(1, 2, 90)
    path.SetTarget(2, 2, 0)

    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, 90)
    path.SetTarget(1, 3, 100)
    path.SetTarget(2, 3, 0)
    path.SetCircleIntermediateTarget(0, 3, 97.071)
    path.SetCircleIntermediateTarget(1, 3, 97.071)
    path.SetCircleIntermediateTarget(2, 3, 0)

    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 10)
    path.SetTarget(1, 4, 100)
    path.SetTarget(2, 4, 0)

    path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 5, 0)
    path.SetTarget(1, 5, 90)
    path.SetTarget(2, 5, 0)
    path.SetCircleIntermediateTarget(0, 5, 10 - 7.071)
    path.SetCircleIntermediateTarget(1, 5, 97.071)
    path.SetCircleIntermediateTarget(2, 5, 0)

    path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 6, 0)
    path.SetTarget(1, 6, 0)
    path.SetTarget(2, 6, 0)

    path.SetType(7, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 7, 90)
    path.SetTarget(1, 7, 0)
    path.SetTarget(2, 7, 0)

    path.SetType(8, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 8, 100)
    path.SetTarget(1, 8, 0)
    path.SetTarget(2, 8, -10)
    path.SetCircleIntermediateTarget(0, 8, 97.071)
    path.SetCircleIntermediateTarget(1, 8, 0)
    path.SetCircleIntermediateTarget(2, 8, -(10 - 7.071))

    path.SetType(9, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 9, 100)
    path.SetTarget(1, 9, 0)
    path.SetTarget(2, 9, -90)

    path.SetType(10, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 10, 90)
    path.SetTarget(1, 10, 0)
    path.SetTarget(2, 10, -100)
    path.SetCircleIntermediateTarget(0, 10, 97.071)
    path.SetCircleIntermediateTarget(1, 10, 0)
    path.SetCircleIntermediateTarget(2, 10, -97.071)

    path.SetType(11, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 11, 10)
    path.SetTarget(1, 11, 0)
    path.SetTarget(2, 11, -100)

    path.SetType(12, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 12, 0)
    path.SetTarget(1, 12, 0)
    path.SetTarget(2, 12, -90)
    path.SetCircleIntermediateTarget(0, 12, 10 - 7.071)
    path.SetCircleIntermediateTarget(1, 12, 0)
    path.SetCircleIntermediateTarget(2, 12, -97.071)

    path.SetType(13, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 13, 0)
    path.SetTarget(1, 13, 0)
    path.SetTarget(2, 1, 0)

    path.SetType(14, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 14, 0)
    path.SetTarget(1, 14, 90)
    path.SetTarget(2, 14, 0)

    path.SetType(15, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 15, 0)
    path.SetTarget(1, 15, 100)
    path.SetTarget(2, 15, -10)
    path.SetCircleIntermediateTarget(0, 15, 0)
    path.SetCircleIntermediateTarget(1, 15, 97.071)
    path.SetCircleIntermediateTarget(2, 15, -(10 - 7.071))

    path.SetType(16, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 16, 0)
    path.SetTarget(1, 16, 100)
    path.SetTarget(2, 16, -90)

    path.SetType(17, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 17, 0)
    path.SetTarget(1, 17, 90)
    path.SetTarget(2, 17, -100)
    path.SetCircleIntermediateTarget(0, 17, 0)
    path.SetCircleIntermediateTarget(1, 17, 97.071)
    path.SetCircleIntermediateTarget(2, 17, -97.071)

    path.SetType(18, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 18, 0)
    path.SetTarget(1, 18, 10)
    path.SetTarget(2, 18, -100)

    path.SetType(19, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 19, 0)
    path.SetTarget(1, 19, 0)
    path.SetTarget(2, 19, -90)
    path.SetCircleIntermediateTarget(0, 19, 0)
    path.SetCircleIntermediateTarget(1, 19, 10 - 7.071)
    path.SetCircleIntermediateTarget(2, 19, -97.071)

    path.SetType(20, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 20, 0)
    path.SetTarget(1, 20, 0)
    path.SetTarget(2, 20, 0)

    ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
    if ret != 0:
        print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
    

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 3
    axes.SetAxis(0, 0)
    axes.SetAxis(1, 1)
    axes.SetAxis(2, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return



# <log --------------------------------------------------------------------------- 
    sleep(0.1)                                                                    
    # Stop log
    ret = WMX3Log.StopLog(0)
    if ret!=0:
        print('StopLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return

    for axisNo in axislist:                                
        ret = Wmx3Lib_cm.home.StartHome(axisNo)
        if ret!=0:
            print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        Wmx3Lib_cm.motion.Wait(axisNo)                                                                  
    # log> ---------------------------------------------------------------------------     
                                     
                
    # Set servo off for Axes
    for axis in Axes:
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
        if ret != 0:
            print(f'SetServoOn to off error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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

