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
    if extrai_carta(baralho[i]) == extrai_carta(baralho[i-1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]):
        resultado = [1]
    if extrai_carta(baralho[i]) == extrai_carta(baralho[i-3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]):
        resultado = [3]