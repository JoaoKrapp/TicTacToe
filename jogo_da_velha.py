position = [[" ", " ", " "], 
            [" ", " ", " "], 
            [" ", " ", " "]]

def print_tic_tac_toe(array : list):

    TIC_TAC_TOE = f"\n\
     {array[0][0]} | {array[0][1]} | {array[0][2]} \n\
    ------------\n\
     {array[1][0]} | {array[1][1]} | {array[1][2]} \n\
    ------------\n\
     {array[2][0]} | {array[2][1]} | {array[2][2]} \n\
         "

    return TIC_TAC_TOE

def verify_diagonals(array : list):
    if (array[2][0] == array[1][1]) and (array[1][1] == array[0][2]) and (array[1][1] != " "):
        return True
    elif (array[0][0] == array[1][1]) and (array[1][1] == array[2][2]) and (array[1][1] != " "):
        return True
    else:
        return False

def verify_horizontals(array : list):
    for i in array:
        if (i[0] == i[1]) and (i[1] == i[2]) and i[1] != " ":
            return True
    return False

def verify_verticals(array : list):
    if (array[0][0] == position[1][0]) and (position[1][0] == position[2][0]) and (array[1][0] != " "):
        return True
    elif (array[0][1] == position[1][1]) and (position[1][1] == position[2][1]) and (array[1][1] != " "):
        return True
    elif (array[0][2] == position[1][2]) and (position[1][2] == position[2][2]) and (array[1][2] != " "):
        return True
    else:
        return False

def won(array : list):
    if verify_verticals(array) or verify_horizontals(array) or verify_diagonals(array):
        return True
    else:
        return False

count = 0

if __name__ == "__main__":
    player = "O"

    
    
    while True:
    
        count = count + 1

        print(print_tic_tac_toe(position))
    
        if player == "O":
            player = "X"
        elif player == "X":
            player = "O"
    
        answer = str(input("Which place do you want to pick? "))
        
        if answer == "1":
            position[2][0] = player
        elif answer == "2":
            position[2][1] = player
        elif answer == "3":
            position[2][2] = player
        elif answer == "4":
            position[1][0] = player
        elif answer == "5":
            position[1][1] = player
        elif answer == "6":
            position[1][2] = player
        elif answer == "7":
            position[0][0] = player
        elif answer == "8":
            position[0][1] = player
        elif answer == "9":
            position[0][2] = player
        else:
            break
    
        if won(position):
            print("")
            print(f"   Player {player} won!")
            print(print_tic_tac_toe(position))
            break
        elif count >= 9:
            print("")
            print(f"      A Tie!")
            print(print_tic_tac_toe(position))
            break