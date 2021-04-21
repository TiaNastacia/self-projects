from random import randint as ri

print()
print('Esse programa irá rolar dados de 4, 6, 8, 12 e 20 lados, uma vez cada. Para finalizar, basta digitar "n"!!!!!')
print()

user = input('Deseja rolar o dado[s/n]? ')

while True:
   
  if user == 'n':
    print('Finalizado.')
    break

  if user == 's':
    d4 = ri(1, 4)
    d6 = ri(1, 6)
    d8 = ri(1, 8)
    d12 = ri(1, 12)
    d20 = ri(1, 20)

    print(f'd4 = {d4}, d6 = {d6}, d8 = {d8}, d12 = {d12}, d20 = {d20}')
  
  user = input('Deseja continuar[s/n]? ')

  if user != 'n' and user != 's':
    print('Digite somente s/n!!!')
    continue