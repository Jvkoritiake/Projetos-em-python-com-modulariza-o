
def rendimento(tipo,val):
    res : float = 0
    if (tipo == 1):
        res = val * 1.03
        return res
    
    elif (tipo == 2):
        res = val * 1.05
        return res
    
    else:
        return "tipo de investimento invalido"

def main():
    print("1 = poupança ; 2 = renda fixa")
    tipoin = int(input("Digite o tipo de investimento: "))
    inv = float(input("Digite qual valor deseja investir: "))

    resultado = rendimento(tipoin,inv)
    if tipoin == 1 or tipoin == 2:
        print("Com esse investimento, o valor será:", resultado)
    else:
        print(resultado)

if(__name__ == '__main__'):
    main()   