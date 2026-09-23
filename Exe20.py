import math
a: float = 0
b: float = 0
c: float = 0
delta: float = 0
x1: float = 0
x2: float = 0
rzdelta: float = 0

def equacao():
       global a
       global b
       global c
       delta = (b * b) - (4 * a * c)

       if delta > 0:
             rzdelta = math.sqrt(delta)
             x1 = (-b + rzdelta) / (2 * a)
             x2 = (-b - rzdelta) / (2 * a)
             print("As raízes reais são:",x1 , x2)

       elif (delta == 0):
              x1 = (-b + rzdelta) / (2 * a)
              print("As duas raízes reais são iguais:",x1)

       else:
            print("Não há raiz real")

def main():
      global a
      global b
      global c
      a = float(input("Digite o coeficiente A:"))
      b = float(input("Digite o coeficiente B:"))
      c = float(input("Digite o coeficiente C:"))
      equacao()

      
    
if (__name__ == '__main__'):
    main()