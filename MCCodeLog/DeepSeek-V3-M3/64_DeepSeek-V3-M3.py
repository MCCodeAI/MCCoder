
# Axes = [2, 4, 5]
# IOInputs = []
# IOOutputs = []

# Define the motion profile
profile = {
    'type': 'Trapezoidal',
    'velocity': 300,
    'acc': 2000,
    'dec': 2000
}

# Define the path segments
segments = [
    # Segment 1: Linear to (90, 0, 0)
    {'type': 'Linear', 'target': [90, 0, 0]},
    
    # Segment 2: Circular to (100, 10, 0) with center (97.071, 2.929, 0)
    {'type': 'Circular', 'target': [100, 10, 0], 'center': [97.071, 2.929, 0]},
    
    # Segment 3: Linear to (100, 90, 0)
    {'type': 'Linear', 'target': [100, 90, 0]},
    
    # Segment 4: Circular to (90, 100, 0) with center (97.071, 97.071, 0)
    {'type': 'Circular', 'target': [90, 100, 0], 'center': [97.071, 97.071, 0]},
    
    # Segment 5: Linear to (10, 100, 0)
    {'type': 'Linear', 'target': [10, 100, 0]},
    
    # Segment 6: Circular to (0, 90, 0) with center (2.929, 97.071, 0)
    {'type': 'Circular', 'target': [0, 90, 0], 'center': [2.929, 97.071, 0]},
    
    # Segment 7: Linear to (0, 0, 0)
    {'type': 'Linear', 'target': [0, 0, 0]},
    
    # Segment 8: Linear to (90, 0, 0)
    {'type': 'Linear', 'target': [90, 0, 0]},
    
    # Segment 9: Circular to (100, 0, -10) with center (97.071, 0, -2.929)
    {'type': 'Circular', 'target': [100, 0, -10], 'center': [97.071, 0, -2.929]},
    
    # Segment 10: Linear to (100, 0, -90)
    {'type': 'Linear', 'target': [100, 0, -90]},
    
    # Segment 11: Circular to (90, 0, -100) with center (97.071, 0, -97.071)
    {'type': 'Circular', 'target': [90, 0, -100], 'center': [97.071, 0, -97.071]},
    
    # Segment 12: Linear to (10, 0, -100)
    {'type': 'Linear', 'target': [10, 0, -100]},
    
    # Segment 13: Circular to (0, 0, -90) with center (2.929, 0, -97.071)
    {'type': 'Circular', 'target': [0, 0, -90], 'center': [2.929, 0, -97.071]},
    
    # Segment 14: Linear to (0, 0, 0)
    {'type': 'Linear', 'target': [0, 0, 0]},
    
    # Segment 15: Linear to (0, 90, 0)
    {'type': 'Linear', 'target': [0, 90, 0]},
    
    # Segment 16: Circular to (0, 100, -10) with center (0, 97.071, -2.929)
    {'type': 'Circular', 'target': [0, 100, -10], 'center': [0, 97.071, -2.929]},
    
    # Segment 17: Linear to (0, 100, -90)
    {'type': 'Linear', 'target': [0, 100, -90]},
    
    # Segment 18: Circular to (0, 90, -100) with center (0, 97.071, -97.071)
    {'type': 'Circular', 'target': [0, 90, -100], 'center': [0, 97.071, -97.071]},
    
    # Segment 19: Linear to (0, 10, -100)
    {'type': 'Linear', 'target': [0, 10, -100]},
    
    # Segment 20: Circular to (0, 0, -90) with center (0, 2.929, -97.071)
    {'type': 'Circular', 'target': [0, 0, -90], 'center': [0, 2.929, -97.071]},
    
    # Segment 21: Linear to (0, 0, 0)
    {'type': 'Linear', 'target': [0, 0, 0]},
]

# Function to execute the path interpolation
def execute_path_interpolation(axes, profile, segments):
    for segment in segments:
        if segment['type'] == 'Linear':
            print(f"Moving linearly to {segment['target']} with velocity {profile['velocity']}")
        elif segment['type'] == 'Circular':
            print(f"Moving circularly to {segment['target']} with center {segment['center']} and velocity {profile['velocity']}")
        # Wait for axes to stop moving after each segment
        print("Waiting for axes to stop moving...")
        # Simulate waiting for axes to stop
        # In a real scenario, this would involve checking the status of the axes

# Execute the forward path
execute_path_interpolation([2, 4, 5], profile, segments)

# Reverse the sequence and execute the reverse path
reversed_segments = segments[::-1]
execute_path_interpolation([2, 4, 5], profile, reversed_segments)
