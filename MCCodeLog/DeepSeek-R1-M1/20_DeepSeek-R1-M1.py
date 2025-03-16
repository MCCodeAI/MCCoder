
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

Wmx3Lib_Io = Io(Wmx3Lib)

# Read IO input bit 0.3
ret, value = Wmx3Lib_Io.GetInBit(0x00, 0x03)
if ret != 0:
    print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Set output based on input state
if value == 1:
    # Set output 0.3 to 0
    ret = Wmx3Lib_Io.SetOutBit(0x00, 0x03, 0x00)
else:
    # Set output 0.3 to 1
    ret = Wmx3Lib_Io.SetOutBit(0x00, 0x03, 0x01)

if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return
