n1 : float = 0
n2 : float = 0
n3 : float = 0
n4 : float = 0
media: float = 0

def aluno():
    global n1
    global n2
    global n3
    global n4
    media = (n1+n2+n3+n4) / 4

    if (media >= 6):
        print (" Sua media foi,",media, "Aluno Aprovado")
    elif (media >= 3):
        print ("sua media foi,",media,"aluno em exame")
    else:
        print("sua media foi,",media,"Aluno reprovado")

def main():
      global n1
      global n2
      global n3
      global n4

      n1 = float(input("Digite a primeira nota do aluno: "))
      n2 = float(input("Digite a segunda nota do aluno: "))
      n3 = float(input("Digite a terceira nota do aluno: "))
      n4 = float(input("Digite a quarta nota do aluno: "))

      aluno()

      
if (__name__ == '__main__'):
    main()   
