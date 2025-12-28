import sys
import pyautogui
from mss import mss
import time

pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0
mss = mss()

print("Bot Active!")
print("Go to https://humanbenchmark.com/tests/reactiontime and start the game")

count = 0
try:
    while True:
        pos = pyautogui.position()
        clickColor = (119,216,119)
        blueColor = (71,133,203)
        region = (pos.x, pos.y, pos.x + 1, pos.y + 1)
        st = mss.grab(region)
        current_pixel = st.pixel(0,0)
        if current_pixel == clickColor:
            print("CLICKED")
            pyautogui.click(pos.x, pos.y, _pause=False)
            count += 1
        if count >= 5:
            print("Game Finished!, Exiting Program...")
            sys.exit()
except:
    print("Program Exited")