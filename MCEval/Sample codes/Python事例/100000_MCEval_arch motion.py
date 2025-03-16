#WMX3 python library
from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    print('Program begin.')
    sleep(1)

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

    # Clear alarms, set servos on, and perform homing for Axes
    for axis in [0, 1, 2, 3]:
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

    #define axes for arch motion
    axes=[0,1]
    #define four positons for arch motin. They are [0,0] [0,300] [400,300] [400,0]
    posA=[0,0]
    posB=[0,300]
    posC=[400,300]
    posD=[400,0]

    #Move to init position ,that is [0,0], with velocity of 200,and acc of 800.
    pos = Motion_PosCommand()
    pos.profile.type = ProfileType.Trapezoidal
    pos.axis = axes[0]
    pos.target = posA[0]
    pos.profile.velocity = 200
    pos.profile.acc = 800
    pos.profile.dec = 800
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    pos = Motion_PosCommand()
    pos.profile.type = ProfileType.Trapezoidal
    pos.axis = axes[1]
    pos.target = posA[1]
    pos.profile.velocity = 200
    pos.profile.acc = 800
    pos.profile.dec = 800
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion done
    Wmx3Lib_cm.motion.Wait(axes[0])
    Wmx3Lib_cm.motion.Wait(axes[1])

    #Move to position B ,that is [0,300], with velocity of 200,and acc of 800.
    pos = Motion_PosCommand()
    pos.profile.type = ProfileType.Trapezoidal
    pos.axis = axes[1]
    pos.target = posB[1]
    pos.profile.velocity = 200
    pos.profile.acc = 800
    pos.profile.dec = 800
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Trigger a Move to position C ,that is [400,300], with velocity of 200,and acc of 800. Motion start when renaimed distance of last motion be 20
    post = Motion_TriggerPosCommand()
    trigger = Trigger()
    post.profile.type = ProfileType.Trapezoidal
    post.axis = axes[0]
    post.target = posC[0]
    post.profile.velocity = 200
    post.profile.acc = 800
    post.profile.dec = 800
    trigger.triggerAxis = axes[1]
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 20
    post.trigger = trigger
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(post)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for motion done
    Wmx3Lib_cm.motion.Wait(axes[1])

    #Trigger a Move to position D ,that is [400,0], with velocity of 200,and acc of 800. Motion start when renaimed distance of last motion be 20
    post = Motion_TriggerPosCommand()
    trigger = Trigger()
    post.profile.type = ProfileType.Trapezoidal
    post.axis = axes[1]
    post.target = posD[1]
    post.profile.velocity = 200
    post.profile.acc = 800
    post.profile.dec = 800
    trigger.triggerAxis = axes[0]
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 20
    post.trigger = trigger
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(post)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion done
    Wmx3Lib_cm.motion.Wait(axes[0])
    Wmx3Lib_cm.motion.Wait(axes[1])

    sleep(2)
    
    #return back
    #Move to position C ,that is [400,300], with velocity of 200,and acc of 800.
    pos = Motion_PosCommand()
    pos.profile.type = ProfileType.Trapezoidal
    pos.axis = axes[1]
    pos.target = posC[1]
    pos.profile.velocity = 200
    pos.profile.acc = 800
    pos.profile.dec = 800
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Trigger a Move to position B ,that is [0,300], with velocity of 200,and acc of 800. Motion start when renaimed distance of last motion be 20
    post = Motion_TriggerPosCommand()
    trigger = Trigger()
    post.profile.type = ProfileType.Trapezoidal
    post.axis = axes[0]
    post.target = posB[0]
    post.profile.velocity = 200
    post.profile.acc = 800
    post.profile.dec = 800
    trigger.triggerAxis = axes[1]
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 20
    post.trigger = trigger
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(post)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for motion done
    Wmx3Lib_cm.motion.Wait(axes[1])

    #Trigger a Move to position A ,that is [0,0], with velocity of 200,and acc of 800. Motion start when renaimed distance of last motion be 20
    post = Motion_TriggerPosCommand()
    trigger = Trigger()
    post.profile.type = ProfileType.Trapezoidal
    post.axis = axes[1]
    post.target = posA[1]
    post.profile.velocity = 200
    post.profile.acc = 800
    post.profile.dec = 800
    trigger.triggerAxis = axes[0]
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 20
    post.trigger = trigger
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(post)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for motion done
    Wmx3Lib_cm.motion.Wait(axes[0])
    Wmx3Lib_cm.motion.Wait(axes[1])

    sleep(2)


    # Set servo off for Axes
    for axis in [0, 1, 2, 3]:
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