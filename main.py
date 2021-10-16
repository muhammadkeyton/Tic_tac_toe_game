from os import system, name
import time
from game_brain import GameBrain

game_logo = '''
 
 
 _________   ___   ________          _________   ________   ________          _________   ________   _______          
|\___   ___\|\  \ |\   ____\        |\___   ___\|\   __  \ |\   ____\        |\___   ___\|\   __  \ |\  ___ \         
\|___ \  \_|\ \  \\ \  \___|        \|___ \  \_|\ \  \|\  \\ \  \___|        \|___ \  \_|\ \  \|\  \\ \   __/|        
     \ \  \  \ \  \\ \  \                \ \  \  \ \   __  \\ \  \                \ \  \  \ \  \\\  \\ \  \_|/__      
      \ \  \  \ \  \\ \  \____            \ \  \  \ \  \ \  \\ \  \____            \ \  \  \ \  \\\  \\ \  \_|\ \     
       \ \__\  \ \__\\ \_______\           \ \__\  \ \__\ \__\\ \_______\           \ \__\  \ \_______\\ \_______\    
        \|__|   \|__| \|_______|            \|__|   \|__|\|__| \|_______|            \|__|   \|_______| \|_______|   
        
'''


game_field_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(game_logo)
print("WELCOME TO THE TIC TAC TOE GAME.")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def human_players(player_a,player_b,game_length):
    while game_length > 0:

        game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                     f"--|---|--\n" \
                     f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                     f"--|---|--\n" \
                     f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
        #player 1
        print(f"{player_a}'s turn:")
        print(game_field)
        move1 = input(f"{player_a},enter position number: ")

        try:
            move1 = int(move1)
        except ValueError:
            print("")
            print("please enter whole numbers only and don't leave blank spaces.(1) not (1.2)")
            continue
        else:
            print("")
            if gamebrain.if_datatype_same(chosen_position=move1):
                game_field_positions[move1] = players_symbols[player_a]
                if game_length == 1:
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \

                    print(game_field)
                    print("draw")
                    quit()
                if gamebrain.player_win_check(player_dictionary=players_symbols,player_name=player_a):
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
         \

                    print(f"{player_a} won")
                    print(game_field)
                    break
                else:
                    game_length -= 1
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \

            else:
                clear()
                print(game_field)
                print("position already occupied or position doesn't exist")
                continue

        if game_length == 0:
            print(game_field)
            break

        clear()
        # player 2
        equal = False
        print(f"{player_b}'s turn:")
        print(game_field)
        while not equal:
            print("")
            move2 = input(f"{player_b},enter position number: ")
            try:
                move2 = int(move2)
            except ValueError:
                print("")
                print("please enter numbers only and don't leave blank spaces.(1) not (1.2)")
                continue
            else:
                if gamebrain.if_datatype_same(chosen_position=move2):
                    game_field_positions[move2] = players_symbols[player_b]
                    if gamebrain.player_win_check(player_dictionary=players_symbols, player_name=player_b):
                        game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                     f"--|---|--\n" \
                                     f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                     f"--|---|--\n" \
                                     f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \

                        print(f"{player_b} won")
                        print(game_field)
                        quit()

                    else:
                        game_length -= 1
                        equal = True



                else:
                    clear()
                    print(f"{player_b}'s turn:")
                    print(game_field)
                    print("position already occupied or position doesn't exist")
                    continue
        clear()

gamebrain = GameBrain(game_field_positions)
game_length = 9
game_type = input("please type 'P' to play with a human or type 'I' to play with AI: ").lower()

if game_type == "p":
    player_a = input("what is the first player's name? ")
    player_b = input("what is the second player's name? ")

    players_symbols = {
        player_a: "X",
        player_b: "O"
    }
    print(f"{player_a},you are 'x', while your opponent {player_b} is 'o'.")
    human_players(player_a,player_b,game_length)
elif game_type == "i":
    player_a = input("what is your name? ")
    player_b = "Artificial intelligence"
    players_symbols = {
        player_a: "X",
        player_b: "O"
    }
    print(f"{player_a},you are 'x', while your opponent {player_b} is 'o'.")
    while game_length > 0:

        game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                     f"--|---|--\n" \
                     f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                     f"--|---|--\n" \
                     f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
        #human player
        print(f"{player_a}'s turn:")
        print(game_field)
        move1 = input(f"{player_a},enter position number: ")

        try:
            move1 = int(move1)
        except ValueError:
            print("")
            print("please enter whole numbers only and don't leave blank spaces.(1) not (1.2)")
            continue
        else:
            print("")
            if gamebrain.if_datatype_same(chosen_position=move1):
                game_field_positions[move1] = players_symbols[player_a]
                if game_length == 1:
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \

                    print(game_field)
                    print("draw")
                    quit()
                if gamebrain.player_win_check(player_dictionary=players_symbols,player_name=player_a):
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
         \

                    print(f"{player_a} won")
                    print(game_field)
                    break
                else:
                    game_length -= 1
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \

            else:
                clear()
                print(game_field)
                print("position already occupied or position doesn't exist")
                continue

        if game_length == 0:
            print(game_field)
            break

        clear()

        #AI player

        # player 2
        equal = False
        print(f"{player_b}'s turn:")
        print(game_field)
        time.sleep(3)
        while not equal:
            print("")
            ai_pos = gamebrain.Artificial_intelligence_selected_position(player_dictionary=players_symbols, player_name=player_a,ai_name=player_b)
            if gamebrain.check_ai_datatype(chosen_position=ai_pos):
                gamebrain.Artificial_intelligence_occupy_position(selected_position=ai_pos,player_dictionary=players_symbols,ai_name=player_b)
                if gamebrain.player_win_check(player_dictionary=players_symbols, player_name=player_b):
                    game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
                                 f"--|---|--\n" \
                                 f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
    \

                    print(f"{player_b} won")
                    print(game_field)
                    quit()

                else:
                    game_length -= 1
                    equal = True
            else:
                break

        clear()





else:
    print("please choose between 'P' and 'I' ONLY!")








