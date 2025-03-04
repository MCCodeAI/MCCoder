
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_and_plot(log_file_path):
    # Check if file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return
    
    # Read the file
    try:
        data = pd.read_csv(log_file_path, sep='\t')  # Assuming the file is tab-separated; adjust if necessary
    except Exception as e:
        print(f"Error reading file {log_file_path}: {e}")
        return
    
    # Read the first CYCLE value to use as the baseline
    baseline_cycle = data['CYCLE'].iloc[0]
    
    # Adjust CYCLE values
    data['CYCLE'] = data['CYCLE'] - baseline_cycle
    
    # Plot the data
    plt.figure(figsize=(6, 6))  # Set figure size to be square
    for i, column in enumerate(data.columns[1:]):  # Exclude the first column 'CYCLE'
        # Skip columns that are completely empty
        if data[column].isnull().all():
            print(f"Column {column} is empty. Skipping this column.")
            continue
        
        line, = plt.plot(data['CYCLE'], data[column], linestyle='-', label=column, linewidth=2)  # Set line width to 2
        
        # Mark the start and end values
        start_value = data[column].iloc[0]
        end_value = data[column].iloc[-1]
        plt.text(data['CYCLE'].iloc[0], start_value, f'{start_value}', ha='right', fontsize=10, color=line.get_color())
        plt.text(data['CYCLE'].iloc[-1], end_value, f'{end_value}', ha='left', fontsize=10, color=line.get_color())
    
    plt.title(f'Log Plot', fontsize=16)
    plt.xlabel('CYCLE (Time)', fontsize=14)
    plt.ylabel('Values', fontsize=14)
    plt.legend()
    plt.grid(True)
    
    # Save the plot with higher DPI to reduce aliasing
    plot_path = os.path.splitext(log_file_path)[0] + '_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()  # Show the plot in the notebook
    plt.close()
    # print(f"Plot saved: {plot_path}")

def plot_2nd_and_3rd_columns(log_file_path):
    # Check if file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return
    
    # Read the file
    try:
        data = pd.read_csv(log_file_path, sep='\t')  # Assuming the file is tab-separated; adjust if necessary
    except Exception as e:
        print(f"Error reading file {log_file_path}: {e}")
        return
    
    # Check if there are at least 3 columns
    if data.shape[1] < 3:
        # print(f"File {log_file_path} does not have enough columns. Skipping plot.")
        return
    
    # Check if the third column is empty
    if data.iloc[:, 2].isnull().all():
        print(f"Third column in file {log_file_path} is empty. Skipping plot.")
        return
    
    # Plot the 2nd column as X and 3rd column as Y with red color
    plt.figure(figsize=(6, 6))  # Set figure size to be square
    plt.plot(data.iloc[:, 1], data.iloc[:, 2], linestyle='-', label=f'{data.columns[1]} vs {data.columns[2]}', linewidth=2, color='red')
    
    # Mark the start and end values
    start_x = data.iloc[0, 1]
    start_y = data.iloc[0, 2]
    end_x = data.iloc[-1, 1]
    end_y = data.iloc[-1, 2]
    plt.text(start_x, start_y, f'({start_x}, {start_y})', ha='right', fontsize=10, color='red')
    plt.text(end_x, end_y, f'({end_x}, {end_y})', ha='left', fontsize=10, color='red')
    
    plt.title(f'Log Plot - {data.columns[1]} vs {data.columns[2]}', fontsize=16)
    plt.xlabel(data.columns[1], fontsize=14)
    plt.ylabel(data.columns[2], fontsize=14)
    plt.legend()
    plt.grid(True)
    
    # Ensure the axis scale is equal
    plt.axis('equal')
    
    # Save the plot with higher DPI to reduce aliasing
    plot_path = os.path.splitext(log_file_path)[0] + '_2d_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()  # Show the plot in the notebook
    plt.close()
    # print(f"Plot saved: {plot_path}")

def plot_3d(log_file_path):
    # Check if file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return
    
    # Read the file
    try:
        data = pd.read_csv(log_file_path, sep='\t')  # Assuming the file is tab-separated; adjust if necessary
    except Exception as e:
        print(f"Error reading file {log_file_path}: {e}")
        return
    
    # Check if there are at least 4 columns
    if data.shape[1] < 4:
        # print(f"File {log_file_path} does not have enough columns for 3D plot. Skipping plot.")
        return
    
    # Check if the 2nd, 3rd, and 4th columns are empty
    if data.iloc[:, 1].isnull().all() or data.iloc[:, 2].isnull().all() or data.iloc[:, 3].isnull().all():
        print(f"One of the required columns in file {log_file_path} is empty. Skipping plot.")
        return
    
    # Create a 3D plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(data.iloc[:, 1], data.iloc[:, 2], data.iloc[:, 3], linestyle='-', label=f'{data.columns[1]} vs {data.columns[2]} vs {data.columns[3]}', linewidth=2)
    
    # Mark the start and end values
    start_x = data.iloc[0, 1]
    start_y = data.iloc[0, 2]
    start_z = data.iloc[0, 3]
    end_x = data.iloc[-1, 1]
    end_y = data.iloc[-1, 2]
    end_z = data.iloc[-1, 3]
    ax.text(start_x, start_y, start_z, f'({start_x}, {start_y}, {start_z})', color='red', fontsize=10)
    ax.text(end_x, end_y, end_z, f'({end_x}, {end_y}, {end_z})', color='red', fontsize=10)
    
    ax.set_title(f'Log Plot - {data.columns[1]} vs {data.columns[2]} vs {data.columns[3]}', fontsize=16)
    ax.set_xlabel(data.columns[1], fontsize=14)
    ax.set_ylabel(data.columns[2], fontsize=14)
    ax.set_zlabel(data.columns[3], fontsize=14)
    ax.legend()
    
    # Set equal scaling
    ax.set_box_aspect([1, 1, 1])
    
    # Save the plot with higher DPI to reduce aliasing
    plot_path = os.path.splitext(log_file_path)[0] + '_3d_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()  # Show the plot in the notebook
    plt.close()
    # print(f"Plot saved: {plot_path}")

# Set matplotlib to use anti-aliasing
plt.rcParams['lines.antialiased'] = True

# 示例用法
# log_file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/0_gpt-4o_Log.txt'


def plot_log(log_file_path):
    read_and_plot(log_file_path)
    plot_2nd_and_3rd_columns(log_file_path)
    plot_3d(log_file_path)