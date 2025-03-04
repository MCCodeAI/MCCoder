
# Define Axes
Axes = [0, 1]


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
    path_0.fileName = f"41_MCEval_SampleCode_Log.txt"
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


# Write python code to Execute an absolute position path interpolation motion command of Axis 0 and 1 specifying the Motion Profile for Each Segment. The 1st segment is a linear interpolation to position (100, 0) with velocity and endvelocity 1000, the 2nd segment is a clockwise circular interpolation to position (150, 50) with center point (100, 50) with velocity and endvelocity 900, the 3rd segment is a linear interpolation to position (150, 100) with velocity and endvelocity 800, the 4th segment is a clockwise circular interpolation to position (100, 150) with center point (100, 100) with velocity and endvelocity 700, the 5th segment is a linear interpolation to position (0, 150) with velocity and endvelocity 600, the 6th segment is a clockwise circular interpolation to position (-50, 100) with center point (0, 100) with velocity and endvelocity 700, the 7th segment is a linear interpolation to position (-50, 50) with velocity and endvelocity 800, the 8th segment is a clockwise circular interpolation to position (0, 0) with center point (0, 50) with velocity 900. 
    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplCommand()

    path.SetAxis(0, 0)
    path.SetAxis(1, 1)

    # Specify motion profile for each segment
    path.enableConstProfile = 0

    # Define linear and circular segments
    path.numPoints = 8

    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 100)
    path.SetTarget(1, 0, 0)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 1000
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 1000
    path.SetProfile(0, profile)

    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, 150)
    path.SetTarget(1, 1, 50)
    path.SetCenterPos(0, 1, 100)
    path.SetCenterPos(1, 1, 50)
    path.SetDirection(1, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 900
    path.SetProfile(1, profile)

    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 150)
    path.SetTarget(1, 2, 100)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(2, profile)

    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, 100)
    path.SetTarget(1, 3, 150)
    path.SetCenterPos(0, 3, 100)
    path.SetCenterPos(1, 3, 100)
    path.SetDirection(3, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(3, profile)

    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 0)
    path.SetTarget(1, 4, 150)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 600
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 600
    path.SetProfile(4, profile)

    path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 5, -50)
    path.SetTarget(1, 5, 100)
    path.SetCenterPos(0, 5, 0)
    path.SetCenterPos(1, 5, 100)
    path.SetDirection(5, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(5, profile)

    path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 6, -50)
    path.SetTarget(1, 6, 50)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(6, profile)

    path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 7, 0)
    path.SetTarget(1, 7, 0)
    path.SetCenterPos(0, 7, 0)
    path.SetCenterPos(1, 7, 50)
    path.SetDirection(5, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    path.SetProfile(7, profile)

    ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
    if ret != 0:
        print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 0)
    axes.SetAxis(1, 1)
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

