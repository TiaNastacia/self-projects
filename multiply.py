def calc():
    result = multiply()
    return result

def multiply():
    var = input('Digite um numero: ')
    var2 = input('Digite outro numero: ')
    if var.isnumeric() and var2.isnumeric():
        var = int(var)
        var2 = int(var2)
        return var * var2
    return 'Digite apenas numeros inteiros!'

print(calc())
