
# Define Axes and IOs
Axes = [10, 12]
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M3"
    path_0.fileName = f"164_o3-mini-M3_Log.txt"

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


    # Axes = [10, 12]
    # IOInputs = []
    # IOOutputs = []

    #-------------------------------------------------------------------
    # Step 1:
    # Start an absolute position command for Axis 10 to move to position 800
    # with a velocity of 600.
    #-------------------------------------------------------------------

    posCmd = Motion_PosCommand()
    posCmd.axis = 10
    posCmd.target = 800
    posCmd.profile.type = ProfileType.Trapezoidal
    posCmd.profile.velocity = 600
    posCmd.profile.acc = 10000
    posCmd.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCmd)
    if ret != 0:
        print("Error in StartPos for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until Axis 10 stops moving.
    axisSel = AxisSelection()
    axisSel.axisCount = 1
    axisSel.SetAxis(0, 10)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Error in Wait_AxisSel for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
        exit()

    #-------------------------------------------------------------------
    # Step 2:
    # Execute an absolute triggered position command for Axis 10.
    # When the remaining distance (to the current target) becomes 200,
    # trigger Axis 10 to move to position 300 with a velocity of 1000.
    # Do not use an axis wait in the middle of this continuous motion.
    #-------------------------------------------------------------------

    trigCmd = Motion_TriggerPosCommand()
    trigCmd.axis = 10
    trigCmd.target = 300
    trigCmd.profile.type = ProfileType.Trapezoidal
    trigCmd.profile.velocity = 1000
    trigCmd.profile.acc = 10000
    trigCmd.profile.dec = 10000

    trigger = Trigger()
    trigger.triggerAxis = 10
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 200
    trigCmd.trigger = trigger

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCmd)
    if ret != 0:
        print("Error in StartPos_Trigger for Axis 10:", Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # (No axis wait here since the triggered command is part of a continuous motion.)

    #-------------------------------------------------------------------
    # Step 3:
    # Set an event so that when Axis 10 reaches the position of 400,
    # it triggers the movement of Axis 12 to position 80.
    # Use wait(axis) for this event-driven motion.
    #-------------------------------------------------------------------

    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()

    # Configure the event input: trigger when Axis 10 equals position 400.
    eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN_Motion.equalPos.axis = 10
    eventIN_Motion.equalPos.pos = 400

    # Configure the event output: start an absolute position command for Axis 12.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 12
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = 80
    eventOut_Motion.startSinglePos.velocity = 600
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    # Use event ID 0.
    posEventID = 0
    ret, eventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
    if ret != 0:
        print("Error in SetEvent_ID:", ret)
        exit()

    Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)
    sleep(0.01)  # brief delay to ensure event is enabled

    # At this point, when Axis 10 reaches position 400 the event will fire,
    # and the motion command for Axis 12 will be executed.

    # Wait for Axis 12 to complete its motion.
    axisSel2 = AxisSelection()
    axisSel2.axisCount = 1
    axisSel2.SetAxis(0, 12)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel2)
    if ret != 0:
        print("Error in Wait_AxisSel for Axis 12:", Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Optionally remove the event after the motion has completed.
    ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
    if ret != 0:
        print("Error in RemoveEvent:", ret)
        exit()


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

