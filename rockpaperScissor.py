import random

def play(): 
    useroption = input("'r' for Rock, 'p' for Paper and 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if useroption == computer: 
        return 'tie'
    
    #r > s, s > p, p > r
    if vencedor(useroption, computer):
        return "Você Venceu! :)'"

    return "Você Perdeu! :("

def vencedor(jogador, computer):
    
    if (jogador == 'r' and computer == 's') or (jogador == 's' and computer == 'p') or (jogador == 'p' and computer == 'r'): 
        return True

Jogar = ''
while Jogar == '':
    print(f'{play()}')
    Jogar = input("Desejar jogar novamente? Enter para Sim ou 'N' para Não e sair do jogo: ")