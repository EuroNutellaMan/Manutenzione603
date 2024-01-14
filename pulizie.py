#
# Display cleanliness
# Last update: 04/11/2023
#

import os
import datetime
from colorama import init, Fore, Style
from time import sleep

init()

YELLOW = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RESET = Style.RESET_ALL

# List rooms and names
rooms = ['Living room','Bathroom','Right bedroom','Front bedroom']
names = []
with open('names.txt', 'r') as file:
    name_list = file.readlines()
for name in name_list:
    names.append(name)


# Statuses
unass = RED + 'Unassigned' + RESET
unclean = RED + 'Not cleaned' + RESET
clean = GREEN + 'Cleaned' + RESET
namelr = ''
namebt = ''
namerb = ''
namefb = ''
lrass = BLUE + namelr + RESET
btass = BLUE + namebt + RESET
rbass = BLUE + namerb + RESET
fbass = BLUE + namefb + RESET
assgnd = [lrass,btass,rbass,fbass]
ass_stat = [unass,unass,unass,unass]
clean_stat = [unclean,unclean,unclean,unclean]

# Function to assign a room to person
def assign():
    for i in range(len(rooms)):
        if clean_stat[i] == unclean and ass_stat[i] not in assgnd:
            print(str(i) + ': ' + rooms[i])
    print('4: Go back')
    rm = int(input('Select room (0-4): '))
    if rm > 4:
        print(RED + 'Invalid choice!' +RESET)
        assign()
    elif rm == 4:
        printr()
    else:
        if ass_stat[rm] == clean or ass_stat[rm] in assgnd:
            print(RED + 'Invalid choice!' + RESET)
            assign()
        for i in range(len(names)):
            print(str(i) + ': ' + names[i])
        print('4: Go back')
        ps = int(input('Select person (0-4): '))
        if ps > 4:
            print(RED + 'Invalid choice!' + RESET)
            assign()
        elif ps == 4:
            assign()
        else:
            if rm == 0:
                namelr = names[ps]
                lrass = BLUE + namelr + RESET
                ass_stat[rm] = lrass
            elif rm == 1:
                namebt = names[ps]
                btass = BLUE + namebt + RESET
                ass_stat[rm] = btass
            elif rm == 2:
                namerb = names[ps]
                rbass = BLUE + namerb + RESET
                ass_stat[rm] = rbass
            elif rm == 3:
                namefb = names[ps]
                fbass = BLUE + namefb + RESET
                ass_stat[rm] = fbass
            printr()

# Function to state a room is clean
def cleaned():
    for i in range(len(rooms)):
        if clean_stat[i] == unclean and ass_stat[i] != unass:
            print(str(i) + ': ' + rooms[i])
    print('4: Go back')
    rm = int(input('Select room that has been cleaned: '))
    if rm > 4:
        print(RED + 'Invalid choice!' + RESET)
        cleaned()
    elif rm == 4:
        printr()
    else:
        if ass_stat[rm] == unass or clean_stat[rm] == clean:
            print(RED + 'Invalid choice!' + RESET)
            cleaned()
        clean_stat[rm] = clean
        printr()

# Function to reset all statuses
def resetter():
    for i in range(len(clean_stat)):
        if clean_stat[i] == unclean:
            shamed = ass_stat[i].strip(BLUE)
            shamed = shamed.strip(RED)
            shamed = shamed.strip(RESET)
            warn = shamed + ' has not cleaned the ' + rooms[i] + '!'
            print(RED + warn + RESET)
            dateunc = str(datetime.datetime.today())
            warn = warn + ' ' + dateunc + '\n'
            with open('wall-of-shame.txt', 'a') as wos:
                wos.write(str(warn))
    print('Resetting statuses...')
    for i in range (len(rooms)):
        ass_stat[i] = unass
        clean_stat[i] = unclean
    print('Resetting variables...')
    namelr = ''
    namebt = ''
    namerb = ''
    namefb = ''
    lrass = BLUE + namelr + RESET
    btass = BLUE + namebt + RESET
    rbass = BLUE + namerb + RESET
    fbass = BLUE + namefb + RESET
    assgnd = [lrass,btass,rbass,fbass]
    sleep(5)
    printr()

# Function to show statuses and input actions
def printr():
    assgnd = [lrass,btass,rbass,fbass]
    os.system('clear')
    print(YELLOW + 'room | assigned to | status' + RESET)
    for i in range(len(rooms)):
        print(YELLOW + rooms[i] + RESET + ' | ' + ass_stat[i] + ' | ' + clean_stat[i])
    print(YELLOW + 'a = assign person to a room.')
    print('c = signal that a room has been cleaned.')
    print('r = reset statuses.' + RESET)
    ans = str(input('Select action: '))
    if ans == 'a':
        assign()
    elif ans == 'c':
        cleaned()
    elif ans == 'r':
        resetter()
    else:
        print(RED + 'Invalid option!' + RESET)
        sleep(2)
        printr()

printr()
