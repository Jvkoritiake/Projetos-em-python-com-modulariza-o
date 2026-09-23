n1: int = 0
n2: int = 0
res: int = 0

def maior ():
    global n1
    global n2    
    if (n1 > n2):
        res = n1
        print ("o maior número é:",res)

    elif (n1 == n2):
        print ("Os numeros são iguais ")

    else:
        res = n2
        print ("o maior número é:",res)

def main():
    global n1
    global n2
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))    
    maior()

if (__name__ == '__main__'):
    main()

