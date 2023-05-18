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