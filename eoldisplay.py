#
# Display for EoL
# last updated 06/12/2023
#

import os
from time import sleep
from colorama import init, Fore, Style
import pyfiglet

init()

# Stylings
figlet = pyfiglet.Figlet(font='poison')

attention = figlet.renderText("  WARNING")

# Colors
RED = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

# Display
os.system('clear')
print(RED)
print(attention)
print()
print(" Because of the upcoming move to room 311, due to issues in the right bedroom, ")
print("these programs will no longer be available after the move. I recommend that you")
print("write whatever's important down somewhere else. The move will be definitive but")
print("                    we don't know exactly when it will happen                  ")
print("                                      -Lorenzo                                 ")
print(RESET)

# Waiter
a = 1
while a == 1:
	sleep(10000)
