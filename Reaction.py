import pyautogui
import time
#Slow but working protype, hove your mouse over human benchmark and it will auto play
while True:
    currentMouse = pyautogui.position()
    clickColor = (119,216,119)
    blueColor = (71,133,203)
    if(pyautogui.pixelMatchesColor(currentMouse.x * 2,currentMouse.y * 2, clickColor) or (pyautogui.pixelMatchesColor(currentMouse.x * 2,currentMouse.y * 2, blueColor))):
        pyautogui.leftClick(currentMouse.x, currentMouse.y)
    