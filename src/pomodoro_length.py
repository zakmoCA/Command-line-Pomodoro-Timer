def pomodoro_length():

    while True:
        print("Pomodoro timers involve short breaks and long breaks.\nA 'cycle' refers to how many pomodoros you complete before your long break.")
        print("For example a cycle length of '4' means you will have your 'long break' after your 4th pomodoro,\nand the first 3 pomodors will be followed by a 'short break'.")
        cycle_length_input = input("Enter how many pomodoros you want in this 'cycle': ")
        if cycle_length_input == '':
            print("You must enter a number for your 'cycle length'.")
        elif not cycle_length_input.isdigit():
            print("Invalid input for cycle length, please enter a number.")
        else:
            cycle_length = int(cycle_length_input)
            break    

    while True:
        work_time_in_minutes = input('Enter how many minutes you would like to work?: ')
        if work_time_in_minutes == '':
            print("You must enter how many minutes you would like to work.")
        elif not work_time_in_minutes.isdigit():
            print("Invalid input for work time, please enter time in minutes.")
        else:
            work_time = int(work_time_in_minutes)
            break

    while True:
        short_break_time_in_minutes = input('Enter how many minutes you would like to rest for your short break?: ')
        if short_break_time_in_minutes == '':
            print("You must enter how many minutes you would like to rest for your short break.")
        elif not short_break_time_in_minutes.isdigit():
            print("Invalid input for short break time, please enter time in minutes.")
        else:
            short_break_time = int(short_break_time_in_minutes)
            break
    
    while True:
        long_break_time_in_minutes = input('Enter how many minutes you would like to rest for your long break?: ')
        if long_break_time_in_minutes == '':
            print("You must enter how many minutes you would like to rest for your long break.")
        elif not long_break_time_in_minutes.isdigit():
            print("Invalid input for long break time, please enter time in minutes.")
        else:
            long_break_time = int(long_break_time_in_minutes)
            break

    # Return the work and break times for future reference
    return cycle_length, work_time, short_break_time, long_break_time
