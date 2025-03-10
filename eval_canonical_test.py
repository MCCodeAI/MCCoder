from app_NaiveRAG_M1_eval import *
# from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *

def run():

    # # TaskId file path
    # file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/TaskId.txt'
    # with open(file_path, 'r', encoding='utf-8') as file:
    #         task_info = file.read().strip()   

    # Define start and end task IDs manually
    start_id = 117
    end_id = start_id

    # Loop through task IDs from start_id to end_id (inclusive)
    while start_id <= end_id:
        # Construct file path for current task ID
        file_path = f'/Users/yin/Documents/GitHub/MCCodeLog/CanonicalCode/{start_id}_CanonicalCode.py'
        
        # Open and read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            msgCode = file.read()
 
        # Only for making CanonicalCode.
        llm_name = 'CanonicalCode'
    
        RunnableCode = make_code_runnable(msgCode, llm_name, start_id)

        # Old and new paths
        old_path = f'path_0.dirPath = r"\\\\Mac\\\\Home\\\\Documents\\\\GitHub\\\\MCCodeLog\\\\{llm_name}"'

        new_path = r'path_0.dirPath = r"C:\\"'

        # Replace the old path with the new one
        global RunnableCodeinMachine
        RunnableCodeinMachine = RunnableCode.replace(old_path, new_path)
        RunnableCodeinMachine = re.sub(r'# <logon[\s\S]*?# logon>', '', RunnableCodeinMachine)
        RunnableCodeinMachine = re.sub(r'# <logoff[\s\S]*?# logoff>', '', RunnableCodeinMachine)


        # Run Code in WMX3
        codereturn = SendCode(RunnableCode)

        folder_path = f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}'
        os.makedirs(folder_path, exist_ok=True)

        # Define plot files name
        plot_filenames = [
            f"{start_id}_{llm_name}_log_plot.png",
            f"{start_id}_{llm_name}_log_2d_plot.png",
            f"{start_id}_{llm_name}_log_3d_plot.png"
        ]

        # Check if the plot files exist in folder_path and delete them if they do
        for filename in plot_filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)

        log_file_path = os.path.join(folder_path, f"{start_id}_{llm_name}_log.txt")
        # Plot with the log file
        plot_log(log_file_path)
        
        sleep(0.1)

        start_id += 1

def create_empty_files(start_id, end_id, base_path):
    # Loop through IDs from start_id to end_id (inclusive)
    current_id = start_id
    while current_id <= end_id:
        # Construct full file path with ID
        file_path = f'{base_path}/{current_id}_CanonicalCode.py'
        
        # Create and immediately close an empty file
        with open(file_path, 'w', encoding='utf-8') as file:
            pass  # 'w' mode creates an empty file if it doesn't exist
        
        # Print confirmation
        print(f"Created empty file: {file_path}")
        
        # Increment ID
        current_id += 1
    

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()

    # # Set parameters and call the function
    # start_id = 117
    # end_id = 200
    # base_path = '/Users/yin/Documents/GitHub/MCCodeLog/CanonicalCode'
    # create_empty_files(start_id, end_id, base_path)

 