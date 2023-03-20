print('=' * 40)
print('GERADOR DE PA')
print('=' * 40)

primeiro = int(input('Digite o primeiro termo de sua PA: '))
razão = int(input('Digite a razão de sua PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razão
        cont += 1

    print('PAUSA')
    print('-' * 40)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    
print(f'Prograssão finalizada com {total} termos mostrados.')