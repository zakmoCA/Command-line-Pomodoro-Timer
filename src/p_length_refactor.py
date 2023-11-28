def user_preferences():
  print("Pomodoro timers involve short breaks and long breaks.\nA 'cycle' refers to how many pomodoros you complete before your long break.")
  print("For example a cycle length of '4' means you will have your 'long break' after your 4th pomodoro,\nand the first 3 pomodors will be followed by a 'short break'.")
  
  cycle_length = get_cycle_length() 
  work_times = get_work_time()
  break_times = get_break_times()










def get_cycle_length():
    length_of_cycle = input("Enter how many pomodoros you want in this 'cycle': ")
    if length_of_cycle == '':
        print("You must enter a number for your 'cycle length'.")
    elif not length_of_cycle.isdigit():
        print("Invalid input for cycle length, please enter a number.")
    else:
        cycle_length = int(length_of_cycle)
        break
    return cycle_length

def get_work_time():
    work_time_in_minutes = input('Enter how many minutes you would like to work?: ')
    if work_time_in_minutes == '':
        print("You must enter how many minutes you would like to work.")
    elif not work_time_in_minutes.isdigit():
        print("Invalid input for work time, please enter time in minutes.")
    else:
        work_time = int(work_time_in_minutes)
        break
    return work_time

def get_break_times():
    short_break_time_in_minutes = input('Enter how many minutes you would like to rest for your short break?: ')
    if short_break_time_in_minutes == '':
        print("You must enter how many minutes you would like to rest for your short break.")
    elif not short_break_time_in_minutes.isdigit():
        print("Invalid input for short break time, please enter time in minutes.")
    else:
        short_break_time = int(short_break_time_in_minutes)
        break

    long_break_time_in_minutes = input('Enter how many minutes you would like to rest for your long break?: ')
    if long_break_time_in_minutes == '':
        print("You must enter how many minutes you would like to rest for your long break.")
    elif not long_break_time_in_minutes.isdigit():
        print("Invalid input for long break time, please enter time in minutes.")
    else:
        long_break_time = int(long_break_time_in_minutes)
        break
    
    return short_break_time, long_break_time

