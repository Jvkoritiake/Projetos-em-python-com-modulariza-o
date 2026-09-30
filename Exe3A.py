def fatorial(num):
    i = 1
    fat = 1
    while(i <= num):
        fat = fat * i
        i = i+1

    return fat

def main():
    n = int(input("Digite um numero para saber seu fatorial: "))
    resultado = fatorial(n)
    print("Seu fatorial é: ", resultado)

if(__name__ == '__main__'):
    main()   