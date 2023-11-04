#
# Money display
# last updated 04/11/2023
#

import os
import pyfiglet
from time import sleep
from colorama import init, Fore, Style

init()

# Stylings
figlet = pyfiglet.Figlet(font='colossal')

YELLOW = Fore.YELLOW + Style.BRIGHT
RESET = Style.RESET_ALL

# Get width of terminal
terminal_size = os.get_terminal_size()
terminal_width = terminal_size.columns

# Centers text
text = 'Press CTRL+B then ←, ↑, →, or ↓ to navigate between the screens'
spaces = (terminal_width - len(text)) // 2
text = ' ' * spaces + text

# Function for the display
def display():
    # Clears the terminal
    os.system('clear')

    # Stylizes the money text
    with open('MoneyInJar.txt', 'r') as moneyfile:
        amount = moneyfile.read()
    money = str(amount)
    dispmn = figlet.renderText(money)

    # Prints the text
    print(YELLOW)
    print(dispmn)
    print(RESET)
    print(YELLOW + text + RESET)

    # Reloads every 2 hours
    sleep(7200)
    display()

display()
