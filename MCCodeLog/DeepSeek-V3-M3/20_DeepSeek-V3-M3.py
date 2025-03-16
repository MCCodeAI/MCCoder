
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

# Initialize the IO library
Wmx3Lib_Io = Io(Wmx3Lib)

# Read the input bit 0.3
ret, input_value = Wmx3Lib_Io.GetInBit(0x0, 0x03)
if ret != 0:
    print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Check the value of the input bit
if input_value == 1:
    # Set output bit 0.3 to 0
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
else:
    # Set output bit 0.3 to 1
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
