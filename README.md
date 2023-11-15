# 15/11/23: Refactor

Currently have a pull-request open for this project where I will:
- refactor to improve code quality
- rewrite the project in TypeScript
Mainly refactoring as this was one of my first projects and refactoring will be a great exercise in [building essential dev skills](https://www.youtube.com/watch?v=PGjrn9Ci2aY). Rewriting in TypeScript as am currently learning and building with TypeScript.

## Refactor Objectives

- no global variables, it's still bad practice even for my small personal projects. I should write my personal projects the way I would write in a production codebase, especially since I am yet to learn all the best practices and design patterns (you must first [learn the rules before you can disregard them](https://thoughtbot.com/blog/chestertons-fence#:~:text=Chesterton's%20Fence%20is%20a%20principle,why%20it%20was%20put%20up.)). Keep things [simple](https://grugbrain.dev/).
- modularisation and single responsibility
- more robust error handling
- DRY
- more efficient data handling (opportunity to begin data structures and algorithms journey)

# Help Documentation
## System And Hardware Requirements
This is a very simple application, with any computer or laptop running Python 3 being able to run the application. Python 3 needs to be installed if not already.

## Dependencies

A list of dependencies can be found in the file requirements.txt.

## Installation Steps

### Python Version
The first step is to check which python version, if any, is on your system. Many operating systems have at least Python 2 installed, but this application requires a Python 3 version of 3.11.3 and higher. This can be checked by opening the Terminal (Command Line) and typing the following command:

    python3 --version

If you don't have Python 3.11.3 installed, it can be installed at the official [Python website](https://www.python.org/downloads/)
You can also install it in the terminal as follows:

#### macOS
Open up Homebrew in your terminal and enter the following command:

    brew install python

#### Ubuntu

    sudo apt-get install python3.11

#### Windows
Visit official [Python website](https://www.python.org/downloads/)




If you have Python version 3.11.3 or higher already installed, in your terminal, make a new directory in a location of your choosing and name of your choosing, I am calling mine 'PomodoroApp'.

    mkdir PomodoroApp

Inside this directory, run the following command in order to clone the GitHub Pomodro Application.

    git clone https://github.com/zakmoCA/CLI-Pomodoro.git

Once the repository has been cloned locally to your machine, change to the root directory as follows.

    cd CLI-Pomodoro

Now that you are in the root directory, enter the following command, it will add the appropriate execute persmissions.

    chmod +x setup.sh

Finally, to run the application, proceed by entering the following command.

    ./setup.sh

To exit the pomodoro early simply use 'Ctrl/Cmd' + 'C'. The data will still be written to the csv file.









