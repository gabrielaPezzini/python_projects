print('=' * 80)
print('{:^80}'.format('CÁLCULO DO IMC'))
print('=' * 80)

altura = float(input('Digite a sua altura: [Cm] '))
peso = float(input('Digite o seu peso: [Kg] '))

IMC = peso / (altura / 100) ** 2

print('-' * 80)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como MAGREZA.')
    print(f'ATENÇÃO! Você está abaixo do ideal. Equilibre sua alimentação')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como NORMAL.')
    print(f'PARABÉNS! Continue o excelente trabalho.')

elif IMC >= 25 and IMC < 29.5:
    print(f'Sei IMC é de {IMC:.2f}, e é classificada como SOBREPESO.')
    print(f'ATENÇÃO! Você está um pouco acima do ideal. Continue se esforçando.')

elif IMC >= 30 and IMC < 39.9:
    print(f'CUIDADO! Seu IMC é de {IMC:.2f}, e é classificado como OBESIDADE.')
    print(f'Equilibre sua alimentação e comece a treinar.')

else:
    print(f'CUIDADO! Seu IMC é de {IMC:.2f}, e é classificado como OBESIDADE GRAVE.')
    print(f'Equilibre sua alimentação e comece a treinar.')

print('-' * 80)
