
# Axes = [10]
# IOInputs = []
# IOOutputs = []

def main():
    # Segment 1: Move Axis 10 to -10 using TimeAccAdvancedS profile
    pos1 = Motion_PosCommand()
    pos1.axis = 10
    pos1.target = -10
    pos1.profile.type = ProfileType.TimeAccAdvancedS
    # Set profile parameters (values chosen arbitrarily as an example)
    pos1.profile.velocity = 50
    pos1.profile.acc = 200    # Time acceleration (ms)
    pos1.profile.dec = 200    # Time deceleration (ms)
    
    ret = Wmx3Lib_cm.motion.StartPos(pos1)
    if ret != 0:
        print('StartPos (TimeAccAdvancedS) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until axis 10 stops moving after segment 1
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Wait after segment 1 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Segment 2: Move Axis 10 to 20 using TwoVelocityTrapezoidal profile
    pos2 = Motion_PosCommand()
    pos2.axis = 10
    pos2.target = 20
    pos2.profile.type = ProfileType.TwoVelocityTrapezoidal
    # Set profile parameters (example values)
    pos2.profile.velocity = 100
    pos2.profile.acc = 1000
    pos2.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartPos(pos2)
    if ret != 0:
        print('StartPos (TwoVelocityTrapezoidal) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until axis 10 stops moving after segment 2
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Wait after segment 2 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Segment 3: Move Axis 10 to -30 using ConstantDec profile
    pos3 = Motion_PosCommand()
    pos3.axis = 10
    pos3.target = -30
    pos3.profile.type = ProfileType.ConstantDec
    # Set profile parameters (example values)
    pos3.profile.velocity = 80
    pos3.profile.dec = 1200  # constant deceleration value

    ret = Wmx3Lib_cm.motion.StartPos(pos3)
    if ret != 0:
        print('StartPos (ConstantDec) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until axis 10 stops moving after segment 3
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Wait after segment 3 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Segment 4: Move Axis 10 to 40 using ParabolicVelocity profile
    pos4 = Motion_PosCommand()
    pos4.axis = 10
    pos4.target = 40
    pos4.profile.type = ProfileType.ParabolicVelocity
    # Set profile parameters (example values)
    pos4.profile.velocity = 90
    pos4.profile.acc = 800
    pos4.profile.dec = 800

    ret = Wmx3Lib_cm.motion.StartPos(pos4)
    if ret != 0:
        print('StartPos (ParabolicVelocity) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until axis 10 stops moving after segment 4
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Wait after segment 4 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Segment 5: Move Axis 10 to 0 using JerkRatioFixedVelocityS profile
    pos5 = Motion_PosCommand()
    pos5.axis = 10
    pos5.target = 0
    pos5.profile.type = ProfileType.JerkRatioFixedVelocityS
    # Set profile parameters (example values similar to provided example)
    pos5.profile.velocity = 1000
    pos5.profile.acc = 10000
    pos5.profile.dec = 10000
    pos5.profile.jerkAccRatio = 0.5
    pos5.profile.jerkDecRatio = 0.5
    pos5.profile.startingVelocity = 0
    pos5.profile.endVelocity = 0

    ret = Wmx3Lib_cm.motion.StartPos(pos5)
    if ret != 0:
        print('StartPos (JerkRatioFixedVelocityS) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until axis 10 stops moving after segment 5
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print('Final Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
