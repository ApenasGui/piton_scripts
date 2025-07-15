import pyautogui

while True:
    if pyautogui.pixel(472, 193) == (75, 219, 106):
        pyautogui.click()
        break