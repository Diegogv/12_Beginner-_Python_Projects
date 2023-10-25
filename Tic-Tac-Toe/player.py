import math
import random

class Player: 
    def __init__(self, letter):
        #letter pode r ser x ou o
        self.letter = letter

    # quando quiser que todos os player peguem o proximo movimento em um Game
    def get_move(self, game):
        pass    

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.avaible_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square: 
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            #aqui é checado se temos um valor correto para a tentativa de movimento
            #deve ser um inteiro e se não for deve apresentar uma mensagem de invalido
            # se nao não for uma posição valida no board tem que apresentar uma msg de movimento invalido
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = true #movimento valido
            except ValueError:
                print(f'Movimento não permitido tente Outra vez! :)')
        return val