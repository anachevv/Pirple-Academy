# | | | | | | |  0
# --------------- 1
# | | | | | | |  2
# --------------- 3
# | | | | | | |  4
# --------------- 5
# | | | | | | |  6
# --------------- 7
# | | | | | | |  8
# --------------- 9
# | | | | | | |  10
# --------------- 11
# | | | | | | |  12
# 0123456789101112

def drawField(field):
    for row in range(13):  # 0,1,2,3,4,5,6,7,8,9,10,11,12
        if row % 2 == 0:  # 0,2,4,6,8,10,12
            practicalRow = int(row / 2)
            for column in range(13):  # 0,1,2,3,4,5,6,7,8,9,10,11,12
                if column % 2 == 0:  # 0,2,4,6,8,10,12
                    practicalColumn = int(column / 2)
                    if column != 12:
                        print(end="")
                        tile = (field[practicalColumn][practicalRow])
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                        print(tile)
                else:
                    print("|", end="")
            else:
                print("-------------")


Player = 1
currentField = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "]]
drawField(currentField)
while (True):
    print("Players turn: ", Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter the column\n"))
    if Player == 1:
        # Make move for player 1
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        # Make move for player 2
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1


    def updateField(num, player):
        column = currentField[num]
        index = ""
        reversed_column = column[::-1]


    for row in reversed_column:
        if row == " ":
            index = reversed_column.index(row)
            reversed_column[index] = "X" if Player == 1 else "O"
            break
    if index == "":
        column = reversed_column[::-1]
    currentField[num] = column
    drawField(currentField)


    def FourInRow():
        winner = False
        for column in currentField:
            counter = 0
            length = len(column)
            for i in range(1, length):
                if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                    counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner
        return winner


    def FourInColumn(column_matrix):
        winner = False
        for column in column_matrix:
            counter = 0
            length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner
        return winner


    def FourInForwardDiagonal(column_matrix, player):
        for i in range(0, len(column_matrix)):
            for g in range(0, len(column_matrix[i])):
                try:
                    if column_matrix[i][g] == player and column_matrix[i + 1][g - 1] == player and column_matrix[i + 2][
                        g - 2] == player and column_matrix[i + 3][g - 3] == player:
                        return True
                except IndexError:
                    next
                    return False


    def FourInBackwardDiagonal(column_matrix, player):
        for i in range(0, len(column_matrix)):
            for g in range(0, len(column_matrix[i])):
                try:
                    if column_matrix[i][g] == player and column_matrix[i + 1][g + 1] == player and column_matrix[i + 2][
                        g + 2] == player and column_matrix[i + 3][g + 3] == player:
                        return True
                except IndexError:
                    next
                    return False


    def ValidMove(column_no):
        if column_no >= 1 and column_no <= 7:
            return True
        else:
            return False


    def createColumnMatrix():
        column_matrix = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " "]]
        for i in range(7):
            for g in range(len(currentField[i])):
                column_matrix[g][i] = currentField[i][g]
            return column_matrix


    def startConnect4():
        player = 1


    no_win = True
    winner = ""
    while (no_win):
        ask_column = ("Player" + str(Player) + "Turn, enter the column number:\n")
        column_no = input(ask_column)
        if column_no:
            column_no = int(column_no)
            if ValidMove(column_no) == False:
                print("This is a wrong move. Try again.\n")
            else:
                updated_flag = updateField(column_no - 1, Player)
                if updated_flag:
                    print("")
                    current_player = Player
                winner = FourInRow()
            if winner:
                no_win = False
            else:
                column_matrix = createColumnMatrix()
                winner = FourInColumn(column_matrix)
            if winner:
                no_win = False
            elif FourInBackwardDiagonal(column_matrix):
                winner = current_player
                no_win = False
            elif FourInForwardDiagonal(column_matrix):
                winner = current_player
                no_win = False
            else:
                print("This is a wrong move. Try again.\n")
        else:
            print("This is a wrong move. Try again.\n")
        if winner == "X":
            winner = "1"
        else:
            winner = "2"
            print("WINNER = PLAYER " + str(winner))
            print("GAME STARTING! GET READY!!\n")
            drawField(currentField)
            drawField()
