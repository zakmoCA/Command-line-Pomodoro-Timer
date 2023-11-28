import time
import os

# Need absolute path for my audio files since my bash script is not in this directory
AUDIO_BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_pomodoro(cycle_length, work_time, short_break_time, long_break_time):
    # This function takes cycle length, work time, short break time, and long break time as arguments
    # For each pomodoro cycle, it starts a work timer, then a short break timer
    # This is repeated until we reach pomodoro #cycle length, then long break timer is started
    # Each stage is signaled by a unique audio alert

    for i in range(cycle_length):
        print("Work timer started for", work_time, "minutes")
        countdown(work_time * 60) # Run countdown for work time

        if i < cycle_length - 1:  # Check that it's not the last work period
            print("\nShort break timer started for", short_break_time, "minutes")
            countdown(short_break_time * 60) # Run countdown for short break time
      
    print("\nLong break timer started for", long_break_time, "minutes")
    countdown(long_break_time * 60) # Run countdown for long break time

def countdown(t):
    #This function takes an amount of time in seconds and counts down to zero
    #It prints the remaining time every second
    while t:
        # While loop runs as long as t (time in seconds) > 0
        mins, secs = divmod(t, 60) #Divmod splits total seconds into mins and remaining secs and formats to give our timer
        timer = '{:02d}:{:02d}'.format(mins, secs) # Formats mins and secs as 2-digit numbers
        print(timer, end="\r") # Prints timer to console, replacing prev line with end="\r" every second for live countdown
        # Print statement does this by bringing cursor to start of line, therefore overwriting prev timer line
        time.sleep(1) # Pause for 1 second for each iteration
        t -= 1 #Decrement remaining time by 1 second