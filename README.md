# Help Documentation
## System And Hardware Requirements
This is a very simple application, with any computer or laptop running Python 3 being able to run the application. Python 3 needs to be installed if not already.

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




If you have Python version 3.11.3 or higher already installed, in your terminal, navigate to the 
directory you would like to clone this repo into.

Inside this directory, run the following command in order to clone the GitHub Pomodro Application.

    git clone https://github.com/zakmoCA/CLI-Pomodoro.git

Once the repository has been cloned locally to your machine, navigate to the repo's root.

    cd CLI-Pomodoro

Now that you are in the root directory, enter the following command, it will add the appropriate execute persmissions.

    chmod +x setup.sh

Finally, to run the application, enter the following command.

    ./setup.sh











