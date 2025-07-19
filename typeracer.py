import pyautogui
import pyperclip
import time

texto = 'And when the broken hearted people living in the world agree. ' \
'There will be an answer, let it be. For though they may be parted, there is still a chance that they will see. ' \
'There will be an answer, let it be.'

print("Coloca o mouse no lugar que deseja auto escrever o(s) texto(s)")
time.sleep(5)

for palavra in texto.split():
    pyautogui.write(palavra, interval=0.05)
    pyautogui.press('space')