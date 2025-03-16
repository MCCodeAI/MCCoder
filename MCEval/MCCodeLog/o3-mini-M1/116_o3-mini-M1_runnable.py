
# Define Axes and IOs
Axes = [6, 7, 8]
IOInputs = []
IOOutputs = [6.7]


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
    path_0.fileName = f"116_o3-mini-M1_Log.txt"

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


    # Axes = [6, 7, 8]
    # IOInputs = []
    # IOOutputs = [6.7]

    # This script demonstrates multiple motion commands according to the given question:
    # 1. Move Axis 6 to position 20 using a trapezoidal profile at 900 velocity.
    # 2. Set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0.
    # 3. Move Axis 7 to position 30.
    # 4. Linearly interpolate Axes 7 and 8 to positions (40, 50).
    # 5. Start a clockwise circular interpolation motion command for Axes 6 and 7 with center (50,50) and an arc length of 360°.
    # 6. Establish a synchronous control between master Axis 6 and slave Axis 7 (via a simple E‐CAM configuration) and then move Axis 6 to position 60.
    #
    # NOTE: This example follows the code structure in the provided context.
    #       It assumes that objects such as Wmx3Lib_cm, Wmx3Lib_adv, and various command classes (e.g. Motion_PosCommand)
    #       as well as the IO interface (Wmx3Lib_cm.io) and platform-specific waiting functions are already defined.

    from time import sleep

    # ---- Step 1: Move Axis 6 to position 20 using a trapezoidal profile at 900 velocity. ----
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 20
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Error starting position command on Axis 6: ' + str(ret))
        # Optionally return or raise an exception

    # Wait for Axis 6 to stop moving.
    Wmx3Lib_cm.motion.Wait(6)


    # ---- Step 2: Set IO output bit 6.7 to 1, sleep 0.1 sec, then set it to 0 ----
    ret = Wmx3Lib_cm.io.Write(6, 7, 1)
    if ret != 0:
        print('Error setting IO output 6.7 to 1: ' + str(ret))
    sleep(0.1)
    ret = Wmx3Lib_cm.io.Write(6, 7, 0)
    if ret != 0:
        print('Error setting IO output 6.7 to 0: ' + str(ret))


    # ---- Step 3: Move Axis 7 to position 30 ----
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 7
    posCommand.target = 30
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Error starting position command on Axis 7: ' + str(ret))
    Wmx3Lib_cm.motion.Wait(7)


    # ---- Step 4: Linearly interpolate Axes 7 and 8 to positions (40, 50) ----
    linIntplCommand = Motion_LineIntplCommand()
    # Set the interpolation axes
    linIntplCommand.SetAxis(0, 7)
    linIntplCommand.SetAxis(1, 8)
    # Set target positions for Axis 7 and 8 respectively.
    linIntplCommand.SetTargetPos(0, 40)
    linIntplCommand.SetTargetPos(1, 50)
    # Configure the motion profile.
    linIntplCommand.profile.type = ProfileType.Trapezoidal
    linIntplCommand.profile.velocity = 900
    linIntplCommand.profile.acc = 1000
    linIntplCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartLineIntplPos(linIntplCommand)
    if ret != 0:
        print('Error starting linear interpolation for Axes 7 and 8: ' + str(ret))
    # Wait until both Axis 7 and Axis 8 finish the motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 7)
    axisSel.SetAxis(1, 8)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Error waiting for linear interpolation to complete: ' + str(ret))


    # ---- Step 5: Start clockwise circular interpolation for Axes 6 and 7 with center (50,50) and arc length 360 ----
    circCommand = Motion_CircIntplCommand()
    circCommand.SetAxis(0, 6)
    circCommand.SetAxis(1, 7)
    circCommand.SetCenterPos(0, 50)
    circCommand.SetCenterPos(1, 50)
    circCommand.arcLengthDegree = 360
    # 1 indicates clockwise motion.
    circCommand.clockwise = 1
    # Set the motion profile.
    circCommand.profile.type = ProfileType.Trapezoidal
    circCommand.profile.velocity = 900
    circCommand.profile.acc = 1000
    circCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartCircIntplPos(circCommand)
    if ret != 0:
        print('Error starting circular interpolation for Axes 6 and 7: ' + str(ret))
    # Wait until both Axis 6 and Axis 7 complete the motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 6)
    axisSel.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Error waiting for circular interpolation to complete: ' + str(ret))


    # ---- Step 6: Establish synchronous control between master Axis 6 and slave Axis 7, then move Axis 6 to position 60 ----
    # Configure a simple E-CAM table to provide synchronous control.
    syncECAM = AdvSync_ECAMData()
    ecOptions = AdvSync_ECAMOptions()
    ecOptions.type = AdvSync_ECAMType.Repeat
    ecOptions.source.type = AdvSync_ECAMSourceType.MasterCommandPos
    ecOptions.clutch.type = AdvSync_ECAMClutchType.PyNone
    ecOptions.clutch.simpleCatchUpVelocity = 1000
    ecOptions.clutch.simpleCatchUpAcc = 10000

    syncECAM.masterAxis = 6
    syncECAM.slaveAxis = 7
    # For a simple synchronous control, define a minimal table with two points.
    syncECAM.numPoints = 2
    syncECAM.options = ecOptions

    syncECAM.SetMasterPos(0, 0)
    syncECAM.SetSlavePos(0, 0)
    syncECAM.SetMasterPos(1, 60)
    syncECAM.SetSlavePos(1, 60)

    ret = Wmx3Lib_adv.advSync.StartECAM(0, syncECAM)
    if ret != 0:
        print('Error starting synchronous (E-CAM) control between Axis 6 and Axis 7: ' + str(ret))
        # Optionally return or raise an exception

    # Now move the master Axis 6 to position 60 under synchronous control.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 60
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Error starting synchronized motion for Axis 6: ' + str(ret))
    Wmx3Lib_cm.motion.Wait(6)

    # Stop the synchronous (E-CAM) control.
    ret = Wmx3Lib_adv.advSync.StopECAM(0)
    if ret != 0:
        print('Error stopping synchronous (E-CAM) control: ' + str(ret))


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

