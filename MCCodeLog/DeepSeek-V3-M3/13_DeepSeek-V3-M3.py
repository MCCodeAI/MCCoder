
from WMX3ApiPython import *
from time import sleep

# Initialize the WMX3 API
Wmx3Lib = WMX3Api()
Wmx3Lib_cm = CoreMotion(Wmx3Lib)

# Create devices.
ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
if ret != 0:
    print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# Start Communication.
ret = Wmx3Lib.StartCommunication(INFINITE)
if ret != 0:
    print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# Import and set all the preset motion parameters.
ret = Wmx3Lib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
if ret != 0:
    print('ImportAndSetAll Parameters error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set servo on for Axis 13
ret = Wmx3Lib_cm.axisControl.SetServoOn(13, 1)
if ret != 0:
    print('SetServoOn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Jog Axis 13 back and forth 4 times
for _ in range(4):
    # Jog Axis 13 for 1 second with a velocity of 90
    jogCommand = Motion_JogCommand()
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.axis = 13
    jogCommand.profile.velocity = 90
    jogCommand.profile.acc = 10000
    jogCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Jogging for 1 second
    sleep(1)

    # Stop the motor
    Wmx3Lib_cm.motion.Stop(13)

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(13)

    # Jog Axis 13 for 1 second with a velocity of -90
    jogCommand.profile.velocity = -90

    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Jogging for 1 second
    sleep(1)

    # Stop the motor
    Wmx3Lib_cm.motion.Stop(13)

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(13)

# Set servo off for Axis 13
ret = Wmx3Lib_cm.axisControl.SetServoOn(13, 0)
if ret != 0:
    print('SetServoOn to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Stop Communication.
ret = Wmx3Lib.StopCommunication(INFINITE)
if ret != 0:
    print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# Close Device.
ret = Wmx3Lib.CloseDevice()
if ret != 0:
    print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

print('Program End.')
