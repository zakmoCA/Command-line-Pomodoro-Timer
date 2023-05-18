import time

def run_pomodoro(work_time, break_time):
    print("Work timer started for", work_time, "minutes")
    countdown(work_time * 60)

    print("\nBreak timer started for", break_time, "minutes")
    countdown(break_time * 60)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1