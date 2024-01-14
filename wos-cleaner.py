# Cleans the wall of shame every two weeks

from datetime import datetime, timedelta
import os

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

def cleaner():
    cleaned_lines = []
    kept_lines = []
    with open('wall-of-shame.txt','r') as file:
        lines = file.readlines()
    today = datetime.now().date()
    for line in lines:
        parts = line.split()
        logged_date = parse_date(parts[-3])
        if today <= due_date <= today + timedelta(days=14):
            kept_lines.append(line)
        else:
            cleaned_lines.append(line)
    with open('wall-of-shame.txt', 'w') as new_wos:
        new_wos.writelines(kept_lines)
    with open('wos-all.txt', 'a') as record:
        record.writelines(cleaned_lines)

while True:
    if os.path.exists('wall-of-shame.txt'):
        cleaner()
