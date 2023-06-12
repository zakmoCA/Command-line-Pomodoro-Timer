from pomodoro_length import pomodoro_length 
import datetime
from run_pomodoro import run_pomodoro
from write_to_csv import write_to_csv



# Store Pomodoro and task data
pomodoros = [] # List containing dictionary of data for each pomodoro
tasks = [] # list containing dictionary of task names and list of 'pomodoro' dictionaries


def start():
    try:
        while True:
          task_name = input('Enter the name of the task this pomodoro is for: ')
          if task_name:
              break
          else:
              print("You must enter a task name. Please try again.")
        cycle_length, work_time, short_break_time, long_break_time = pomodoro_length()  # my pomodoro as defined by pomodoro_length()

        pomodoro = {
            'start_time': datetime.datetime.now().replace(microsecond=0),
            'end_time': datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(minutes=work_time),
            'duration': work_time,
            'task': task_name,
        }
        pomodoros.append(pomodoro)

        # Check if the task already exists
        task_exists = False
        for task in tasks:
            if task['name'] == task_name:
                task['pomodoros'].append(pomodoro)
                task_exists = True
                break

        # If the task doesn't exist, create a new one
        if not task_exists:
            task = {
                'name': task_name,
                'pomodoros': [pomodoro],
            }
            tasks.append(task)
        
        # WRITING TO CSV
        write_to_csv(task_name, pomodoro)

        # Visualise data
        #visualize_pomodoros()

        # Call the run_pomodoro function below starts the pomodoro
        # Number of pomodoros it runs will be equal to cycle length, with the long break after the nth (cycle_length) pomodoro
        # Start of work work time, short break, and long break will be signalled by unique alert sounds
        run_pomodoro(cycle_length, work_time, short_break_time, long_break_time)

        
    
    except KeyboardInterrupt:
        # If the user interrupts the program, print message below and record the current pomodoro to CSV file
        print("\nInterrupted. Writing current pomodoro to file...")
        # Writing pomodoro to CSV file
        write_to_csv(task_name, pomodoro)
        # Visualise data
        #visualize_pomodoros()

