class TicTacToe: 
    def __init__(self):
        self.board = [' ' for _ in range(9)] #Lista simpes de para representa um 3x3
        self.current_winner = None #Tracking do vencedor

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('|'+'|'.join(row)+'|')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i range(j*3, (j+1*)3))] for j in range(3)]
        for row in number_board: 
            print('|'+'|'.join(row)+'|')
    
    def avaiable_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,x) in enumerate(self.board):
        #    #['x', 'x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #    if spot == '':
        #        moves.append(i)
        #return moves

    def empty_squares(self): 
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #se é um movimento valido altera de Quadrado para Letra
        #E retorna true, se nao false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter)
                self.current_winner = letter
            return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game: 
        game.print_board_nums()
    
    letter = 'X' #Primeira Letra
    #as interações do jogo são apenas nos quadrados vazios
    #não nos preocupamos aqui com se ja temos um vencedor pois o retorno 
    while game.empty_squares():
        #pega o movimento do jogador
        if letter == 'O':
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)
        
        #define a função de movimetação
        if game.make_move(square,   letter):
            if print_game: 
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('') #inserindo uma linha em Branco

            if game.current_winner: 
                if print_game:
                    print(letter + ' wins! :)')

            #depois de feito o movimento, nos precismao alterar a Letra
            letter = 'O' if letter == 'X' else 'X' #altera Jogador

