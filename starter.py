# starts the applications

import subprocess
import time

def run_command_in_tmux(command, window_name, pane):
    tmux_command = f'tmux send-keys -t {window_name}:{pane} "{command}" C-m'
    subprocess.run(tmux_command, shell=True)

def main():
    # Start tmux session
    subprocess.run(['tmux', 'new-session', '-d', '-s', 'my_session'])

    # Define the programs and their locations in the grid
    programs = [
        ('moneydisplay.py', 'top-left'),
        ('wosdisplay.py', 'top-right'),
        ('logspese.py', 'bottom-left'),
        ('pulizie.py', 'bottom-right'),
        ('wos-cleaner', 'background'),
    ]

    # Run commands in tmux panes
    for program, location in programs[:-1]:  # Skip the last program for background
        run_command_in_tmux(program, 'my_session', location)

    # Sleep for a moment to allow the programs in the visible panes to start
    time.sleep(1)

    # Run the last program in the background
    background_program = programs[-1][0]
    subprocess.run([background_program])
