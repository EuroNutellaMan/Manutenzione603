## Requirements:

These programs are designed to run on Linux.
You will need tmux installed.
You will need the python modules listed in requirements.txt.

## Installation:

0a. Install tmux, on Linux Mint, Ubuntu, Debian and derivatives this can be done with this command:

```
sudo apt install tmux
```

0b. Install all python dependencies:

```
pip install -r requirements.txt 
```

1. Clone this repository in your preferred path:

```
git clone https://github.com/EuroNutellaMan/Manutenzione603.git
```

2. Set an alias for your terminal (optional):

```
nano .bashrc
```

then write:

```
alias man603='cd /path/to/Manutenzione603 && python3 starter.py'
```

then close and reopen the terminal

## Usage:

If you set up an alias just type man603, otherwise navigate to the directory in which you cloned the repo:

```
cd /path/to/Manutenzione603
```

then run:

```
python3 starter.py
```

## Notes:

I will not be maintaining this project any further, I haven't had the time to test some features but I hope they work. You're free to do whatever you want with these programs.
