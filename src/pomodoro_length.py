def pomodoro_length():
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
        break_time_in_minutes = input('Enter how many minutes you would like to rest?: ')
        if break_time_in_minutes == '':
            print("You must enter how many minutes you would like to rest.")
        elif not break_time_in_minutes.isdigit():
            print("Invalid input for break time, please enter time in minutes.")
        else:
            break_time = int(break_time_in_minutes)
            break

    # Return the work and break times for future reference
    return work_time, break_time
