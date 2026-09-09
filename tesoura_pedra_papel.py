import random

OPCOES = ('pedra', 'papel', 'tesoura')
VENCE_DE = {'pedra': 'tesoura', 'papel': 'pedra', 'tesoura': 'papel'}


def ler_jogada():
    while True:
        jogada = input('Pedra, papel ou tesoura? ').strip().lower()
        if jogada in OPCOES:
            return jogada
        print('Item inválido. Escolha pedra, papel ou tesoura.')


def jogar_partida():
    jogador = ler_jogada()
    computador = random.choice(OPCOES)
    print(f'Computador escolheu {computador}.')

    if jogador == computador:
        print('Empate!')
    elif VENCE_DE[jogador] == computador:
        print('Você ganhou!')
    else:
        print('Computador venceu.')


def inicio():
    print('Bem-vindo ao Pedra, Papel e Tesoura!')
    while True:
        jogar = input('Jogar? [S/N]: ').strip().upper()
        if jogar == 'S':
            jogar_partida()
        elif jogar == 'N':
            print('Obrigado por jogar!')
            return
        else:
            print('Resposta inválida. Digite S ou N.')


if __name__ == '__main__':
    inicio()