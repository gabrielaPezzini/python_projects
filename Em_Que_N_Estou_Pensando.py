from random import randint
from time import sleep

computador = randint(0, 10)
palpites = 0
acertou = False

print('*.' * 30)
print('{:^60}'.format('VOCÊ GOSTA DE ADIVINHAR?'))
print('*.' * 30)

print('Sou seu computador e estou pensando em número entre 0 e 10. \n'
      'Tente adivinhar...')

while not acertou:
    print('---' * 30)
    jogador = int(input('Em que número pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez!')
        elif jogador > computador:
            print('Menos.. Tente mais uma vez!')

print(F'Acertou com {palpites} tentativas. PARABÉNS!')




