# By Aakash Rohila
game_input =['Null', ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ]
# Board of my Game
def game_board(game_input):
    print("_"+ game_input[7]+ "_" + "|" + "_"+ game_input[8]+"_" + "|" + "_" + game_input[9] + "_" )
    print("_"+ game_input[4]+ "_" + "|" + "_"+ game_input[5]+"_" + "|" + "_" + game_input[6] + "_")
    print(" "+ game_input[1]+ " " + "|" + " "+ game_input[2]+" " + "|" + " " + game_input[3] + " ")



def marker_choose():
    print("Enter X or O for Player_1")
    marker = input()
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')
    else:
        print("Error, your choice cannot be other than X or O")



def win(game_input,marker):
    # For Horizontal
    return ((game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[1] == game_input[2] == game_input[3] == marker) or
            # For Vertical
            (game_input[7] == game_input[4] == game_input[1] == marker) or
            (game_input[8] == game_input[5] == game_input[2] == marker) or
            (game_input[9] == game_input[6] == game_input[3] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            # For Diagonal
            (game_input[7] == game_input[5] == game_input[3] == marker) or
            (game_input[9] == game_input[5] == game_input[1] == marker))

#print(win(game_input,'X'))
# I don't want a player to overwrite so this function exist
def space_check(game_input, num):
    if game_input[num] != ' ':
        return False
    else:
        return True
# Main
print("Are you ready to play Tic-Tac-Toe....")
game_board(game_input)
player_1 , player_2 = marker_choose()
print(player_1 + ' is Player_1 Marker')
print(player_2 + ' is Player_2 Marker')

print("Player_1 will play first")

activeplayer = player_1
isplayer1theactiveplayer = True
for i in range(1,10):
    print("Enter from 1 - 9",end=' ')

    num = int(input("> "))

    while space_check(game_input, num) == True:
        game_input[num] = activeplayer
        game_board(game_input)

    if isplayer1theactiveplayer == True:
        activeplayer = player_2
    else:
        activeplayer = player_1


    if win(game_input,player_1) == True:
        print(" Player_1 is the champion")
        exit()
    elif win(game_input,player_2) == True:
        print(" Player_2 is the champion")
        exit()
