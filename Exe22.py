n1 : float = 0
n2 : float = 0

def ordem ():
    global n1
    global n2
    if (n1>n2):
        print (n2,n1)

    elif (n2>n1):
        print (n1,n2)

    else:
        print ("Os numeros digitados são iguais, tente novamente")

def main():
    global n1
    global n2
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero diferente do primeiro: "))
    ordem()

if (__name__ == '__main__'):
    main()  