import random

print('Bem vindo ao Pedra, Papel e Tesoura:')

jogar = input('Deseja jogar [S/N]: ').strip().upper()

opcoes = ('pedra','papel','tesoura')

while True:
    if jogar == 'S':
        escolha = input('Pedra, Papel ou Tesoura: ').strip().lower()
        computador = random.choice(opcoes)
        print(f'O Computador escolheu: {computador}')
        if escolha == computador:
            print('Empate!!')
        elif (escolha == 'pedra') or (escolha == 'tesoura') or (escolha == 'papel') != computador:
            print('Você Ganhou')
            
        else:
            print(f'O computador ganhou \n Sua escolha: {escolha} n Computador escolheu: {computador}')
            
    elif jogar != 'S':
        break
    sair = input('Deseja sair? [S/N] ').strip().upper()
    if sair == 'S':
        break
    else:
        continue
