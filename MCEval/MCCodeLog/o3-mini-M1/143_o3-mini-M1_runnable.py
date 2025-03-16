
# Define Axes and IOs
Axes = [2, 10]
IOInputs = []
IOOutputs = []


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
            print(f'StartHome before log error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        Wmx3Lib_cm.motion.Wait(axis)

    # <logon---------------------------------------------------------------------------                                                                 
    WMX3Log = Log(Wmx3Lib)
                                 
    # Stop log just in case logging is on.
    ret = WMX3Log.StopLog(0)
    sleep(0.2)
                                     
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
    option.samplingTimeMilliseconds = 60000
    option.precision = 3

    ret=WMX3Log.SetLogOption(0, option)
    if ret!=0:
        print('SetLogOption error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        ret = WMX3Log.StopLog(0)
        sleep(0.2)
        ret=WMX3Log.SetLogOption(0, option)
    sleep(0.1)

    ret = WMX3Log.SetCustomLog(0,cmLogIn_0)
    if ret!=0:
        print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)

    
    # IOInputs and IOOutputs
    Inputslist = IOInputs
    Outputslist = IOOutputs

    # Initialize lists to hold IOAddress instances
    InputIOAddresses = [IOAddress() for _ in range(len(Inputslist))]
    OutputIOAddresses = [IOAddress() for _ in range(len(Outputslist))]

    # Set properties for InputIOAddresses
    for i in range(len(Inputslist)):
        integer_part, fractional_part = str(Inputslist[i]).split('.')
        InputIOAddresses[i].byte = int(integer_part)
        InputIOAddresses[i].bit = int(fractional_part)
        InputIOAddresses[i].size = 1
        inputSize = 1 #temp
        break

    # Set properties for OutputIOAddresses
    for i in range(len(Outputslist)):
        integer_part, fractional_part = str(Outputslist[i]).split('.')
        OutputIOAddresses[i].byte = int(integer_part)
        OutputIOAddresses[i].bit = int(fractional_part)
        OutputIOAddresses[i].size = 1
        outputSize = 1 #temp
        break

    if len(Inputslist) == 0:      #temp
        InputIOAddresses = [IOAddress() for _ in range(1)]
        InputIOAddresses[0].byte = 0
        InputIOAddresses[0].bit = 0
        InputIOAddresses[0].size = 1
        inputSize = 1
    if len(Outputslist) == 0:
        OutputIOAddresses = [IOAddress() for _ in range(1)]
        OutputIOAddresses[0].byte = 0
        OutputIOAddresses[0].bit = 0
        OutputIOAddresses[0].size = 1
        outputSize = 1


    # Call SetIOLog function
    ret = WMX3Log.SetIOLog(0, InputIOAddresses[0], inputSize, OutputIOAddresses[0], outputSize) 
    if ret != 0:
        print('SetIOLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
        
    # Set log file address
    path_0 = LogFilePath()
    WMX3Log.GetLogFilePath(0)
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M1"
    path_0.fileName = f"143_o3-mini-M1_Log.txt"

    ret = WMX3Log.SetLogFilePath(0, path_0)
    if ret!=0:
        print('SetLogFilePath error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return


    # Start log
    ret = WMX3Log.StartLog(0)
    if ret!=0:
        print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)
    # --------------------------------------------------------------------------- 
    # logon>  


    # Axes = [2, 10]
    # IOInputs = []
    # IOOutputs = []

    #----------------------------------------------------------------------
    # This script executes an absolute triggered position command:
    # 1. Axis 10 is commanded to move to -1000 with a velocity of 600.
    # 2. When the remaining distance for Axis 10 reaches 500, a triggered command
    #    starts to move Axis 10 to -300 with a velocity of 1000.
    # 3. An event is set so that when Axis 10 reaches the absolute position 100,
    #    a motion command is triggered to move Axis 2 to -200 with a velocity of 1000.
    #
    # The script waits for the axis motion to complete after each separate motion.
    #----------------------------------------------------------------------

    # ----- Absolute motion command for Axis 10 -----
    posCmd = Motion_PosCommand()
    posCmd.axis = 10
    posCmd.profile.type = ProfileType.Trapezoidal
    posCmd.profile.velocity = 600
    posCmd.profile.acc = 10000
    posCmd.profile.dec = 10000
    posCmd.profile.endVelocity = 600
    posCmd.target = -1000

    ret = Wmx3Lib_cm.motion.StartPos(posCmd)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        # Early exit if error encountered.
    else:
        # Wait until Axis 10 stops before starting the trigger command.
        Wmx3Lib_cm.motion.Wait(10)


    # ----- Triggered motion command for Axis 10 -----
    trigCmd = Motion_TriggerPosCommand()
    trigCmd.axis = 10
    trigCmd.profile.type = ProfileType.Trapezoidal
    trigCmd.profile.velocity = 1000
    trigCmd.profile.acc = 10000
    trigCmd.profile.dec = 10000
    trigCmd.target = -300
    # Set the trigger to start when the remaining distance on Axis 10 reaches 500
    trigCmd.trigger.triggerType = TriggerType.RemainingDistance
    trigCmd.trigger.triggerAxis = 10
    trigCmd.trigger.triggerValue = 500

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCmd)
    if ret != 0:
        print("StartPos_Trigger error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        # Early exit if error encountered.
    else:
        # Wait until Axis 10 completes its triggered motion.
        Wmx3Lib_cm.motion.Wait(10)


    # ----- Set an event to trigger a motion command for Axis 2 -----
    # The event will trigger when Axis 10 reaches the absolute position of 100.

    # Configure the event input to monitor Axis 10 position equals 100.
    eventIN_Motion = CoreMotionEventInput()
    eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN_Motion.equalPos.axis = 10
    eventIN_Motion.equalPos.pos = 100

    # Configure the event output to start an absolute position command on Axis 2.
    eventOut_Motion = CoreMotionEventOutput()
    eventOut_Motion.type = CoreMotionEventOutputType.StartPos
    # Assuming that the StartPos command parameters are provided within the event output structure.
    eventOut_Motion.startPos.axis = 2
    eventOut_Motion.startPos.profile.type = ProfileType.Trapezoidal
    eventOut_Motion.startPos.profile.velocity = 1000
    eventOut_Motion.startPos.profile.acc = 10000
    eventOut_Motion.startPos.profile.dec = 10000
    eventOut_Motion.startPos.profile.endVelocity = 1000
    eventOut_Motion.startPos.target = -200

    # Define an event ID for registration.
    eventID = 0

    ret, regEventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print("SetEvent_ID error code is " + str(ret))
    else:
        # Enable the event so that it becomes active.
        Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # Wait until both Axis 10 and Axis 2 finish their motions.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 10)
    axisSel.SetAxis(1, 2)

    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

    # Optionally, remove the event after it has been triggered.
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("RemoveEvent error code is " + str(ret) + ": " + Wmx3Lib.ErrorToString(ret))


# <logoff --------------------------------------------------------------------------- 
    sleep(0.1)                                                                    
    # Stop log
    ret = WMX3Log.StopLog(0)
    if ret!=0:
        print('StopLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))       
    sleep(0.1) 

    # for axisNo in axislist:                                
    #     ret = Wmx3Lib_cm.home.StartHome(axisNo)
    #     if ret!=0:
    #         print('StartHome after log error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            
    #     Wmx3Lib_cm.motion.Wait(axisNo)      
    #  -----------------------------------                                   
    # logoff>    
                                     
                
    # Set servo off for Axes
    for axis in Axes:
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
        if ret != 0:
            print(f'SetServoOn to off error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            

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

