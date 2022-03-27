

game_board=[[" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "]]
game = True
count = 0
score1 = 0
score2 = 0
letter_1 = 0
p1_row = 0
p1_column = 0
letter_2 = 0
p2_row = 0
p2_column = 0
player_turn = True



def print_game_board():
    print("|", game_board[2][2], "|", game_board[2][3], "|", game_board[2][4], "|", game_board[2][5], "|")
    print("-" * 20)
    print("|", game_board[3][2], "|", game_board[3][3], "|", game_board[3][4], "|", game_board[3][5], "|")
    print("-" * 20)
    print("|", game_board[4][2], "|", game_board[4][3], "|", game_board[4][4], "|", game_board[4][5], "|")
    print("-" * 20)
    print("|", game_board[5][2], "|", game_board[5][3],"|", game_board[5][4], "|", game_board[5][5], "|")


print_game_board()

def checkplay():
    global count
    if count % 2 == 1:
        input1()
        count += 1
        checkhorizontal1()
        checkvertical1()
        checkdiagonal1()

    elif count % 2 == 0:
        input2()
        count += 1
        checkhorizontal2()
        checkvertical2()
        checkdiagonal2()
#take player input

def input1():
    global letter_1
    global p1_row
    global p1_column
    letter_1 = str(input("please enter your letter"))
    p1_row = int(input("please enter your row's number"))
    p1_column = int(input("please enter your column's number"))
    game_board[p1_row + 1][p1_column + 1] = letter_1

def checkhorizontal1():
    global letter_1
    global p1_row
    global p1_column
    global count
    global score1
    if letter_1 == 's':
        if game_board[p1_row + 1][p1_column + 1] == game_board[p1_row + 1][p1_column + 3] == "s" and game_board[p1_row + 1][p1_column + 2] == "o":
            count += 1
            score1 += 1

        elif game_board[p1_row + 1][p1_column + 1] == game_board[p1_row + 1][p1_column - 1] == "s" and game_board[p1_row + 1][p1_column] == "o":
            count += 1
            score1 += 1
        if letter_1 == 'o':
            if game_board[p1_row + 1][p1_column + 1] == 'o' and game_board[p1_row + 1][p1_column + 2] == game_board[p1_row + 1][p1_column] == "s":
                count += 1
                score1 += 1

def checkvertical1():
    global letter_1
    global p1_row
    global p1_column
    global count
    global score1
    if letter_1 == "s":
        if game_board[p1_row + 1][p1_column + 1] == game_board[p1_row - 1][p1_column + 1] == "s" and game_board[p1_row][p1_column + 1] == "o":
            count += 1
            score1 += 1

        elif game_board[p1_row + 1][p1_column + 1] == game_board[p1_row + 3][p1_column + 1] == "s" and game_board[p1_row + 2][p1_column + 1] == "o":
            count += 1
            score1 += 1
        if letter_1 == "o":
            if game_board[p1_row + 1][p1_column + 1] == 'o' and game_board[p1_row][p1_column + 1] == game_board[p1_row + 2][p1_column + 1] == 's':
                count += 1
                score1 += 1

def checkdiagonal1():
    global letter_1
    global p1_row
    global p1_column
    global count
    global score1

    if letter_1 == "s":
        if game_board[p1_row+1][p1_column +1] == game_board[p1_row-1][p1_column  -1] == "s" and game_board[p1_row][p1_column] == 'o':
            count += 1
            score1 += 1

        elif game_board[p1_row + 1][p1_column + 3] == game_board[p1_row - 1][p1_column + 5] == "s" and game_board[p1_row][p1_column + 4] == "o":
            count += 1
            score1 += 1

    if letter_1 == 'o':
        if game_board[p1_row + 1][p1_column + 1] == 'o' and game_board[p1_row + 2][p1_column ] == game_board[p1_row][p1_column+2] == 's':
            count += 1
            score1 += 1
        elif game_board[p1_row + 1][p1_column + 3] == 'o' and game_board[p1_row][p1_column + 4] == game_board[p1_row + 2][p1_column + 2] == 's':
            count += 1
            score1 += 1
def input2():
    global letter_2
    global p2_row
    global p2_column
    letter_2 = str(input("please enter your letter"))
    p2_row =int(input("please enter your row's number"))
    p2_column = int(input("please enter your column's number"))
    game_board[p2_row + 1][p2_column + 1] = letter_2



def checkhorizontal2():
    global letter_2
    global p2_row
    global p2_column
    global count
    global score2
    if letter_2 == "s":
         if game_board[p2_row + 1][p2_column + 1] == game_board[p2_row + 1][p2_column + 3] == "s" and game_board[p2_row + 1][  p2_column + 2] == "o":
            count += 1
            score2 += 1

         elif game_board[p2_row + 1][p2_column + 1] == game_board[p2_row + 1][p2_column - 1] == "s" and game_board[p2_row + 1][p2_column] == "o":
            count += 1
            score2 += 1
    if letter_1 == 'o':
        if game_board[p2_row+1][p2_column+1] =='o' and game_board[p2_row+1][p2_column+2] == game_board[p2_row+1][p2_column] == "s":
            count += 1
            score2 += 1

def checkvertical2():
    global letter_2
    global p2_row
    global p2_column
    global count
    global score2
    if letter_2 == "s":
        if game_board[p2_row + 1][p2_column + 1] == game_board[p2_row - 1][p2_column + 1] == "s" and game_board[p2_row][p2_column + 1] == "o":
            count +=1
            score2 += 1

        elif game_board[p2_row + 3][p2_column + 1] == game_board[p2_row + 2][p2_column + 1] == "s" and game_board[p2_row + 3][p2_column + 1] == "o":
            count +=1
            score2 += 1
    if letter_2 == "o":
         if game_board[p2_row][p2_column + 1] == 'o' and game_board[p2_row+2][p2_column + 1] ==  game_board[p2_row + 2][p2_column + 1] == 's':
            count += 1
            score2 += 1


def checkdiagonal2():
    global letter_2
    global p2_row
    global p2_column
    global count
    global score2
    if letter_2 == "s":
        if game_board[p2_row + 1][p2_column + 1] == game_board[p2_row -1][p2_column + -1] == "s" and game_board[p2_row ][p2_column] == "o":
            count +=1
            score2 += 1

        elif game_board[p2_row + 1][p2_column + 3] == game_board[p2_row -1][p2_column + 5] == "s" and game_board[p2_row ][p2_column + 4] == "o":
            count +=1
            score2 += 1
    if letter_2 =='o':
        if game_board[p2_row+1][p2_column+1] == 'o' and game_board[p2_row+2][p2_column] == game_board[p2_row][p2_column+2] == 's' :
            count+= 1
            score1 += 1
        elif game_board[p2_row+1][p2_column+3] == 'o' and game_board[p2_row][p2_column+4] == game_board[p2_row+2][p2_column+2] == 's' :
            count+= 1
            score2 += 1

#check the end of the game
def checktheendofgame():
    global game
    if " " not in game_board:
        game = False
        checkwinner()


#check for the winner
def checkwinner():
    global score1
    global score2
    if score1 > score2:
        print("the first player is the winner")
    elif score1 < score2:
        print("the second player is the winner")
    elif score1 == score2:
        print("the two player have the same score")

#print gameboard








while game:
    checkplay()
    print_game_board()
    checktheendofgame()
    checkplay()
    print_game_board()
    checktheendofgame()

while True:
    checkplay()
    print_game_board()
    checktheendofgame()
    checkplay()
    print_game_board()
    checktheendofgame()