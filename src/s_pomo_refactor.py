from p_length_refactor import user_preferences
import datetime
from run_pomodoro import run_pomodoro
from write_to_csv import write_to_csv


def start():

    pomodoros = [] 
    tasks = [] 

    try:
        while True:
          task_name = input('Enter the name of the task this pomodoro is for: ')
          if task_name:
              break
          else:
              print("You must enter a task name. Please try again.")
        cycle_length, work_time, short_break, long_break = user_preferences()  

        pomodoro = {
            'start_time': datetime.datetime.now().replace(microsecond=0),
            'end_time': datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(minutes=work_time),
            'duration': work_time,
            'task': task_name,
        }
        pomodoros.append(pomodoro)

        # if the task already exists append pomodoro to task
        task_exists = False
        for task in tasks:
            if task['name'] == task_name:
                task['pomodoros'].append(pomodoro)
                task_exists = True
                break

        if not task_exists:
            task = {
                'name': task_name,
                'pomodoros': [pomodoro],
            }
            tasks.append(task)
        
        write_to_csv(task_name, pomodoro)

        run_pomodoro(cycle_length, work_time, short_break, long_break)

    except KeyboardInterrupt:
        print("\nInterrupted. Writing current pomodoro to file...")
        write_to_csv(task_name, pomodoro)


