class tictactoe():
    def board_setup(self, board):
        print(board[0] + '|' + board[1] + '|' + board[2])
        print('-----')
        print(board[3] + '|' + board[4] + '|' + board[5])
        print('-----')
        print(board[6] + '|' + board[7] + '|' + board[8])
    
    def print_board(self, board):
        print(board[0] + '|' + board[1] + '|' + board[2])
        print('-----')
        print(board[3] + '|' + board[4] + '|' + board[5])
        print('-----')
        print(board[6] + '|' + board[7] + '|' + board[8])

    def win_condition(self, board):
        if board[0] == board[4] and board[4] == board[8] and (board[0] == 'X' or board[0] == 'O'):
            if board[0] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[2] == board[4] and board[4] == board[6] and (board[2] == 'X' or board[2] == 'O'):
            if board[2] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[0] == board[3] and board[3] == board[6] and (board[0] == 'X' or board[0] == 'O'):
            if board[0] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[1] == board[4] and board[4] == board[7] and (board[1] == 'X' or board[1] == 'O'):
            if board[1] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[2] == board[5] and board[5] == board[8] and (board[2] == 'X' or board[2] == 'O'):
            if board[2] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[0] == board[1] and board[1] == board[2] and (board[0] == 'X' or board[0] == 'O'):
            if board[0] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[3] == board[4] and board[4] == board[5] and (board[3] == 'X' or board[3] == 'O'):
            if board[3] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        if board[6] == board[7] and board[7] == board[8] and (board[6] == 'X' or board[6] == 'O'):
            if board[6] == 'X':
                print('player 1 wins')
                return True
            else:
                print('player 2 wins')
                return True
        return False
    
    def is_free(self,board,pos):
        if board[pos] == ' ':
            return True
        return False
    
    def player_move(self,board,pos,who_goes):
        while self.is_free(board,pos) != True:
            new_pos = input('position is already taken, please choose a new position: ')
            if self.is_free(board,new_pos):
                if who_goes == 0:
                    board[new_pos-1] = 'X'
                    break
                else:
                    board[new_pos-1] = 'O'
                    break

        if who_goes == 0:
            board[pos] = 'X'
        else:
            board[pos] = 'O'

        

    def start_game(self, board):
        who_goes = 0
        self.board_setup(board)
        while self.win_condition(board) != True:
            p1_move = input('Which position would you like to take p1: ')
            pos1 = p1_move - 1
            self.player_move(board,pos1,who_goes)
            self.print_board(board)
            self.win_condition(board)
            who_goes += 1

            p2_move = input('Which position would you like to take p2: ')
            pos2 = p2_move - 1
            self.player_move(board,pos2,who_goes)
            self.print_board(board)
            self.win_condition(board)
            who_goes = who_goes - 1



if __name__ == "__main__":
    test = tictactoe()
    board = [' ',' ',' ',
            ' ',' ',' ',
            ' ',' ',' ']
    test.start_game(board)