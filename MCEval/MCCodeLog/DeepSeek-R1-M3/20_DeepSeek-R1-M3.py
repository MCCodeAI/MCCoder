
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

Wmx3Lib_Io = Io(Wmx3Lib)

# Read input bit 0.3
ret, value = Wmx3Lib_Io.GetInBit(0x0, 0x03)
if ret != 0:
    print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Set output bit 0.3 based on input state
output_value = 0x00 if value == 1 else 0x01

ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, output_value)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return
