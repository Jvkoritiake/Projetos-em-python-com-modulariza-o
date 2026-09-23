n1: int = 0
n2: int = 0

def multiplo():
    global n1
    global n2

    if (n1 >= n2 and n1 % n2 == 0):
        print("o",n1," é multiplo de",n2)
    elif(n2 >= n1 and n2 % n1 == 0):
        print ("o",n2," é multiplo de",n1)
    else:
        print("Os numeros não são multiplos")

def main():
    global n1
    global n2
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: ")) 
    multiplo()

if(__name__ == '__main__'):
    main()