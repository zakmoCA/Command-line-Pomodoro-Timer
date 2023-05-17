import unittest
import math
import argparse
import time
import datetime
import csv
import playsound
import plyer



def pomodoro_length():
    while True:
        # instructions will be in the help documentation
        work_time_in_minutes = input('Enter how many minutes you would like to work?: ')
        break_time_in_minutes = input('Enter how many minutes you would like to rest?: ')
        
        if not work_time_in_minutes.isdigit() or not break_time_in_minutes.isdigit():
            print("Invalid input, please enter time in minutes")
        else:
            pomodoro_settings = (int(work_time_in_minutes), int(break_time_in_minutes)) 
            
            return pomodoro_settings

work_time, break_time = pomodoro_length()
print("Work time: ", work_time)
print("Break time: ", break_time)


    





# Tests
