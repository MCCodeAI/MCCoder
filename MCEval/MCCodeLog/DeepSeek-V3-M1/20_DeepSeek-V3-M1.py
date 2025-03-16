
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

# Write Python code to read IO input bit 0.3. If it is 1, set IO output bit 0.3 to 0, otherwise, set it to 1.

Wmx3Lib_Io = Io(Wmx3Lib)

# Read IO input bit 0.3
ret, input_value = Wmx3Lib_Io.GetInBit(0x0, 0x03)
if ret != 0:
    print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Set IO output bit 0.3 based on the input value
if input_value == 1:
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x00)
else:
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x01)

if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return
