num:int = 0

def divisivel():
    global num

    if (num % 2 == 0 and num % 3 == 0):
        print(" O número",num,"é divisivel por 2 e por 3")
    elif (num % 2 == 0):
        print(" O número",num,"é divisivel só por 2")
    elif (num % 3 == 0):
        print(" O número",num,"é divisivel só por 3")
    else:
        print("O número não é divisivel por 2 e nem por 3")

def main():
    global num
    num = float(input("Digite um numero para saber se é divisivel por 2 ou 3: "))
    divisivel()

if(__name__ == '__main__'):
    main()  
   