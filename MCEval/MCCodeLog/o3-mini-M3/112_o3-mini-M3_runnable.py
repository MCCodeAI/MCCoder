
# Define Axes and IOs
Axes = []
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
    path_0.fileName = f"112_o3-mini-M3_Log.txt"

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


    import time

    # -------------------------------
    # 1. Record and execute an API buffer to move Axis 2 to position 150.
    # -------------------------------
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    Wmx3Lib_buf.Clear(0)
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 2
    posCommand.target = 150
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait until Axis 2 stops moving before ending the buffer recording.
    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print("Wait error code for Axis 2 is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    Wmx3Lib_buf.EndRecordBufferChannel()
    Wmx3Lib_buf.Execute(0)

    # Ensure Axis 2 has completed its motion.
    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print("Post-execute wait error for Axis 2: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # -------------------------------
    # 2. Set an event that triggers a relative move command for Axis 2.
    #    When IO Output 1.2 equals 1, move Axis 2 by 260 (relative) at 1100 velocity.
    #    Event ID is 5.
    # -------------------------------
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

    eventIN_IO = IoEventInput()
    # Correction: Use the correct IO event type for matching the bit condition.
    eventIN_IO.type = IoEventInputType.IOBit
    # Specify the I/O source: Output with byte address 1 and bit address 2 (i.e., Output 1.2).
    eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
    eventIN_IO.ioBit.byteAddress = 1
    eventIN_IO.ioBit.bitAddress = 2

    eventOut_Motion = CoreMotionEventOutput()
    # Use the multiple motion command even for a single axis.
    eventOut_Motion.type = CoreMotionEventOutputType.StartMultipleMov
    eventOut_Motion.startMultipleMov.axisCount = 1
    eventOut_Motion.startMultipleMov.SetAxis(0, 2)
    eventOut_Motion.startMultipleMov.SetType(0, ProfileType.Trapezoidal)
    eventOut_Motion.startMultipleMov.SetVelocity(0, 1100)
    # Specify acceleration/deceleration as needed.
    eventOut_Motion.startMultipleMov.SetAcc(0, 10000)
    eventOut_Motion.startMultipleMov.SetDec(0, 10000)
    eventOut_Motion.startMultipleMov.SetTarget(0, 260)

    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, 5)
    if ret != 0:
        print("SetEvent_ID error code is " + str(ret))
        exit(1)

    Wmx3Lib_EventCtl.EnableEvent(5, 1)

    # -------------------------------
    # 3. Execute linear interpolation of Axis 1 and Axis 3 to (80, 110) at 1500 velocity.
    # -------------------------------
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    lin.SetAxis(0, 1)
    lin.SetAxis(1, 3)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1500
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    lin.SetTarget(0, 80)
    lin.SetTarget(1, 110)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print("StartLinearIntplPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # -------------------------------
    # 4. Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it to 0.
    # -------------------------------
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
    if ret != 0:
        print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
        exit(1)

    time.sleep(0.2)

    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
    if ret != 0:
        print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
        exit(1)

    # -------------------------------------------------------------------
    # Additional snippet: 
    # Set output bit 0.2 to be 1, sleep for 0.15 seconds, and then set it to 0.
    # -------------------------------------------------------------------
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x00, 0x02, 0x01)
    if ret != 0:
        print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
        exit(1)

    time.sleep(0.15)

    ret = Wmx3Lib_Io.SetOutBit(0x00, 0x02, 0x00)
    if ret != 0:
        print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
        exit(1)


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

