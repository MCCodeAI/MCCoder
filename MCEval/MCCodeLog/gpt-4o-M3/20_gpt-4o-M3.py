
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

# Create an instance of the Io class
Wmx3Lib_Io = Io(Wmx3Lib)

# Read the input bit 0.3
input_status = Wmx3Lib_Io.GetInBit(0x0, 0x03)

# Check if the input bit 0.3 is 1
if input_status == 1:
    # Set the output bit 0.3 to 0
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
else:
    # Set the output bit 0.3 to 1
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
