voltas: float = 0
extensao:float = 0
tempo: int = 0

def velomed(v,ex,tp):
    res = ((ex / 1000) / (tp / 60)) / v
    return res

def main():
    global voltas
    global extensao
    global tempo
    voltas = float(input("Digite o numero de voltas realizadas no circuito: "))
    extensao = float(input("Digite o a extensão do circuito em metros: "))
    tempo = float(input("Digite a duração do circuito em minutos: "))

    velomed(voltas,extensao,tempo)
    resultado = velomed(voltas,extensao,tempo)
    print("A velocidade média foi de",resultado,"KM/H")


if(__name__ == '__main__'):
    main()