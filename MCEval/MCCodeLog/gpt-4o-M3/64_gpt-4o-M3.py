
# Axes = [4, 5, 2]
# Inputs = []
# Outputs = []

# Define the path interpolation for Axes 4, 5, and 2 with a velocity of 300
class PathInterpolation:
    def __init__(self):
        self.segments = []

    def add_linear(self, target):
        self.segments.append(('Linear', target))

    def add_circular(self, target, center):
        self.segments.append(('Circular', target, center))

    def execute(self):
        for segment in self.segments:
            if segment[0] == 'Linear':
                self.move_linear(segment[1])
            elif segment[0] == 'Circular':
                self.move_circular(segment[1], segment[2])

    def move_linear(self, target):
        print(f"Moving linearly to {target}")
        # Simulate waiting for the axis to stop
        self.wait_for_axes()

    def move_circular(self, target, center):
        print(f"Moving circularly to {target} with center {center}")
        # Simulate waiting for the axis to stop
        self.wait_for_axes()

    def wait_for_axes(self):
        print("Waiting for axes to stop...")

# Create the path interpolation object
path = PathInterpolation()

# Define the path segments
path.add_linear((90, 0, 0))
path.add_circular((100, 10, 0), (97.071, 2.929, 0))
path.add_linear((100, 90, 0))
path.add_circular((90, 100, 0), (97.071, 97.071, 0))
path.add_linear((10, 100, 0))
path.add_circular((0, 90, 0), (2.929, 97.071, 0))
path.add_linear((0, 0, 0))
path.add_linear((90, 0, 0))
path.add_circular((100, 0, -10), (97.071, 0, -2.929))
path.add_linear((100, 0, -90))
path.add_circular((90, 0, -100), (97.071, 0, -97.071))
path.add_linear((10, 0, -100))
path.add_circular((0, 0, -90), (2.929, 0, -97.071))
path.add_linear((0, 0, 0))
path.add_linear((0, 90, 0))
path.add_circular((0, 100, -10), (0, 97.071, -2.929))
path.add_linear((0, 100, -90))
path.add_circular((0, 90, -100), (0, 97.071, -97.071))
path.add_linear((0, 10, -100))
path.add_circular((0, 0, -90), (0, 2.929, -97.071))
path.add_linear((0, 0, 0))

# Execute the path
path.execute()

# Reverse the path
print("Reversing the path...")
path.segments.reverse()
path.execute()
