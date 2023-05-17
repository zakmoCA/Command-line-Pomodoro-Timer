import unittest
import math
import argparse
import time
import datetime
import csv
import playsound
import plyer

class Pomodoro:
    def __init__(self, task, work_time):
        self.task = task
        self.work_time = work_time
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def stop(self):
        self.end_time = datetime.datetime.now()

    def duration(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60  # duration in minutes
        else:
            return 0


class Task:
    def __init__(self, name):
        self.name = name
        self.pomodoros = []

    def add_pomodoro(self, pomodoro):
        self.pomodoros.append(pomodoro)

    def total_time(self):
        return sum(pomodoro.duration() for pomodoro in self.pomodoros)

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def time_remaining(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            return self.duration - elapsed_time
        else:
            return self.duration

    def is_finished(self):
        if self.start_time:
            return self.time_remaining() <= 0
        else:
            return False


class DataManager:
    pass

class PomodoroApplication:
    pass

