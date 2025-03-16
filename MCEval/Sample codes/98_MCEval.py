# Write Python code to perform a soft landing, or torque control.

# WMX3 python library
from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)
class WMX3SoftLand():
    def __init__(self):
        self.wmxApi = WMX3Api()
        self.Wmx3Lib_buf = ApiBuffer(self.wmxApi)
        self.Wmx3Lib_cm = CoreMotion(self.wmxApi)
        self.ApiBuffstu = ApiBufferStatus()
        self.Opsta = ApiBufferOptions()
    def SoftLandInit(self,channel):
        # Create devices.
        ret=self.wmxApi.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)
        if ret!=0:
            return  ret
        sleep(0.1)
        #  Free the buffer of the specified channel.
        ret = self.Wmx3Lib_buf.FreeApiBuffer(channel)
        sleep(0.01)
        # Create a buffer for the specified channel.
        ret = self.Wmx3Lib_buf.CreateApiBuffer(channel, 1024 * 1024 * 3)
        if ret != 0:
            return ret

    def SoftLandClose(self,channel):
        self.Wmx3Lib_buf.FreeApiBuffer(channel)
        self.wmxApi.CloseDevice()

    def GetApiBufferStu(self,channel):
        ret,self.ApiBuffstu= self.Wmx3Lib_buf.GetStatus(channel)
        return  self.ApiBuffstu.remainingBlockCount
    def SoftLandApibufferData(self,channel,axis,StartPoint,SlowVelPoint,TargetPoint,FastVel,SlowVel,Acc,Trqlimit,SleepTime):
        self.Wmx3Lib_buf.Halt(channel)
        sleep(0.01)
        self.Wmx3Lib_buf.Clear(channel)
        sleep(0.01)
        # Start recording for the specified channel.
        self.Wmx3Lib_buf.StartRecordBufferChannel(0)
        # Create a command value.
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = axis
        posCommand.target = StartPoint
        posCommand.profile.velocity = FastVel
        posCommand.profile.acc = Acc
        posCommand.profile.dec = Acc
        # Run to the starting position.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait for the movement to be completed.
        self.Wmx3Lib_buf.Wait(axis)
        posCommand.target = SlowVelPoint
        posCommand.profile.velocity = FastVel
        posCommand.profile.endVelocity = SlowVel
        # Run at high speed to the low-speed point, and set the end speed equal to the low speed.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait for the movement to be completed.
        self.Wmx3Lib_buf.Wait(axis)
        # Torque limit value written.
        self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis,Trqlimit)
      # self.Wmx3Lib_cm.torque.SetNegativeTrqLimit(axis,Trqlimit)
      # self.Wmx3Lib_cm.torque.SetPositiveTrqLimit(axis,Trqlimit)
        posCommand.target = TargetPoint
        posCommand.profile.velocity = SlowVel
        posCommand.profile.startingVelocity = SlowVel
        posCommand.profile.endVelocity = 0
        # Run to the target point at low speed.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait for the movement to be completed.
        self.Wmx3Lib_buf.Wait(axis)
        # Delay
        self.Wmx3Lib_buf.Sleep(SleepTime*1000)

        # Raise the process.
        posCommand.target = SlowVelPoint
        posCommand.profile.velocity = SlowVel
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = FastVel
        # Run at low speed to the deceleration point first.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait for the movement to be completed.
        self.Wmx3Lib_buf.Wait(axis)
        # Torque restriction is lifted
        self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis, 300)
        # self.Wmx3Lib_cm.torque.SetNegativeTrqLimit(axis,300)
        # self.Wmx3Lib_cm.torque.SetPositiveTrqLimit(axis,300)
        posCommand.target = StartPoint
        posCommand.profile.velocity = FastVel
        posCommand.profile.startingVelocity = FastVel
        posCommand.profile.endVelocity = 0
        # Run to the start point at high speed.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait for the movement to be completed.
        self.Wmx3Lib_buf.Wait(axis)
        # End Recording.
        self.Wmx3Lib_buf.EndRecordBufferChannel()
        # When this option is FALSE, the API buffer will continue execution when an API returns an error. When this option is TRUE, the API buffer will stop execution when an API returns an error. Execution may be resumed using the Execute function.
        self.Opsta.stopOnLastBlock = True
        # When this option is FALSE, the API buffer will remain in Active state after the last API in the buffer is executed. When another API is added to the buffer, it is immediately executed. When this option is TRUE, the API buffer will change to the Stop state when the last API in the buffer is executed as if the Halt function is called. When another API is added to the buffer, it will not be executed until the Execute function is called.
        self.Opsta.stopOnError = True
        # When this option is FALSE, the API buffer will wait for additional API functions to be entered into the buffer when the buffer becomes empty. When this option is TRUE, the API buffer will rewind when the buffer becomes empty and continue execution from the first API in the buffer. This option will not rewind the buffer when the first API in the buffer has been overwritten by an API that is added later.
        self.Opsta.autoRewind = False
        self.Wmx3Lib_buf.SetOptions(channel,self.Opsta)

    def SoftLandMovStarPoint(self,axis,StartPoint,SlowVelPoint,FastVel,SlowVel,Acc):
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = axis
        posCommand.profile.velocity = SlowVel
        posCommand.profile.acc = Acc
        posCommand.profile.dec = Acc
        posCommand.target = SlowVelPoint
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = FastVel
        # Execute command to move to a specified absolute position.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        self.Wmx3Lib_cm.Wait(axis)
        self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis, 300)
        # self.Wmx3Lib_cm.torque.SetNegativeTrqLimit(axis,300)
        # self.Wmx3Lib_cm.torque.SetPositiveTrqLimit(axis,300)
        posCommand.target = StartPoint
        posCommand.profile.velocity = FastVel
        posCommand.profile.startingVelocity = FastVel
        posCommand.profile.endVelocity = 0
        # Execute command to move to a specified absolute position.
        self.Wmx3Lib_cm.motion.StartPos(posCommand)
        self.Wmx3Lib_cm.Wait(axis)
    def SoftLandStart(self,channel):
        ret=self.Wmx3Lib_buf.Execute(channel)
        return ret

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    Wmx_Softland= WMX3SoftLand()
    print('Program begin.')
    sleep(1)

    # Create devices.
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret!=0:
        print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    # Set Device Name.
    Wmx3Lib.SetDeviceName('ApiBufferMotion')
    #AxisId
    axis = 0
    # Start Communication.
    timeoutCounter=0
    for i in range(100):
        ret = Wmx3Lib.StartCommunication(INFINITE)
        if ret != 0:
            print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.engineState==EngineState.Communicating):
            break

    # Import and set all the preset motion parameters.
    ret=Wmx3Lib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
    if ret != 0:
        print('ImportAndSetAll Parameters error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    sleep(0.5)

    ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 1)
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(axis).servoOn):
            break
        sleep(0.1)
        # Homing
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeType = Config_HomeType.CurrentPos
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)

    ret = Wmx3Lib_cm.home.StartHome(axis)
    if ret != 0:
        print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(axis)

    ret = Wmx_Softland.SoftLandInit(0)
    if ret != 0:
        print('SoftLandInit error code is ' + str(ret) )
    # Record a soft landing process with the following parameters: Starting point is 0, deceleration point is 400, target point is 500, high speed is 1000, low speed is 100, and the acceleration and deceleration are the same at 10000, with a torque limit of 30.
    Wmx_Softland.SoftLandApibufferData(0,axis,0,400,500,1000,100,10000,30,2)
    ret = Wmx_Softland.SoftLandStart(0)
    if ret != 0:
        print('SoftLandStart error code is ' + str(ret) )
    while True:
        cutter = Wmx_Softland.GetApiBufferStu(0)
        if (cutter<=0):
            break
        sleep(0.01)
    Wmx3Lib_cm.motion.Wait(axis)

    Wmx_Softland.SoftLandClose(0)
    # Set servo off.
    ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
    if ret != 0:
        print('SetServoOn to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

    # Stop Communication.
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret != 0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    # Close Device.
    ret = Wmx3Lib.CloseDevice()
    if ret != 0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

    print('Program End.')

if __name__ == '__main__':
    main()
