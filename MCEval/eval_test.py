# from app_NaiveRAG_M1_eval import *
from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *
import json
from tqdm import tqdm 

def run():
    # Initialize counters for tracking statistics
    total_correct = 0
    total_error = 0
    diff1_correct = 0
    diff1_error = 0
    diff2_correct = 0
    diff2_error = 0
    diff3_correct = 0
    diff3_error = 0
    error_ids = []  # List to store IDs of tasks with errors
    llm_times = []  # List to store LLM execution times
    
    # Define start and end task IDs manually
    start_id = 112 #111
    end_id = 116
    
    # Load the JSON dataset from file
    with open('docs/WMX3API_MCEval_Evaluation_Dataset.json', 'r') as f:
        dataset = json.load(f)
    
    # Loop through task IDs with tqdm progress bar
    for current_id in tqdm(range(start_id, end_id + 1), desc="Processing Tasks"):
        # Log the start of script execution with task ID
        log_message(f"{llm_name}: starts for Task ID: {current_id}")
        
        # Get the specific item from dataset (assuming start_id matches index + 1)
        item = dataset[current_id - 1]
        task_id = item['TaskId']
        tp = item['Instruction']  # Assign Instruction to tp
        difficulty = item['Difficulty']
        check_end = item['CheckEnd']
        
        # Execute the on_message function with task_id and instruction
        codereturn = on_message(task_id, tp)
        
        # Extract llm_time from codereturn (between "llm_time:" and "s")
        import re
        time_match = re.search(r'llm_time: (\d+\.?\d*)s', codereturn)
        llm_time = float(time_match.group(1)) if time_match else 0.0
        llm_times.append(llm_time)
        
        # Check if codereturn contains error indicators
        if "codeerr" in codereturn.lower() or "error code" in codereturn.lower():
            is_error = True
            total_error += 1
            error_ids.append(current_id)  # Record the ID of the erroneous task
            # Update difficulty-specific error count
            if difficulty == 1:
                diff1_error += 1
            elif difficulty == 2:
                diff2_error += 1
            elif difficulty == 3:
                diff3_error += 1
            # Log error with task ID
            log_message(f"{llm_name} Error detected for Task ID: {current_id}")
            task_status = "Error"
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
            task_status = "Correct"
        
        # Log the completion of script execution with task ID and LLM time
        log_message(f"{llm_name}: completed for Task ID: {current_id}, LLM Time: {llm_time:.2f}s")
        
        # Append only the task result to log.txt during the loop
        with open(f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}/log.txt', 'a') as f:
            f.write(f"Task ID: {current_id}, Status: {task_status}, Difficulty: {difficulty}, LLM Time: {llm_time:.2f}s\n")
        
        # Wait for 0.1 seconds before next iteration
        sleep(0.1)
    
    # After the loop, calculate statistics for overall and difficulty-specific performance
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
    
    # Calculate average LLM time
    average_llm_time = sum(llm_times) / len(llm_times) if llm_times else 0.0
    
    # Prepare log content with statistics, error IDs, and average LLM time
    log_content = f"""
Evaluation Statistics:
Total Tasks: {total_tasks}
Total Correct: {total_correct}
Total Errors: {total_error}
Overall Accuracy: {total_accuracy:.2f}%
Overall Error Rate: {total_error_rate:.2f}%
Error Task IDs: {error_ids}
Average LLM Time: {average_llm_time:.2f}s

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
    
    # Append the final statistics to the log file only after all tasks are completed
    with open(f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}/log.txt', 'a') as f:
        f.write(log_content)


# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")