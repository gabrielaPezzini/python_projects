from time import sleep

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

usuario = 0
maior = n1

while usuario != 5:
    print('-=-' * 20)
    print('OPERAÇÕES')
    print('-=-' * 20)
    print('[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Maior \n'
          '[ 4 ] Novos números \n'
          '[ 5 ] Sair do programa')
    print('---' * 20)
    usuario = int(input('Qual operação gostaria de executar? '))
    print('Executando...')
    sleep(1)

    if usuario == 1:
        print(f'{n1} + {n2} = {n1 + n2}')

    elif usuario == 2:
        print(f'{n1} x {n2} = {n1 * n2}')

    elif usuario == 3:
        if n2 > maior:
            maior = n2
        print(f'O maior valor é {maior}')

    elif usuario == 4:
        print('Informe os novos valores... ')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))

    elif usuario == 5:
        print('Finalizando...')
        sleep(1)

    else:
        print('Opção inválida! Tente novamente.')
    sleep(1)

print('Fim do programa! VOLTE SEMPRE!')

