#
# Display log expenses
# last updated 04/11/2023
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

# Variable for total money in the jar
if os.path.exists('MoneyInJar.txt') == False:
    total = 0
else:
    with open('MoneyInJar.txt', 'r') as moneyfile:
        total = moneyfile.read()
    total = float(total)

# List of names and loglines
names = ['Lorenzo','Abdu','Serhat','Hasnain']
logs = []
if os.path.exists('MoneyLog.txt') == False:
    logs = []
else:
    with open('MoneyLog.txt', 'r') as moneylog:
        lgs = moneylog.readlines()
        for line in lgs:
            line = line.strip('\n')
            components = line.split(' ')
            if '+' in components[0]:
                logline = GREEN + components[0] + RESET + ' ' + BLUE + components[1] + RESET + ' ' + YELLOW + components[2] + ' ' + components[3] + RESET
            elif '-' in components[0]:
                logline = RED + components[0] + ' ' + components[1] + RESET + ' ' + BLUE + components[2] + RESET + ' ' + YELLOW + components[3] + ' ' + components[4] + RESET
            logs.append(logline)

# Function to add money
def AddMon():
    global total
    os.system('clear')
    var = input('How much money did you put in the jar? [ex. 2.50] ')
    if ',' in var:
        print(RED + 'Wrong format, use "." instead of ","' + RESET)
        sleep(3)
        AddMon()
    else:
        var = var.strip(' \t\n\r')
        var = float(var)
        svar = GREEN + '+€' + str(var) + RESET
    for i in range(len(names)):
        print(YELLOW + str(i) + ': ' + names[i] + RESET)
    naddr = int(input('Who are you? [0-3] '))
    if naddr >= 4:
        print(RED + 'Invalid input! Try again.' + RESET)
        sleep(3)
        AddMon()
    else:
        addr = BLUE + names[naddr] + RESET
    date = YELLOW + str(datetime.datetime.today()) + RESET
    logline = svar + ' ' + addr + ' ' + date
    print(logline)
    cnfrm = input('Confirm? [y/n] ')
    if cnfrm == 'y':
        logs.append(logline)
        total = round(total + var, 2)
        with open('MoneyInJar.txt', 'w') as moneyfile:
            moneyfile.write(str(total))
        logline = logline + '\n'
        with open('MoneyLog.txt', 'a') as moneylog:
            moneylog.write(str(logline))
        loggr()
    else:
        rtr = input('Retry? [y/n] ')
        if rtr == 'y':
            AddMon()
        else:
            loggr()

# Function to remove money
def RemMon():
    global total
    os.system('clear')
    var = input('How much money did you take from the jar? [ex. 2.50] ')
    if ',' in var:
        print(RED + 'Wrong format, use "." instead of ","' + RESET)
        sleep(3)
        RemMon()
    else:
        var = var.strip(' \t\n\r')
        var = float(var)
        svar = RED + '-€' + str(var) + RESET
    item = input('What did you buy? ')
    item = RED + item + RESET
    for i in range(len(names)):
        print(YELLOW + str(i) + ': ' + names[i] + RESET)
    naddr = int(input('Who are you? [0-3] '))
    if naddr >= 4:
        print(RED + 'Invalid input! Try again.' + RESET)
        sleep(3)
        RemMon()
    else:
        addr = BLUE + names[naddr] + RESET
    date = YELLOW + str(datetime.datetime.today()) + RESET
    logline = svar + ' ' + item + ' ' + addr + ' ' + date
    print(logline)
    cnfrm = input('Confirm? [y/n] ')
    if cnfrm == 'y':
        logs.append(logline)
        total = round(total - var, 2)
        with open('MoneyInJar.txt', 'w') as moneyfile:
            moneyfile.write(str(total))
        logline = logline + '\n'
        with open('MoneyLog.txt', 'a') as moneylog:
            moneylog.write(str(logline))
        loggr()
    else:
        rtr = input('Retry? [y/n] ')
        if rtr == 'y':
            RemMon()
        else:
            loggr()

# Function to show logs
def loggr():
    os.system('clear')
    for logline in logs[-20:]:
        print(logline)
    print(YELLOW + 'a = Added money to jar (one person at a time)')
    print('r = Removed money from the jar (one item at a time)' + RESET)
    inpt = input('Select operation: [a/r] ')
    if inpt == 'a':
        AddMon()
    elif inpt == 'r':
        RemMon()
    else:
        print(RED + 'Invalid Input! Try Again!' + RESET)
        sleep(3)
        loggr()

loggr()
