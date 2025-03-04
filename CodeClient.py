import socket

def SendCode(code_data_raw):
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    server_addr = ("10.211.55.5", 8888)  #("115.236.153.172", 50871)  10.211.55.5
    tcp_socket.connect(server_addr)

    #Python code test
    Codetest='''
print("Destiny is all!")
import time
#time.sleep(3)
print(\"Bravo!\")
raise Exception("0: Return something!")
    '''

    Codetest='''
#*****************************************************************************#
#* FILE        : MotorControl.Py                                             *# 
#* DESCRIPTION : Sample from Device Creation to Communication Establishment. *#
#*****************************************************************************#

# E:\\wmxai\\WMX3Test3.11\\venv\\wmx3_test.py
print("start main2")




#*****************************************************************************#
# Function                                                                    #
#*****************************************************************************#

#-----------------------------------------------------------------------------#
# Function    : main                                                          #
# Description : Main Function.                                                #
#-----------------------------------------------------------------------------#

from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)

#def main():

print("in main")

Wmx3Lib    = WMX3Api()
CmStatus   = CoreMotionStatus()
Wmx3Lib_cm = CoreMotion(Wmx3Lib)
adv = AdvancedMotion(Wmx3Lib)
Wmx3Lib_Io = Io(Wmx3Lib)
ret        = 345

print('Program Start.')
sleep(0.1)

# Create devices.
ret=Wmx3Lib.CreateDevice('C:\Program Files\SoftServo\WMX3', DeviceType.DeviceTypeNormal, INFINITE)    
print(str(ret) + ":createDe")

# Set Device Name.
ret=Wmx3Lib.SetDeviceName('MotorControl')
print(str(ret) + ":SetDeviceName")


# Start Communication.
ret = Wmx3Lib.StartCommunication(INFINITE)
print(str(ret) + ":StartCommunication")

# Set servo on.
ret=Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
print(str(ret) + ":SetServoOn")
while True:
    
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (CmStatus.GetAxesStatus(0).servoOn):
        break
    sleep(0.1)

# Homing.
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(0)
homeParamError = Config_HomeParam()
homeParam.homeType = Config_HomeType.CurrentPos

    
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(0, homeParam)

Wmx3Lib_cm.home.StartHome(0)
Wmx3Lib_cm.motion.Wait(0)

# --------------------------------------------------------------------------
# Create a command value.
# --------------------------------------------------------------------------
posCommand                          = Motion_PosCommand()
posCommand.profile.type             = ProfileType.Trapezoidal
posCommand.axis                     = 0;
posCommand.target                   = -100
posCommand.profile.velocity         = 1000
posCommand.profile.acc              = 100000
posCommand.profile.dec              = 100000

# --------------------------------------------------------------------------
# Execute command to move from current position to specified position.
# --------------------------------------------------------------------------
ret=Wmx3Lib_cm.motion.StartMov(posCommand)
print(ret)

# --------------------------------------------------------------------------
# Wait until the axis moves to the target position and stops.
# --------------------------------------------------------------------------
Wmx3Lib_cm.motion.Wait(0)

jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.Trapezoidal
jogCommand.axis = 0
jogCommand.profile.velocity = 100
jogCommand.profile.acc = 100000
jogCommand.profile.dec = 100000

# Rotate the motor at the specified speed.
ret =Wmx3Lib_cm.motion.StartJog(jogCommand)
print(ret)

sleep(0.1)


Wmx3Lib_cm.motion.Stop(0)

# Set servo off.
Wmx3Lib_cm.axisControl.SetServoOn(0, 0)

# sleep(1)

Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
Wmx3Lib_cm.axisControl.SetServoOn(1, 1)
sleep(0.1)
path = AdvMotion_PathIntplCommand()

path.SetAxis(0, 0)
path.SetAxis(1, 1)

path.enableConstProfile = 1

path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1000
path.profile.acc = 100000
path.profile.dec = 100000

path.numPoints = 8

path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)

path.SetTarget(0, 0, -200)
path.SetTarget(1, 0, -200)

path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 1, -150)
path.SetTarget(1, 1, -200)
path.SetCenterPos(0, 1, 0)
path.SetCenterPos(1, 1, 0)
path.SetDirection(1, 1)

path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, -180)
path.SetTarget(1, 2, -10)

path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 3, -10)
path.SetTarget(1, 3, -150)
path.SetCenterPos(0, 3, 0)
path.SetCenterPos(1, 3, 0)
path.SetDirection(3, 1)

path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, 0)
path.SetTarget(1, 4, -100)

path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 5, -50)
path.SetTarget(1, 5, -100)
path.SetCenterPos(0, 5, 0)
path.SetCenterPos(1, 5, 0)
path.SetDirection(5, 1)

path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 6, -50)
path.SetTarget(1, 6, 50)

path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
path.SetTarget(0, 7, 0)
path.SetTarget(1, 7, 0)
path.SetCenterPos(0, 7, 0)
path.SetCenterPos(1, 7, 0)
path.SetDirection(7, 1)

ret = adv.advMotion.StartPathIntplPos(path)
print(ret)
Wmx3Lib_cm.motion.Wait(0)

Wmx3Lib_Io.SetOutBit(0x0, 0x00, 0x01)
sleep(1)
Wmx3Lib_Io.SetOutBit(0x0, 0x00, 0x00)
# while True:
#     ret, CmStatus = Wmx3Lib_cm.GetStatus()
#     if (not CmStatus.GetAxesStatus(0).servoOn):
#         break
#     sleep(0.1)

# ----------------------
# Stop Communication.
# ----------------------
Wmx3Lib.StopCommunication(INFINITE)

# Close Device.
Wmx3Lib.CloseDevice()

print('Program End.')
sleep(0.1)
#return 0
    
# if __name__ == '__main__':
#     main()

# print("before main")
# main()
    '''




    Codetest='''

 
"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<SAMPLE CODE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
This is a typical example of a WMX3 script from initialization, through motion execution, to termination/closing/shutting down. The Python script initializes and operates a motion control system using the WMX3 software library, sequentially executing steps for robust control in an industrial setting. It starts by creating and naming a device with `CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)` and `SetDeviceName('WMX3initTest')`, then begins communication with `StartCommunication(INFINITE)`. The script clears any amplifier alarms with `ClearAmpAlarm(axis)` and activates the servo with `SetServoOn(axis, 1)`. It executes a motion command using `StartMov(posCommand)` and concludes by shutting down the servo and stopping communication with `SetServoOn(axis, 0)` and `StopCommunication(INFINITE)`. This structured approach ensures each component is correctly set up and terminated, ensuring safe and effective system operations.
"""
 
 

#WMX3 python library
from WMX3ApiPython import *
from time import *


INFINITE = int(0xFFFFFFFF)


def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    ret = 0
    print('Program begin.')
    sleep(1)

    # Create devices.
    Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)

    # Set Device Name.
    Wmx3Lib.SetDeviceName('WMX3initTest')

    # Start Communication.
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret!=0:
        print('start communicaiton fail!')
        return 0

    #Clear every servo/motor/amplifier's alarm
    timeoutCounter=0
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (not CmStatus.GetAxesStatus(0).ampAlarm):
            break
        Wmx3Lib_cm.axisControl.ClearAmpAlarm(0)
        sleep(0.5)
        timeoutCounter=timeoutCounter+1
        if(timeoutCounter > 5):
            break
    if(timeoutCounter > 5):
        print('clear axis alarm fails!')
        return 0

    # Set servo on.
    Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).servoOn):
            break
        sleep(0.1)

    # Homing.
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(0)
    homeParamError = Config_HomeParam()
    homeParam.homeType = Config_HomeType.CurrentPos

    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(0, homeParam)

    Wmx3Lib_cm.home.StartHome(0)
    Wmx3Lib_cm.motion.Wait(0)

    # --------------------------------------------------------------------------
    # Create a command value.
    # --------------------------------------------------------------------------
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 1000
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 1000000
    posCommand.profile.dec = 1000000

    # --------------------------------------------------------------------------
    # Execute command to move from current position to specified position.
    # --------------------------------------------------------------------------
    Wmx3Lib_cm.motion.StartMov(posCommand)

    # --------------------------------------------------------------------------
    # Wait until the axis moves to the target position and stops.
    # --------------------------------------------------------------------------
    Wmx3Lib_cm.motion.Wait(0)

    # Set servo off.
    Wmx3Lib_cm.axisControl.SetServoOn(0, 0)
    while True:
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (not CmStatus.GetAxesStatus(0).servoOn):
            break
        sleep(0.1)

    # ----------------------
    # Stop Communication.
    # ----------------------
    Wmx3Lib.StopCommunication(INFINITE)

    # Close Device.
    Wmx3Lib.CloseDevice()

    print('Program End.')
    sleep(0.5)
    return 0


if __name__ == '__main__':
    main()



'''

    # 3. 发送数据
    # send_data = Codetest
    # tcp_socket.send(send_data.encode("utf-8"))

    import time
    
    send_data = code_data_raw
    tcp_socket.send(send_data.encode("utf-8"))

    time.sleep(0.1)
    send_data = 'exit'
    tcp_socket.send(send_data.encode("utf-8"))

    #4.从服务器接收数据
    tcp_remsg = tcp_socket.recv(1024) #注意这个1024byte，大小根据需求自己设置
    print(tcp_remsg.decode("utf-8"))  #如果要乱码可以使用tcp_remsg.decode("gbk")
    
    # 4. 关闭套接字
    tcp_socket.close()
    # print("end")

    return tcp_remsg.decode("utf-8")

# SendCode('code_data_raw')