import pyautogui
import time

texto = "No meio do caminho tinha uma pedra"
texto2 = "tinha uma pedra no meio do caminho"
texto3 = "tinha uma pedra"
texto4 = "no meio do caminho tinha uma pedra."
texto5 = "Nunca me esquecerei desse acontecimento"
texto6 = "na vida de minhas retinas tão fatigadas."
texto7 = "Nunca me esquecerei que no meio do caminho"
texto8 = "tinha uma pedra"
texto9 = "tinha uma pedra no meio do caminho"
texto10 = "no meio do caminho tinha uma pedra."

poema = [texto, texto2, texto3, texto4, texto5, texto6, texto7, texto8, texto9, texto10]

print("Coloca o mouse no lugar que deseja auto escrever o(s) texto(s)")
time.sleep(5)

for msg in poema:
    pyautogui.write(msg, interval=0.01)
    pyautogui.press('enter')
