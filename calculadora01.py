print('----- Calculadora em Python -----')

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y
    
def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        print('O Y não pode ser igual a zero, por favor selecione outro valor')
    else:
        return x / y

opc = int(input('Qual operação deseja executar? 1 soma, 2 subtração, 3 multiplicação ou 4 divisão?'))

if opc == 1:
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo número: '))
    print(soma(x, y))

if opc == 2:
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    print(subtracao(x, y))

if opc == 3:
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    print(multiplicacao(x, y))

if opc == 4:
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    print(divisao(x, y))

if opc > 4 or opc == 0:
    print('Opção inválida!')