hora_inicio: int = 0
minuto_inicio: int = 0
hora_final: int = 0
minuto_final: int = 0
inicio_minutos: int = 0
final_minutos: int = 0
duracao_minutos: int = 0
horas: int = 0
minutos: int = 0


def calcular():
    global hora_inicio, minuto_inicio, hora_final, minuto_final
    global inicio_minutos, final_minutos, duracao_minutos
    global horas, minutos

    hora_inicio = int(input("Digite a hora de início: "))
    minuto_inicio = int(input("Digite os minutos de início: "))

    hora_final = int(input("Digite a hora de final: "))
    minuto_final = int(input("Digite os minutos de final: "))

    inicio_minutos = (hora_inicio * 60) + minuto_inicio
    final_minutos = (hora_final * 60) + minuto_final

    if (final_minutos <= inicio_minutos):
        final_minutos = final_minutos + (24 * 60)

    duracao_minutos = final_minutos - inicio_minutos

    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60

    print("O jogo durou", horas, "hora(s) e", minutos, "minuto(s)")


def main():
    calcular()


if(__name__ == '__main__'):
    main()