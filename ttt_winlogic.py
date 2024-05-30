game = [[1, 1, 1],
        [0, 0, 0],
        [1, 0, 1]]

'''
win conditions: -
1. horizontally
2. vertically
3. diagonally
'''

def win(current_game):
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")

win(game)