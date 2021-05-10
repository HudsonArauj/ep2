import random
def cria_baralho():
    cartas =['\033[2;34mA♠\033[m', '\033[2;34m2♠\033[m', '\033[2;34m3♠\033[m', '\033[2;34m4♠\033[m', '\033[2;34m5♠\033[m', '\033[2;34m6♠\033[m', '\033[2;34m7♠\033[m', '\033[2;34m8♠\033[m', '\033[2;34m9♠\033[m', '\033[2;34m10♠\033[m', '\033[2;34mJ♠\033[m', '\033[2;34mQ♠\033[m', '\033[2;34mK♠\033[m', '\033[1;31mA♥\033[m', '\033[1;31m2♥\033[m', '\033[1;31m3♥\033[m', '\033[1;31m4♥\033[m', '\033[1;31m5♥\033[m', '\033[1;31m6♥\033[m', '\033[1;31m7♥\033[m', '\033[1;31m8♥\033[m', '\033[1;31m9♥\033[m', '\033[1;31m10♥\033[m', '\033[1;31mJ♥\033[m', '\033[1;31mQ♥\033[m', '\033[1;31mK♥\033[m', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    random.shuffle(cartas)
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

def lista_movimentos_possiveis(baralho,i):
    lista_possiveis =[]
    if i ==0:
        return lista_possiveis
    if len(baralho) <4:
        if extrai_naipe(baralho[i])== extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]):
            lista_possiveis.append(1)
    elif len(baralho)>3:
        if extrai_naipe(baralho[i])== extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]):
            lista_possiveis.append(1) 
        if (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-3])) and (i-3) >=0:
            lista_possiveis.append(3)
    return lista_possiveis

def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    possibilidades = False
    for i in range(len(baralho)):
        if len(lista_movimentos_possiveis(baralho,i)) != 0:
            possibilidades = True
    return possibilidades   


    
