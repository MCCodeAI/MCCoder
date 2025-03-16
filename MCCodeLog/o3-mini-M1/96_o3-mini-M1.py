
# Axes = [6]
# IOInputs = []
# IOOutputs = []

import time

def wait_until_axis_stop(axis):
    # Poll the axis until it stops moving.
    # This is a placeholder function. In a real system, replace this with the proper API call.
    while Wmx3Lib_cm.motion.IsAxisMoving(axis):
        time.sleep(0.1)

def main():
    axis = 6

    # --- Set Following Error Stopped to 0.02 ---
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    if ret != 0:
        print("Error getting AlarmParam for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return
    alarmParam.followingErrorStopped = 0.02
    ret, paramError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if ret != 0:
        print("Set followingErrorStopped error code {}: {}".format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # --- Set Following Error Moving to 0.05 ---
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    if ret != 0:
        print("Error getting AlarmParam for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return
    alarmParam.followingErrorMoving = 0.05
    ret, paramError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if ret != 0:
        print("Set followingErrorMoving error code {}: {}".format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # --- Set Servo Off During Amp Alarm to FALSE ---
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    if ret != 0:
        print("Error getting AlarmParam for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return
    alarmParam.servoOffDuringAmpAlarm = False
    ret, paramError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if ret != 0:
        print("Set servoOffDuringAmpAlarm error code {}: {}".format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # --- Verify parameters ---
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    if ret != 0:
        print("Error verifying AlarmParam for Axis {}: {}".format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    if (abs(alarmParam.followingErrorStopped - 0.02) < 1e-6 and 
        abs(alarmParam.followingErrorMoving - 0.05) < 1e-6 and 
        alarmParam.servoOffDuringAmpAlarm == False):
        target_position = 99
    else:
        target_position = 66

    # --- Move Axis 6 to the determined position ---
    ret = Wmx3Lib_cm.motion.MoveAxisAbs(axis, target_position)
    if ret != 0:
        print("Error moving Axis {} to position {}: {}".format(axis, target_position, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until the axis has completely stopped moving.
    wait_until_axis_stop(axis)
    print("Axis", axis, "moved to position", target_position)

if __name__ == "__main__":
    main()
