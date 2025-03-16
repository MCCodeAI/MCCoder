
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
    path_0.fileName = f"156_o3-mini-M3_Log.txt"

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


    # -*- coding: utf-8 -*-
    # Axes = [10, 12]
    # IOInputs = []
    # IOOutputs = []

    # This script executes an absolute triggered position command for Axis 10
    # and sets an event so that when Axis 10 reaches position 100 it triggers 
    # an absolute move for Axis 12.
    #
    # The motion sequence is as follows:
    # 1. Before starting Axis 10’s move, set up an event so that when Axis 10 equals 100,
    #    Axis 12 will move to -50 (using a trapezoidal profile).
    # 2. Start Axis 10 moving to -800 at a velocity of 600.
    # 3. When the remaining distance for Axis 10 equals 200, it is triggered to move 
    #    to 300 at 1000 velocity.
    # 4. Wait until Axis 10 has finished its continuous motion.
    # 5. Then wait until the event-triggered move for Axis 12 is complete.
    # 6. Finally, clear the event.

    # --- Set up the event for Axis 12 ---

    # Create an instance of the event control object.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()

    # Choose an event ID that is not currently in use (use 2 instead of 1 to avoid conflict).
    eventID = 2

    # Configure the event input: trigger when Axis 10 equals 100.
    eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN_Motion.equalPos.axis = 10
    eventIN_Motion.equalPos.pos = 100

    # Configure the event output: when triggered, start an absolute position command for Axis 12.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 12
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = -50
    # Using a chosen velocity value for Axis 12; adjust as needed.
    eventOut_Motion.startSinglePos.velocity = 600
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    # Set the event with the chosen event ID.
    ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print("SetEvent_ID error code:", ret)
        # Depending on requirements, you might clear the old event or try a different ID.

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # --- Execute the absolute triggered position command for Axis 10 ---

    posCommand = Motion_PosCommand()
    trigPosCommand = Motion_TriggerPosCommand()

    # Configure the primary motion for Axis 10: move to -800 at velocity 600.
    posCommand.axis = 10
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 600
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    # End velocity set equal to velocity for a clean stop.
    posCommand.profile.endVelocity = 600
    posCommand.target = -800

    # Start the primary move for Axis 10.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("Axis 10 StartPos error code:", ret)
        # Handle error as needed

    # Configure the triggered motion for Axis 10: when the remaining distance equals 200,
    # trigger a move to 300 at velocity 1000.
    trigPosCommand.axis = 10
    trigPosCommand.profile.type = ProfileType.Trapezoidal
    trigPosCommand.profile.velocity = 1000
    trigPosCommand.profile.acc = 10000
    trigPosCommand.profile.dec = 10000
    trigPosCommand.target = 300
    trigPosCommand.trigger.triggerType = TriggerType.RemainingDistance
    trigPosCommand.trigger.triggerAxis = 10
    trigPosCommand.trigger.triggerValue = 200

    # Start the triggered motion command for Axis 10.
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
    if ret != 0:
        print("Axis 10 StartPos_Trigger error code:", ret)
        # Handle error as needed

    # Wait until Axis 10 has completed its motion.
    Wmx3Lib_cm.motion.Wait(10)

    # --- Wait for the event-triggered motion of Axis 12 to finish ---

    Wmx3Lib_cm.motion.Wait(12)

    # --- Clear the event now that the triggered motion is complete ---

    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("RemoveEvent error code:", ret)
        # Handle error as needed


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

