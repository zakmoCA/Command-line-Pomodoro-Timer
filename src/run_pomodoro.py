import time
import os


# new audio files path

class Timer:

    def run_pomodoro(self, cycle_length, work_time, short_break, long_break):
        for i in range(cycle_length):
            print("Work timer started for", work_time, "minutes")
            self.countdown(work_time * 60) 

            if i < cycle_length - 1: # last work period requires long break timer
                print("\nShort break timer started for", short_break, "minutes")
                self.countdown(short_break * 60) 
        
        print("\nLong break timer started for", long_break, "minutes")
        self.countdown(long_break * 60)

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) # Formats mins and secs as 2-digit numbers
            print(timer, end="\r") # Prints timer to console, replacing prev line with end="\r" every second for live self.countdown
            time.sleep(1) # Pause for 1 second for each iteration
            t -= 1 #Decrement remaining time by 1 second
