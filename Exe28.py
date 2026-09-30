preço : float = 0
mediames : float = 0


def preçonovo(val,vendas):
    res : float = 0 
    if (vendas < 500 and val < 30):
        res = val * 1.10
        return res 

    elif ((vendas >= 500 and vendas < 1000 ) and (val >= 30 and val < 80)):
        res = val * 1.15
        return res

    elif((vendas >= 1000 and val >= 80)):
        res = preço * 0.95
        return res

    else:
        res = val 
        return res

def main():
    global preço
    global mediames 
    preço = float(input("Digite o preço atual do produto: "))
    mediames = float(input("Digite a media mensal de venda do produto: "))
    preçonovo(preço,mediames)
    resultado = preçonovo(preço,mediames)

    print("O novo preço do produto é", resultado)

if(__name__ == '__main__'):
    main()