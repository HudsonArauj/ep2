def cria_baralho():
    cartas =['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    return cartas

def extrai_naipe(carta):
    if len(carta)>2:
        naipe = carta[2]
    else:
        naipe = carta[1]
    return naipe

def extrai_valor(carta):
    if len(carta)>2:
        valor = carta[0]+carta[1]
    else:
        valor = carta[0]
    return valor

def lista_movimentos_possiveis(baralho, i):
    v = extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-3])
    n = extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-1])
    if i == 0:
        resultado = []
    elif i>=3 and v and n:
        resultado =[1, 3]
    elif n:
        resultado = [1]
    elif i>=3 and v:
        resultado = [3] 
    else:
        resultado = []
    return resultado