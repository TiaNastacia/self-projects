from random import randint as ri

print()
print('O programa ira gerar um número aleatório de 0 a 99. Você tem 10 chances de desvendar esse número!!!')
print()

secret = ri(0, 99)
chances = 10

while True:
  

  if chances == 0:
    print('Você não foi capaz de desvendar o número secreto!!!')
    break
  
  num = input('Digite um número entre 0 e 99: ')
  
  if num.isnumeric():
    num = int(num)

    if num > secret:
      print('O número secreto é menor que o número informado!')
    elif num < secret:
      print ('O número secreto é maior que o número informado!')
    else:
      print('Parabéns, você descobriu o número secreto!!!!')
      break

  else:
    print('Você gastou uma chance de bobeira. Por favor, digite apenas números!!')

  if num != secret:
    chances -= 1
    print(f'Você ainda tem {chances} chances!')