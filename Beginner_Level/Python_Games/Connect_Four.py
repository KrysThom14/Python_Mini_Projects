# To-Do List:
# Display board
# Play a turn
# Make sure that turn was valid
# Check rows/columns/diagonals for a win
# Check for tie
# Switch between players


# Board = a single list with dashes as blank spaces
board = ["-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-"]


# Multiple print statements will make the board look the way we want it
def display_board():
    print(' 1  ', '  2  ', '  3  ', '  4  ', '  5  ', '  6  ', '  7')
    print('', board[0], ' | ', board[1], ' | ', board[2], ' | ', board[3],
                    ' | ', board[4], ' | ', board[5], ' | ', board[6])
    print('', board[7], ' | ', board[8], ' | ', board[9], ' | ', board[10],
                    ' | ', board[11], ' | ', board[12], ' | ', board[13])
    print('', board[14], ' | ', board[15], ' | ', board[16], ' | ', board[17],
                     ' | ', board[18], ' | ', board[19], ' | ', board[20])
    print('', board[21], ' | ', board[22], ' | ', board[23], ' | ', board[24],
                     ' | ', board[25], ' | ', board[26], ' | ', board[27])
    print('', board[28], ' | ', board[29], ' | ', board[30], ' | ', board[31],
                     ' | ', board[32], ' | ', board[33], ' | ', board[34])
    print('', board[35], ' | ', board[36], ' | ', board[37], ' | ', board[38],
                     ' | ', board[39], ' | ', board[40], ' | ', board[41])

# These are the 3 global variables
winner = None
playing_game = True
# Player 1 will be 'X'
current_player = 'X'


# SOURCE CODE
def play_game():

    # Define global variables
    global winner
    global current_player
    global playing_game

    # Display inital board
    display_board()

    # This while loop will continue until the game ends
    while playing_game:

        handle_turn(current_player)

        check_if_win()

        check_if_tie()

        switch_player()


    # If the game has ended, print out the results
    if winner == 'X' or winner == 'O':
        print('Congatulations! ' + winner + ' won!')
    elif winner == None:
        print("It's a Tie!")


def handle_turn(current_player):

    # Initial prompt for player to begin
    position = input('Choose a column 1-7: ')

    # Make sure player "ONLY" chooses a #1-7
    while not position.isnumeric():
        print('This is not a valid entry. Please try again...')
        return handle_turn(current_player)
    while int(position) < 1 or int(position) > 7:
        print('This is not a valid entry. Please try again...')
        return handle_turn(current_player)

    # The following if/elif statements put player's piece
    # at the bottom most available spot
    if int(position) == 1:
        if board[35] == '-':
            board[35] = current_player
        elif board[28] == '-':
            board[28] = current_player
        elif board[21] == '-':
            board[21] = current_player
        elif board[14] == '-':
            board[14] = current_player
        elif board[7] == '-':
            board[7] = current_player
        elif board[0] == '-':
            board[0] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 2:
        if board[36] == '-':
            board[36] = current_player
        elif board[29] == '-':
            board[29] = current_player
        elif board[22] == '-':
            board[22] = current_player
        elif board[15] == '-':
            board[15] = current_player
        elif board[8] == '-':
            board[8] = current_player
        elif board[1] == '-':
            board[1] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 3:
        if board[37] == '-':
            board[37] = current_player
        elif board[30] == '-':
            board[30] = current_player
        elif board[23] == '-':
            board[23] = current_player
        elif board[16] == '-':
            board[16] = current_player
        elif board[9] == '-':
            board[9] = current_player
        elif board[2] == '-':
            board[2] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 4:
        if board[38] == '-':
            board[38] = current_player
        elif board[31] == '-':
            board[31] = current_player
        elif board[24] == '-':
            board[24] = current_player
        elif board[17] == '-':
            board[17] = current_player
        elif board[10] == '-':
            board[10] = current_player
        elif board[3] == '-':
            board[3] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 5:
        if board[39] == '-':
            board[39] = current_player
        elif board[32] == '-':
            board[32] = current_player
        elif board[25] == '-':
            board[25] = current_player
        elif board[18] == '-':
            board[18] = current_player
        elif board[11] == '-':
            board[11] = current_player
        elif board[4] == '-':
            board[4] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 6:
        if board[40] == '-':
            board[40] = current_player
        elif board[33] == '-':
            board[33] = current_player
        elif board[26] == '-':
            board[26] = current_player
        elif board[19] == '-':
            board[19] = current_player
        elif board[12] == '-':
            board[12] = current_player
        elif board[5] == '-':
            board[5] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    if int(position) == 7:
        if board[41] == '-':
            board[41] = current_player
        elif board[34] == '-':
            board[34] = current_player
        elif board[27] == '-':
            board[27] = current_player
        elif board[20] == '-':
            board[20] = current_player
        elif board[13] == '-':
            board[13] = current_player
        elif board[6] == '-':
            board[6] = current_player
        else:
            print("""Sorry. No available spaces in this column.
                    Please try again...""")
            return handle_turn(current_player)

    # Diplay board again, but with updated player pieces
    display_board()


