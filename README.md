# Roblox Shortcuts Creator
A simple Qt5 app to add Roblox game shortcuts to Windows desktop, running in Python.

## Preview

![clip1-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/9ced974d-eaef-4af9-8784-0e3e28cddd4d)
![clip2-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/a7b149b3-74f5-472a-a53f-444f8dac1a1b)

## Why making this?
Roblox, without a question, is one of the most commonly used game launchers on Windows. Weirdly enough, unlike Steam or Epic Games launcher, Roblox has never had a native feature to add games to the desktop, which can be overwhelming if you only want to play one game. You can paste the URL scheme of the game into the Run command or even use that to create a new shortcut; however, the process is not the fastest because you would want to manually provide game data to that, namely its name, its icon/avatar, and its URL scheme. Too many steps. That's what inspired me to create a simple app that performs all these steps with just one click, using a URL.


## Requirements
python >= 3.10 (required by the `pillow` library)


## How to run
1. ‌Install required libraries
```bash
pip install -r requirements.txt
```

2. Run the script

**Using the terminal**
```bash
python3 main.py
```
or
```bash
python main.py
```

**Running directly without the terminal**

Double click on `main.pyw`
