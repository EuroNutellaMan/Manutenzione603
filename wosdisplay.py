#
# Display wall of shame
# last updated 04/11/2023
#

import os
import pyfiglet
from time import sleep
from colorama import init, Fore, Style

init()

# Wall of shame text stylings
figlet = pyfiglet.Figlet(font='poison')

wallof = figlet.renderText("Wall of")
shame = figlet.renderText("  SHAME")

RED = Fore.RED + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RESET = Style.RESET_ALL

# Function for the display
def display():
    # Clears the terminal
    os.system('clear')
    
    # Print the text
    print(RED)
    print(wallof)
    print(shame)
    print(RESET)
    
    if os.path.exists('wall-of-shame.txt') == True:
        # List last 5 shameful individuals
        with open('wall-of-shame.txt', 'r') as wos:
            shamed = wos.readlines()
        for line in shamed[-5:]:
            line = line.strip('\n')
            print(RED + line + RESET)
    else:
        print(GREEN + 'No shameful individuals found!' + RESET)
    
    # Reloads every 6 hours
    sleep(21600)
    display()

display()