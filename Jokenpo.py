from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('=' * 20)
print('Vamos jogar JOKENPÔ!')
print('=' * 20)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

print('-' * 20)
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-' * 20)

print('O computador jogou: {}'.format(itens[computador]))
print('O jogador jogou: {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
