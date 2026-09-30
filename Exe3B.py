def fatorial(num):
    i = 1
    fat = 1

    while i <= num:
        fat = fat * i
        i = i + 1

    return fat


def divisao(num1, num2):
    return num1 / num2


def main():
    n = int(input("Digite o valor de N: "))

    resultado = 1
    i = 1

    while i <= n:
        fat = fatorial(i)
        resultado = resultado + divisao(1, fat)
        i = i + 1

    print("Resultado:", resultado)


if __name__ == '__main__':
    main()