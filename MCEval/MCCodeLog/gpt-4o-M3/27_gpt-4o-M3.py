
# Axes = [7, 8]
# Inputs = []
# Outputs = []

# Define the points for the pentastar path
pentastar_points = [
    (0.00, 0.00),
    (22.45, -69.10),
    (95.11, -69.10),
    (36.33, -111.80),
    (58.78, -180.90),
    (0.00, -138.20),
    (-58.78, -180.90),
    (-36.33, -111.80),
    (-95.11, -69.10),
    (-22.45, -69.10)
]

# Set the velocity for the path interpolation
velocity = 1500

# Function to move to a specific point
def move_to_point(axis1, axis2, point):
    # Simulate moving to the point
    print(f"Moving Axis {axis1} to {point[0]} and Axis {axis2} to {point[1]} at velocity {velocity}")
    # Wait for the axes to stop moving
    print(f"Waiting for Axis {axis1} and Axis {axis2} to stop...")

# Execute the path interpolation
for point in pentastar_points:
    move_to_point(7, 8, point)

print("Path interpolation complete.")
