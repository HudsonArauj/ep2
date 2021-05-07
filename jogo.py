import funcoes_paciencia


print('Paiciencia acordeao')
print('o estado atual do baralho é:')
baralho = funcoes_paciencia.cria_baralho()

while funcoes_paciencia.possui_movimentos_possiveis(baralho) != False:    
    for i in range(len(baralho)):
        print('{0}. {1}'.format(i+1, baralho[i]))
    entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
    
    if int(entrada) >= 53 or int(entrada) <= 0:
        print('Entrada invalida')
    else:
            
        possibilidades = funcoes_paciencia.lista_movimentos_possiveis(baralho, int(entrada)-1)
        if len(possibilidades) == 0:
            print("A carta {} não pode ser movida".format(baralho[int(entrada)-1]))
            entrada = input('escolha um numero de 1 a {}: '.format(len(baralho)))
        elif len(possibilidades) == 2:
            print("Escolha sobra qual carta você que empilhar o {}".format(baralho[int(entrada)-1]))
            print('{0}. {1}'.format(1, baralho[int(entrada)-2]))
            print('{0}. {1}'.format(2, baralho[int(entrada)-4]))
            escolha2 = ''
            while escolha2 != '1' and escolha2 != '2':
                escolha2 = input('Digite o número de sua escolha (1 ou 2): ')
                if escolha2 == '1':
                    baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-2)
                elif escolha2 == '2':
                    baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-4)
                else:
                    print('Escolha inválida!')
        elif len(possibilidades) == 1:
            baralho = funcoes_paciencia.empilha(baralho, int(entrada)-1, int(entrada)-2)

    funcoes_paciencia.possui_movimentos_possiveis(baralho) == False