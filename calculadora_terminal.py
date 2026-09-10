print('Bem-vindo a Calculadora pelo terminal.')

num1 = int(input('Digite um número? '))
num2 = int(input('Digite outro número? '))
operadores = input('Qual será o operador? ')
resultado = ''

if operadores == '+':
    resultado = num1 + num2
    print(f'A soma do {num1} e o {num2} é o {resultado}')
if operadores == '-':
    resultado = num1 - num2
    print(f'A subtração do {num1} e o {num2} é o {resultado}')
if operadores == '*':
    resultado = num1 * num2
    print(f'A multiplicação do {num1} e o {num2} é o {resultado}')
if operadores == '/':
    resultado = num1 / num2
    print(f'A divisão do {num1} e o {num2} é o {resultado}')
