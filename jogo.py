import funcoes_paciencia

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;33m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


print('Paiciencia acordeao')
print('='*30)
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! \nO objetivo é empilhar todas as cartas.\n\n')

print('Existem apenas dois movimentos: \n1. Empilhar uma carta sobre a anterior \n2. Empilhar uma carta sobre a terceira carta anterior\n\n')
print('Para que o movimento possa ser realizado basta que uma das condições sejam atendidas:\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe.\n\n')
print('Se alguma condição anterior é satisfeita,\nqualquer carta pode ser movimentada\n\n')
inicio = input('Aperte [Enter] para iniciar o jogo! ')

resposta = 'sim'
while resposta == 'sim':
    print('o estado atual do baralho é:')
    baralho = funcoes_paciencia.cria_baralho()
    while funcoes_paciencia.possui_movimentos_possiveis(baralho) != False:    
        for i in range(len(baralho)):
            carta = baralho[i]
            if funcoes_paciencia.extrai_naipe(carta) == '♠':
                carta = BLUE + carta + RESET
            elif funcoes_paciencia.extrai_naipe(carta) == '♥':
                carta = RED + carta + RESET
            elif funcoes_paciencia.extrai_naipe(carta) == '♦':
                carta = CYAN + carta + RESET
            else:
                carta = GREEN + carta + RESET
            print('{0}. {1}'.format(i+1, carta))
        entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
        aux = True
        while aux:
            try:
                entrada = int(entrada)
            except ValueError:
                entrada = -1
            if int(entrada) >= len(baralho)+1 or int(entrada) <= 0:
                entrada = input('Entrada inválida. Escolha um numero de 1 a {}: '.format(len(baralho)))
            else:
                aux = False
    
        possibilidades = funcoes_paciencia.lista_movimentos_possiveis(baralho, int(entrada)-1)
        while len(possibilidades) == 0:
            carta = baralho[int(entrada)-1]
            if funcoes_paciencia.extrai_naipe(carta) == '♠':
                carta = BLUE + carta + RESET
            elif funcoes_paciencia.extrai_naipe(carta) == '♥':
                carta = RED + carta + RESET
            elif funcoes_paciencia.extrai_naipe(carta) == '♦':
                carta = CYAN + carta + RESET
            else:
                carta = GREEN + carta + RESET
            print("A carta {} não pode ser movida".format(carta))
            entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
            possibilidades = funcoes_paciencia.lista_movimentos_possiveis(baralho, int(entrada)-1)
        
        if len(possibilidades) == 2:
            carta1 = baralho[int(entrada)-1]
            carta2 = baralho[int(entrada)-2]
            carta3 = baralho[int(entrada)-4]
            if funcoes_paciencia.extrai_naipe(carta1) == '♠':
                carta1 = BLUE + carta1 + RESET
            elif funcoes_paciencia.extrai_naipe(carta1) == '♥':
                carta1 = RED + carta1 + RESET
            elif funcoes_paciencia.extrai_naipe(carta1) == '♦':
                carta1 = CYAN + carta1 + RESET
            else:
                carta1 = GREEN + carta1 + RESET
            print("Escolha sobre qual carta você que empilhar o {}".format(carta1))
            if funcoes_paciencia.extrai_naipe(carta2) == '♠':
                carta2 = BLUE + carta2 + RESET
            elif funcoes_paciencia.extrai_naipe(carta2) == '♥':
                carta2 = RED + carta2 + RESET
            elif funcoes_paciencia.extrai_naipe(carta2) == '♦':
                carta2 = CYAN + carta2 + RESET
            else:
                carta2 = GREEN + carta2 + RESET
            print('{0}. {1}'.format(1, carta2))
            if funcoes_paciencia.extrai_naipe(carta3) == '♠':
                carta3 = BLUE + carta3 + RESET
            elif funcoes_paciencia.extrai_naipe(carta3) == '♥':
                carta3 = RED + carta3 + RESET
            elif funcoes_paciencia.extrai_naipe(carta3) == '♦':
                carta3 = CYAN + carta3 + RESET
            else:
                carta3 = GREEN + carta3 + RESET
            print('{0}. {1}'.format(2, carta3))
            escolha2 = ''
            while escolha2 != '1' and escolha2 != '2':
                escolha2 = input('Digite o número de sua escolha (1 ou 2): ')
                if escolha2 == '1':
                    baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-2)
                    print('o estado atual do baralho é:')
                elif escolha2 == '2':
                    baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-4)
                    print('o estado atual do baralho é:')
                else:
                    print('Escolha inválida!')
                    print("Escolha sobra qual carta você que empilhar o {}".format(baralho[int(entrada)-1]))
                    print('{0}. {1}'.format(1, baralho[int(entrada)-2]))
                    print('{0}. {1}'.format(2, baralho[int(entrada)-4]))
        elif len(possibilidades) == 1:
            if possibilidades == [1]:
                baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-2)
            if possibilidades == [3]:
                baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-4)
            print('o estado atual do baralho é:')
        funcoes_paciencia.possui_movimentos_possiveis(baralho) == False
    for i in range(len(baralho)):
        carta = baralho[i]
        if funcoes_paciencia.extrai_naipe(carta) == '♠':
            carta = BLUE + carta + RESET
        elif funcoes_paciencia.extrai_naipe(carta) == '♥':
            carta = RED + carta + RESET
        elif funcoes_paciencia.extrai_naipe(carta) == '♦':
            carta = CYAN + carta + RESET
        else:
            carta = GREEN + carta + RESET
        print('{0}. {1}'.format(i+1, carta))
    if len(baralho) == 1:
        print('Parabéns você ganhou!')
        resposta = input('Você quer jogar novamente? (sim ou não) ')
    else:
        print('Que pena você perdeu. Tente outra vez!')
        resposta = input('Você quer jogar novamente? (sim ou não) ')