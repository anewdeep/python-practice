'''
win conditions: -
1. horizontally
2. vertically
3. diagonally
'''

game = [[1, 2, 1],
        [2, 0, 1],
        [1, 0, 1]]

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])
        
    if check.count(check[0]) == len(check) and check[0] != 0:
        print("winner!")

'''
def win(current_game):
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")

win(game)
'''