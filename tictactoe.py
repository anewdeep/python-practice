# simple tic tac toe game

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(player = 0, row = 0, column = 0):
    print("   0  1  2")
    game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(player=1, row=2, column=1)