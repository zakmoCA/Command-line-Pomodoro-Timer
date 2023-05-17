import unittest
import math
import argparse
import time
import datetime
import csv
import playsound
import plyer



import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def pomodoro_length():
    while True:
        work_time_in_minutes = input('Enter how many minutes you would like to work?: ')
        break_time_in_minutes = input('Enter how many minutes you would like to rest?: ')

        if not work_time_in_minutes.isdigit() or not break_time_in_minutes.isdigit():
            print("Invalid input, please enter time in minutes")
        else:
            work_time = int(work_time_in_minutes)
            break_time = int(break_time_in_minutes)

            # Return the work and break times for future reference
            return work_time, break_time

def run_pomodoro(work_time, break_time):
    print("Work timer started for", work_time, "minutes")
    countdown(work_time * 60)

    print("\nBreak timer started for", break_time, "minutes")
    countdown(break_time * 60)

pomodoros = []
tasks = []


def start_pomodoro():
    try:
        task_name = input('Enter the name of the task this pomodoro is for: ')
        work_time, break_time = pomodoro_length()  # my pomodoro as defined by pomodoro_length()

        pomodoro = {
            'start_time': datetime.datetime.now(),
            'end_time': datetime.datetime.now() + datetime.timedelta(minutes=work_time),
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

        # Now, write the pomodoro to a CSV file
        with open('pomodoros.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([task_name, pomodoro['start_time'], pomodoro['end_time'], pomodoro['duration']])

        # Now start the timer
        run_pomodoro(work_time, break_time)
    except KeyboardInterrupt:
        print("\nInterrupted. Writing current pomodoro to file...")
        # Now, write the pomodoro to a CSV file
        with open('pomodoros.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([task_name, pomodoro['start_time'], datetime.datetime.now(), pomodoro['duration']])



start_pomodoro()
