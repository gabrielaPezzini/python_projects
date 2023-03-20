from random import randint

print('=' * 30)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=' * 30)

computador = randint(0, 10)
vitorias = 0

while True:
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    opcao = ' '

    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    print('-' * 30)

    if opcao == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break

    elif opcao == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')
    print('-' * 30)
    
print(f'GAME OVER! Você venceu {vitorias} vezes.')


