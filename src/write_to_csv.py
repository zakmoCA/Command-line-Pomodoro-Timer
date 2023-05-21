import os
import csv

def write_to_csv(task_name, pomodoro):
    # CSV file headers 
    headers = ['Task Name', 'Start Time', 'End Time', 'Duration']
    # Check if the CSV file already exists
    file_exists = os.path.isfile('pomodoros.csv')
    # Now, write the pomodoro to a CSV file
    with open('pomodoros.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # If file doesn't already exist (first pomodoro), write headers first
        if not file_exists:
            writer.writerow(headers)
        # Write Pomodoro data to CSV 
        writer.writerow([task_name, pomodoro['start_time'], pomodoro['end_time'], f"{pomodoro['duration']} min"])
