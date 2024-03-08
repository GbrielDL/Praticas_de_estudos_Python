from time import sleep
from funcoes.numeros import *
from funcoes.strings import *

#pegar os dados em forma de dicionario
dados = dict()
#quantidade de gols em forma de lista
gols = list()
#lista final
time = list()

while True:
    #limpa a lista de gols
    gols.clear()
    #cadastrar um jogador (nome, partidas e gols)
    print('\033[32m-=- CADASTRE UM JOGADOR -=-\033[m')
    try:
        nome = leiaStr('Nome do jogador: ')
    except:
        print('\033[31mError\033[m')
    else:
        if nome == '':
            print('\033[31mNão deixe o campo em branco\033[m')
            continue
        else:
            dados['Nome'] = nome

    part = leiaInt(f'Quantas partidas \033[33m\'{nome}\'\033[m jogou? ')
    dados['Partidas'] = part
    
    for gol in range(0, part):
        gols.append(leiaInt(f'-- Quantos gols na {gol+1}° partida? '))
    dados['Gols'] = gols[:]
    #adicionar todos os dados na lista final
    time.append(dados.copy())
    #continuar ou não com a repetição
    pro = ' '
    while pro not in 'SN':
        print(f'\033[36m{linha()}\033[m')
        pro = str(input('Próximo Jogador [S/N]? ')).strip().upper()[0]
        if pro not in 'SN':
            print('\033[33mDigite apenas Sim ou Não\033[m')
    if pro == 'N':
        break

print('\033[32m-=- LISTA DO TIME -=-\033[m')

print(f'{"Cod":<4}', end='')
for key in dados.keys():
    print(f'{key:<20}', end='')
#quebra de linha
print()
print(f'\033[36m{linha()}\033[m')
for p, jog in enumerate(time):
    print(f'{p:3}', end=' ')
    for value in jog.values():
        print(f'{str(value):<20}', end='')
    print()
print(f'\033[36m{linha()}\033[m')

while True:
    opcao = leiaInt('Levantamento de qual Jogador? \033[36m[999 pra parar]\033[m ')
    if opcao == 999:
        break
    elif opcao >= len(time):
        print(f'\033[33mO código \'{opcao}\' não pertence a nenhum jogador\033[m')
        continue
    else:
        print(f'\033[36m{linha()}\033[m')
        print(f'Levantamento do Jogador \033[33m\'{time[opcao]["Nome"]}\'\033[m')
        #tabela de gols nas partidas
        for p, gol in enumerate(time[opcao]["Gols"]):
            print(f'-- Na {p+1} partida, fez {gol} ', end='')
            if gol <= 1:
                print('gol')
            else:
                print('gols')
    print(f'\033[36m{linha()}\033[m')

print('\033[33m-=- PROGRAMA ENCERRADO -=-\033[m')