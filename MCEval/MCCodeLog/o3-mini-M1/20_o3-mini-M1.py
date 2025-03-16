
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

# Read IO input bit 0.3. If it is 1, set IO output bit 0.3 to 0, otherwise set it to 1.

# Create an instance of the Io class.
Wmx3Lib_Io = Io(Wmx3Lib)

# Read input bit 0.3
ret, input_value = Wmx3Lib_Io.GetInBit(0x0, 0x03)
if ret != 0:
    print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Check the read value: if it's 1, set output bit 0.3 to 0, else set it to 1.
if input_value == 1:
    output_val = 0
else:
    output_val = 1

ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, output_val)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# As there is no motion command in this script, no waiting for axes stopping is needed.
