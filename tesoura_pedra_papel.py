import random

# Lista imutável de jogadas aceitas pelo programa.
OPCOES = ('pedra', 'papel', 'tesoura')
# Cada chave vence a jogada indicada pelo seu valor.
# Exemplo: pedra vence tesoura.
VENCE_DE = {'pedra': 'tesoura', 'papel': 'pedra', 'tesoura': 'papel'}


def ler_jogada():
    # Repete a pergunta até a pessoa informar uma opção válida.
    while True:
        # strip() remove espaços extras e lower() aceita maiúsculas/minúsculas.
        jogada = input('Pedra, papel ou tesoura? ').strip().lower()

        # Se a resposta estiver nas opções permitidas, ela é devolvida.
        if jogada in OPCOES:
            return jogada

        # Se não for válida, o laço recomeça e pergunta novamente.
        print('Item inválido. Escolha pedra, papel ou tesoura.')


def jogar_partida():
    # Obtém a escolha validada da pessoa.
    jogador = ler_jogada()
    # Sorteia uma das opções para o computador.
    computador = random.choice(OPCOES)
    print(f'Computador escolheu {computador}.')

    # Escolhas iguais resultam em empate.
    if jogador == computador:
        print('Empate!')
    # Consulta a regra: a jogada do usuário vence a do computador?
    elif VENCE_DE[jogador] == computador:
        print('Você ganhou!')
    # Não sendo empate nem vitória, a única possibilidade é derrota.
    else:
        print('Computador venceu.')


def inicio():
    # Esta mensagem aparece uma vez, antes do ciclo principal.
    print('Bem-vindo ao Pedra, Papel e Tesoura!')

    # Mantém o jogo em execução até a pessoa responder N.
    while True:
        # upper() permite que s e S tenham o mesmo significado.
        jogar = input('Jogar? [S/N]: ').strip().upper()

        if jogar == 'S':
            # Executa uma partida e volta a perguntar se deseja jogar de novo.
            jogar_partida()
        elif jogar == 'N':
            print('Obrigado por jogar!')
            # Encerra a função e, como ela é a principal, encerra o programa.
            return
        else:
            print('Resposta inválida. Digite S ou N.')


# Só inicia o jogo quando este arquivo é executado diretamente.
# Ao importá-lo em outro arquivo (por exemplo, para testes), inicio() não roda.
if __name__ == '__main__':
    inicio()
