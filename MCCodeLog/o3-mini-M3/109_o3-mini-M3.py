
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# In this script, we move Axis 2 and Axis 9 to the target positions 100 and 200 respectively.
# We issue separate absolute position commands for each axis and then wait until both axes have stopped moving.

# Create and send an absolute position command for Axis 2
posCommand_axis2 = Motion_PosCommand()
posCommand_axis2.profile.type = ProfileType.Trapezoidal
posCommand_axis2.axis = 2
posCommand_axis2.target = 100
posCommand_axis2.profile.velocity = 1000
posCommand_axis2.profile.acc = 10000
posCommand_axis2.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis2)
if ret != 0:
    print('StartPos error code for Axis 2 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    
# Create and send an absolute position command for Axis 9
posCommand_axis9 = Motion_PosCommand()
posCommand_axis9.profile.type = ProfileType.Trapezoidal
posCommand_axis9.axis = 9
posCommand_axis9.target = 200
posCommand_axis9.profile.velocity = 1000
posCommand_axis9.profile.acc = 10000
posCommand_axis9.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis9)
if ret != 0:
    print('StartPos error code for Axis 9 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait for both axes to finish moving.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