def check_if_win():
    global winner
    global playing_game

    # Check each row for a possible win
    def check_rows():
        row_1_1 = board[0] == board[1] == board[2] == board[3]
        row_1_2 = board[1] == board[2] == board[3] == board[4]
        row_1_3 = board[2] == board[3] == board[4] == board[5]
        row_1_4 = board[3] == board[4] == board[5] == board[6]

        if row_1_1 == True and board[0] != '-':
            return board[0]
        elif row_1_2 == True and board[1] != '-':
            return board[1]
        elif row_1_3 == True and board[2] != '-':
            return board[2]
        elif row_1_4 == True and board[3] != '-':
            return board[3]

        row_2_1 = board[7] == board[8] == board[9] == board[10]
        row_2_2 = board[8] == board[9] == board[10] == board[11]
        row_2_3 = board[9] == board[10] == board[11] == board[12]
        row_2_4 = board[10] == board[11] == board[12] == board[13]

        if row_2_1 == True and board[7] != '-':
            return board[7]
        elif row_2_2 == True and board[8] != '-':
            return board[8]
        elif row_2_3 == True and board[9] != '-':
            return board[9]
        elif row_2_4 == True and board[10] != '-':
            return board[10]

        row_3_1 = board[14] == board[15] == board[16] == board[17]
        row_3_2 = board[15] == board[16] == board[17] == board[18]
        row_3_3 = board[16] == board[17] == board[18] == board[19]
        row_3_4 = board[17] == board[18] == board[19] == board[20]

        if row_3_1 == True and board[14] != '-':
            return board[14]
        elif row_3_2 == True and board[15] != '-':
            return board[15]
        elif row_3_3 == True and board[16] != '-':
            return board[16]
        elif row_3_4 == True and board[17] != '-':
            return board[17]

        row_4_1 = board[21] == board[22] == board[23] == board[24]
        row_4_2 = board[22] == board[23] == board[24] == board[25]
        row_4_3 = board[23] == board[24] == board[25] == board[26]
        row_4_4 = board[24] == board[25] == board[26] == board[27]

        if row_4_1 == True and board[21] != '-':
            return board[21]
        elif row_4_2 == True and board[22] != '-':
            return board[22]
        elif row_4_3 == True and board[23] != '-':
            return board[23]
        elif row_4_4 == True and board[24] != '-':
            return board[24]

        row_5_1 = board[28] == board[29] == board[30] == board[31]
        row_5_2 = board[29] == board[30] == board[31] == board[32]
        row_5_3 = board[30] == board[31] == board[32] == board[33]
        row_5_4 = board[31] == board[32] == board[33] == board[34]

        if row_5_1 == True and board[28] != '-':
            return board[28]
        elif row_5_2 == True and board[29] != '-':
            return board[29]
        elif row_5_3 == True and board[30] != '-':
            return board[30]
        elif row_5_4 == True and board[31] != '-':
            return board[31]

        row_6_1 = board[35] == board[36] == board[37] == board[38]
        row_6_2 = board[36] == board[37] == board[38] == board[39]
        row_6_3 = board[37] == board[38] == board[39] == board[40]
        row_6_4 = board[38] == board[39] == board[40] == board[41]

        if row_6_1 == True and board[35] != '-':
            return board[35]
        elif row_6_2 == True and board[36] != '-':
            return board[36]
        elif row_6_3 == True and board[37] != '-':
            return board[37]
        elif row_6_4 == True and board[38] != '-':
            return board[38]

    # Check each column for a possible win
    def check_columns():
        column_1_1 = board[0] == board[7] == board[14] == board[21]
        column_1_2 = board[7] == board[14] == board[21] == board[28]
        column_1_3 = board[14] == board[21] == board[28] == board[35]

        if column_1_1 == True and board[0] != '-':
            return board[0]
        elif column_1_2 == True and board[7] != '-':
            return board[7]
        elif column_1_3 == True and board[14] != '-':
            return board[14]

        column_2_1 = board[1] == board[8] == board[15] == board[22]
        column_2_2 = board[8] == board[15] == board[22] == board[29]
        column_2_3 = board[15] == board[22] == board[29] == board[36]

        if column_2_1 == True and board[1] != '-':
            return board[1]
        elif column_2_2 == True and board[8] != '-':
            return board[8]
        elif column_2_3 == True and board[15] != '-':
            return board[15]

        column_3_1 = board[2] == board[9] == board[16] == board[23]
        column_3_2 = board[9] == board[16] == board[23] == board[30]
        column_3_3 = board[16] == board[23] == board[30] == board[37]

        if column_3_1 == True and board[2] != '-':
            return board[2]
        elif column_3_2 == True and board[9] != '-':
            return board[9]
        elif column_3_3 == True and board[16] != '-':
            return board[16]

        column_4_1 = board[3] == board[10] == board[17] == board[24]
        column_4_2 = board[10] == board[17] == board[24] == board[31]
        column_4_3 = board[17] == board[24] == board[31] == board[38]

        if column_4_1 == True and board[3] != '-':
            return board[3]
        elif column_4_2 == True and board[10] != '-':
            return board[10]
        elif column_4_3 == True and board[17] != '-':
            return board[17]

        column_5_1 = board[4] == board[11] == board[18] == board[25]
        column_5_2 = board[11] == board[18] == board[25] == board[32]
        column_5_3 = board[18] == board[25] == board[32] == board[39]

        if column_5_1 == True and board[4] != '-':
            return board[4]
        elif column_5_2 == True and board[11] != '-':
            return board[11]
        elif column_5_3 == True and board[18] != '-':
            return board[18]

        column_6_1 = board[5] == board[12] == board[19] == board[26]
        column_6_2 = board[12] == board[19] == board[26] == board[33]
        column_6_3 = board[19] == board[26] == board[33] == board[40]

        if column_6_1 == True and board[5] != '-':
            return board[5]
        elif column_6_2 == True and board[12] != '-':
            return board[12]
        elif column_6_3 == True and board[19] != '-':
            return board[19]

        column_7_1 = board[6] == board[13] == board[20] == board[27]
        column_7_2 = board[13] == board[20] == board[27] == board[34]
        column_7_3 = board[20] == board[27] == board[34] == board[41]

        if column_7_1 == True and board[6] != '-':
            return board[6]
        elif column_7_2 == True and board[13] != '-':
            return board[13]
        elif column_7_3 == True and board[20] != '-':
            return board[20]

    # Check each diagonal for a possible win
    def check_diagonals():
        diagonal_1 = board[21] == board[15] == board[9] == board[3]
        diagonal_2 = board[28] == board[22] == board[16] == board[10]
        diagonal_3 = board[22] == board[16] == board[10] == board[4]
        diagonal_4 = board[35] == board[29] == board[23] == board[17]
        diagonal_5 = board[29] == board[23] == board[17] == board[11]
        diagonal_6 = board[23] == board[17] == board[11] == board[5]
        diagonal_7 = board[36] == board[30] == board[24] == board[18]
        diagonal_8 = board[30] == board[24] == board[18] == board[12]
        diagonal_9 = board[24] == board[18] == board[12] == board[6]
        diagonal_10 = board[37] == board[31] == board[25] == board[19]
        diagonal_11 = board[31] == board[25] == board[19] == board[13]
        diagonal_12 = board[38] == board[32] == board[26] == board[20]
        diagonal_13 = board[14] == board[22] == board[30] == board[38]
        diagonal_14 = board[7] == board[15] == board[23] == board[31]
        diagonal_15 = board[3] == board[11] == board[19] == board[27]
        diagonal_16 = board[10] == board[18] == board[26] == board[34]
        diagonal_17 = board[15] == board[23] == board[31] == board[39]
        diagonal_18 = board[2] == board[10] == board[18] == board[26]
        diagonal_19 = board[0] == board[8] == board[16] == board[24]
        diagonal_20 = board[1] == board[9] == board[17] == board[25]
        diagonal_21 = board[8] == board[16] == board[24] == board[32]
        diagonal_22 = board[9] == board[17] == board[25] == board[33]
        diagonal_23 = board[16] == board[24] == board[32] == board[40]
        diagonal_24 = board[17] == board[25] == board[33] == board[41]

        if diagonal_1 == True and board[21] != '-':
            return board[21]
        elif diagonal_2 == True and board[28] != '-':
            return board[28]
        elif diagonal_3 == True and board[22] != '-':
            return board[22]
        elif diagonal_4 == True and board[35] != '-':
            return board[35]
        elif diagonal_5 == True and board[29] != '-':
            return board[29]
        elif diagonal_6 == True and board[23] != '-':
            return board[23]
        elif diagonal_7 == True and board[36] != '-':
            return board[36]
        elif diagonal_8 == True and board[30] != '-':
            return board[30]
        elif diagonal_9 == True and board[24] != '-':
            return board[24]
        elif diagonal_10 == True and board[37] != '-':
            return board[37]
        elif diagonal_11 == True and board[31] != '-':
            return board[31]
        elif diagonal_12 == True and board[38] != '-':
            return board[38]
        elif diagonal_13 == True and board[14] != '-':
            return board[14]
        elif diagonal_14 == True and board[7] != '-':
            return board[7]
        elif diagonal_15 == True and board[3] != '-':
            return board[3]
        elif diagonal_16 == True and board[10] != '-':
            return board[10]
        elif diagonal_17 == True and board[15] != '-':
            return board[15]
        elif diagonal_18 == True and board[2] != '-':
            return board[2]
        elif diagonal_19 == True and board[0] != '-':
            return board[0]
        elif diagonal_20 == True and board[1] != '-':
            return board[1]
        elif diagonal_21 == True and board[8] != '-':
            return board[8]
        elif diagonal_22 == True and board[9] != '-':
            return board[9]
        elif diagonal_23 == True and board[16] != '-':
            return board[16]
        elif diagonal_24 == True and board[17] != '-':
            return board[17]

    # Call previous functions to see if they return anything
    check_rows()
    check_columns()
    check_diagonals()

    # If so... assign the result of the function to a variable
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()

    # Award that player the win!
    if row_win:
        playing_game = False
        winner = row_win
    elif column_win:
        playing_game = False
        winner = column_win
    elif diagonal_win:
        playing_game = False
        winner = diagonal_win
    else:
        winner = None


# If check_if_win function fails to return anything...
def check_if_tie():

    global playing_game

    if '-' not in board:
        playing_game = False


# If there is neither a win nor a tie from the previous move...
def switch_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'
        print("Player O's turn...")
    elif current_player == 'O':
        current_player = 'X'
        print("Player X's turn...")



# Call function (Source Code) that starts the game
play_game()
