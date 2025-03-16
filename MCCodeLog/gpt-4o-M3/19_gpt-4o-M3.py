
# Axes = []
# IOInputs = []
# IOOutputs = [1.1]

import time

# Function to set an IO output bit
def set_io_output(byte, bit, value):
    # Simulate setting the IO output bit
    print(f"Setting output {byte}.{bit} to {value}")

# Repeat the cycle 5 times
for _ in range(5):
    # Set IO output bit 1.1 to 1
    set_io_output(1, 1, 1)
    # Wait for 0.2 seconds
    time.sleep(0.2)
    # Set IO output bit 1.1 to 0
    set_io_output(1, 1, 0)
    # Wait for 0.2 seconds
    time.sleep(0.2)
