from app_NaiveRAG_M1_eval import *
# from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *
import json
from tqdm import tqdm 

def run():

    # Initialize counters for statistics
    total_correct = 0
    total_error = 0
    diff1_correct = 0
    diff1_error = 0
    diff2_correct = 0
    diff2_error = 0
    diff3_correct = 0
    diff3_error = 0
    
    # Define start and end task IDs manually
    start_id = 1
    end_id = 10
    
    # Load the JSON dataset
    with open('docs/WMX3API_MCEval_Evaluation_Dataset.json', 'r') as f:
        dataset = json.load(f)
    
    # Loop through task IDs with tqdm progress bar
    for current_id in tqdm(range(start_id, end_id + 1), desc="Processing Tasks"):
        # Log the start of script execution with task ID
        log_message(f"{llm_name} Script execution starts for Task ID: {current_id}")
        
        # Get the specific item from dataset (assuming start_id matches index + 1)
        item = dataset[current_id - 1]
        task_id = item['TaskId']
        tp = item['Instruction']  # Assign Instruction to tp
        difficulty = item['Difficulty']
        check_end = item['CheckEnd']
        
        # Execute the on_message function with task_id and instruction
        codereturn = on_message(task_id, tp)
        
        # Check if codereturn contains error indicators
        if "codeerr" in codereturn.lower() or "error code" in codereturn.lower():
            is_error = True
            total_error += 1
            # Update difficulty-specific error count
            if difficulty == 1:
                diff1_error += 1
            elif difficulty == 2:
                diff2_error += 1
            elif difficulty == 3:
                diff3_error += 1
        else:
            is_error = False
            total_correct += 1
            # Update difficulty-specific correct count
            if difficulty == 1:
                diff1_correct += 1
            elif difficulty == 2:
                diff2_correct += 1
            elif difficulty == 3:
                diff3_correct += 1
        
        # Log the completion of script execution with task ID
        log_message(f"{llm_name} Script execution completed for Task ID: {current_id}")
        
        # Wait for 0.1 seconds before next iteration
        sleep(0.1)
    
    # Calculate statistics
    total_tasks = total_correct + total_error
    total_accuracy = total_correct / total_tasks * 100 if total_tasks > 0 else 0
    total_error_rate = total_error / total_tasks * 100 if total_tasks > 0 else 0
    
    diff1_tasks = diff1_correct + diff1_error
    diff1_accuracy = diff1_correct / diff1_tasks * 100 if diff1_tasks > 0 else 0
    diff1_error_rate = diff1_error / diff1_tasks * 100 if diff1_tasks > 0 else 0
    
    diff2_tasks = diff2_correct + diff2_error
    diff2_accuracy = diff2_correct / diff2_tasks * 100 if diff2_tasks > 0 else 0
    diff2_error_rate = diff2_error / diff2_tasks * 100 if diff2_tasks > 0 else 0
    
    diff3_tasks = diff3_correct + diff3_error
    diff3_accuracy = diff3_correct / diff3_tasks * 100 if diff3_tasks > 0 else 0
    diff3_error_rate = diff3_error / diff3_tasks * 100 if diff3_tasks > 0 else 0
    
    # Prepare log content
    log_content = f"""
Evaluation Statistics:
Total Tasks: {total_tasks}
Total Correct: {total_correct}
Total Errors: {total_error}
Overall Accuracy: {total_accuracy:.2f}%
Overall Error Rate: {total_error_rate:.2f}%

Difficulty 1:
  Correct: {diff1_correct}
  Errors: {diff1_error}
  Accuracy: {diff1_accuracy:.2f}%
  Error Rate: {diff1_error_rate:.2f}%

Difficulty 2:
  Correct: {diff2_correct}
  Errors: {diff2_error}
  Accuracy: {diff2_accuracy:.2f}%
  Error Rate: {diff2_error_rate:.2f}%

Difficulty 3:
  Correct: {diff3_correct}
  Errors: {diff3_error}
  Accuracy: {diff3_accuracy:.2f}%
  Error Rate: {diff3_error_rate:.2f}%
"""
    
    with open(f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}/log.txt', 'w') as f:
        f.write(log_content)
    

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")