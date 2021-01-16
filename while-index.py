frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova = ' '
alterar = input('Qual letra deseja alterar? ')

while contador < tamanho:
    letra = frase[contador]
    if letra == alterar:
    	    nova += alterar.upper()
    else:
        	nova += letra
    contador += 1

print(nova)