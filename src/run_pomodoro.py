import time
from playsound import playsound 
import os

# Need absolute path for my audio files since my bash script is not in this directory
AUDIO_BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_pomodoro(cycle_length, work_time, short_break_time, long_break_time):
    for _ in range(cycle_length):
      print("Work timer started for", work_time, "minutes")
      countdown(work_time * 60)
      playsound(os.path.join(AUDIO_BASE_DIR, 'break-start.wav'))

      print("\nShort break timer started for", short_break_time, "minutes")
      countdown(short_break_time * 60)
      playsound(os.path.join(AUDIO_BASE_DIR, 'pomodoro-start.wav'))
    
    print("\nLong break timer started for", long_break_time, "minutes")
    countdown(long_break_time * 60)
    playsound(os.path.join(AUDIO_BASE_DIR, 'end-of-long-break.wav'))

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1