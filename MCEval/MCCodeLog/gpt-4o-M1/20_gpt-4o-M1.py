
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

# Initialize the IO library
Wmx3Lib_Io = Io(Wmx3Lib)

# Read the input bit 0.3
input_status = Wmx3Lib_Io.GetInBit(0x0, 0x03)

# Check if reading the input was successful
if input_status is None:
    print('GetInBit error: Unable to read input bit 0.3')
else:
    # If input bit 0.3 is 1, set output bit 0.3 to 0
    if input_status == 1:
        ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x00)
        if ret != 0:
            print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    # If input bit 0.3 is 0, set output bit 0.3 to 1
    else:
        ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x01)
        if ret != 0:
            print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
