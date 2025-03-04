
# Define Axes
Axes = [2, 3]


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
    path_0.fileName = f"11_MCEval_SampleCode_Log.txt"
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


# Write python code to Start a cubic spline motion command of Axis 2 and 3 with the total time of 1000ms to complete, the 1st point to 9th point are (0,0),(10,0),(50,50),(100,100),(100,150),(0,150),(0,100),(50,50),(7,8).
    # Axes = [2, 3]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Allocate buffer memory for a spline execution channel with 100 points for Channel 0.
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Set the spline command options, specifying Axis 0 and Axis 1, with a total time of 1,000 milliseconds to complete the spline motion.
    splineCommand = AdvMotion_TotalTimeSplineCommand()
    splineCommand.dimensionCount = 2
    splineCommand.SetAxis(0, 2)
    splineCommand.SetAxis(1, 3)
    splineCommand.totalTimeMilliseconds = 1000

    # Set the spline point data with 9 points.
    splinePoint = []

    ret, CmStatus = Wmx3Lib_cm.GetStatus()

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[0].SetPos(0, 0)
    splinePoint[0].SetPos(1, 0)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[1].SetPos(0, 10)
    splinePoint[1].SetPos(1, 0)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[2].SetPos(0, 50)
    splinePoint[2].SetPos(1, 50)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[3].SetPos(0, 100)
    splinePoint[3].SetPos(1, 100)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[4].SetPos(0, 100)
    splinePoint[4].SetPos(1, 150)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[5].SetPos(0, 0)
    splinePoint[5].SetPos(1, 150)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[6].SetPos(0, 0)
    splinePoint[6].SetPos(1, 100)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[7].SetPos(0, 50)
    splinePoint[7].SetPos(1, 50)

    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[8].SetPos(0, 7)
    splinePoint[8].SetPos(1, 8)

    # Execute the spline command.
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 9, splinePoint)
    if ret != 0:
        print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the spline motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Free buffer memory for the spline execution channel. (Normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
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

