
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Define motion profiles for Axis 10
pos = Motion_PosCommand()

# Move Axis 10 to -10 using TimeAccAdvancedS profile
pos.axis = 10
pos.profile.type = ProfileType.TimeAccAdvancedS
pos.target = -10
pos.profile.velocity = 1000  # Example velocity, adjust as needed
pos.profile.acc = 1000       # Example acceleration, adjust as needed
pos.profile.dec = 1000       # Example deceleration, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 10 to 20 using TwoVelocityTrapezoidal profile
pos.profile.type = ProfileType.TwoVelocityTrapezoidal
pos.target = 20
pos.profile.velocity = 1000  # Example velocity, adjust as needed
pos.profile.acc = 1000       # Example acceleration, adjust as needed
pos.profile.dec = 1000       # Example deceleration, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 10 to -30 using ConstantDec profile
pos.profile.type = ProfileType.ConstantDec
pos.target = -30
pos.profile.velocity = 1000  # Example velocity, adjust as needed
pos.profile.acc = 1000       # Example acceleration, adjust as needed
pos.profile.dec = 1000       # Example deceleration, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 10 to 40 using ParabolicVelocity profile
pos.profile.type = ProfileType.ParabolicVelocity
pos.target = 40
pos.profile.velocity = 1000  # Example velocity, adjust as needed
pos.profile.acc = 1000       # Example acceleration, adjust as needed
pos.profile.dec = 1000       # Example deceleration, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 10 to 0 using JerkRatioFixedVelocityS profile
pos.profile.type = ProfileType.JerkRatioFixedVelocityS
pos.target = 0
pos.profile.velocity = 1000  # Example velocity, adjust as needed
pos.profile.acc = 1000       # Example acceleration, adjust as needed
pos.profile.dec = 1000       # Example deceleration, adjust as needed
pos.profile.jerkAccRatio = 0.5  # Example jerk ratio, adjust as needed
pos.profile.jerkDecRatio = 0.5  # Example jerk ratio, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
