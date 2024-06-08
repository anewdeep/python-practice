'''
win conditions: -
1. horizontally
2. vertically
3. diagonally
'''

game = [[1, 0, 2],
        [1, 2, 0],
        [1, 2, 1]]

def win(current_game):
    # Horizontal
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")

    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/)!")

    diags = []
    for index in range(len(game)):
        diags.append(game[index][index])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\)!")

    # Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")

win(game)