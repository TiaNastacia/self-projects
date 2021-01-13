name = input('insira seu nome: ')
idade = (input('insira sua idade: '))
altura = (input('insira sua altura: '))
peso = (input('insira seu peso: '))

#verifica e formata os valores de idade, peso e altura.
if idade.isdigit() and altura.isdigit() and peso.isdigit():
    age = int(idade)
    alt = float(altura)
    ps = float(peso)
    imc = ps / alt ** 2
    if imc < 18.5:
        print(f'{name}, seu imc é {imc:.2f} e você está abaixo do peso.')
    elif imc >= 25:
        print(f'{name}, seu imc é {imc:.2f} e você está acima do peso.')
    elif imc >= 30:
        print(f'{name}, seu imc é {imc:.2f} e você está em obesidade grau 1. Cuide de sua saúde.')
    elif imc >= 35:
        print(f'{name}, seu imc é {imc:.2f} e você está em obesidade grau 2. Cuide de sua saúde.')
    elif imc >= 40:
        print(f'{name}, seu imc é {imc:.2f} e você está em obesidade mórbida. Procure um especialista URGENTE.')
    else:
        print(f'{name}, seu imc é {imc:.2f} e você está no peso ideal. Mantenha os bons hábitos.')
else:
    print('Dados inválidos foram digitados!')
