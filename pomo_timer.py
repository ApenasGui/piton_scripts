import time
from plyer import notification

def notificar(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        timeout = 10
    )

def contagem_regressiva(minutos):
    segundos = minutos * 60
    while segundos:
        mins, secs = divmod(segundos, 60)
        tempo = f"{mins:02d}:{secs:02d}"
        print(f"tempo restante : {tempo}", end='')
        time.sleep(1)
        segundos -= 1
    print()


def pomodoro(ciclos=4):
    for i in range(1, ciclos + 1):
        print(f"iniciando pomodoro {i}")
        notificar("Pomodoro iniciado", "Foco total por 25 minutos")
        contagem_regressiva(25)

        print(f"Hora da pausa")
        notificar("Pausa!", "Descanse por 5 minutos")
        contagem_regressiva(5)

pomodoro(ciclos=1)