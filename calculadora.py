# Escreva um programa em Python que simule uma calculadora simples, contendo as quatro operações basicas( +, - , *, / - Depois acrescente uma orepação nova). 

# - O programa deve ter:
# - menu de operações 
# - realizar o calculos escolhido (dois numero)
# - apresentar resultado

print('Ola Bem-vindo a calculadora basica de python')
print('--------------------------------------------')

print('Escreva Dois Numero e Depois escolha sua forma de Operação: +, *, - e / ou X˟')

num1 = float(input('Escreva seu primeiro numero: '))
num2 = float(input('Escreva seu segundo numero: '))
operador = input('Escreva a Operação: ')

match operador:
    case '+':
        resultado = num1+num2
        print(f'Resultado: {resultado:.1f}')
    case '-':
        resultado = num1-num2
        print(f'Resultado: {resultado:.1f}')
    case '*':
        resultado = num1*num2
        print(f'Resultado: {resultado:.1f}')
    case '/':
        resultado = num1/num2
        print(f'Resultado: {resultado:.1f}')
    case 'x˟':
        resultado = num1 ** num1
        print(f'Resultado: {resultado:.1f}')
    case _: 
        print('Operação não Encontrada!')

    
