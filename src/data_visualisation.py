import pandas as pd
import matplotlib.pyplot as plt

def visualize_pomodoros():
    # Load the data from CSV
    df = pd.read_csv('pomodoros.csv')

    # Group by task and count the number of pomodoros
    pomodoro_counts = df.groupby('task').size()

    # Plot the data
    pomodoro_counts.plot(kind='bar')

    # Set the title and labels
    plt.title('Pomodoros per Task')
    plt.xlabel('Task')
    plt.ylabel('Number of Pomodoros')

    # Show the plot
    plt.show()
