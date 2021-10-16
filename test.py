
#-------------------------------------------this is my code testing area and debugging area------------------------------


# game_field_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# players_symbols = {
#     "a": "X",
#     "b": "O"
# }
#
# game_field_positions[0] = players_symbols["a"]

# print(type(game_field_positions[0]))

#------------------------data type check test----------------------------------------------------------------------------
# def if_datatype_same(chosen_position):
#     if chosen_position in game_field_positions:
#         return True
#     else:
#         return False
#
# print(game_field_positions)
#
# if if_datatype_same(0):
#     print("yeye")
# else:
#     print("no no no")


#-----------------------player win test----------------------------------------------------------------------------------

# game_field_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# players_symbols = {
#     "a": "X",
#     "b": "O"
# }
#
# game_field_positions[0] = players_symbols["a"]
# game_field_positions[3] = players_symbols["a"]
# game_field_positions[6] = players_symbols["a"]
# def player_a_win_check():
#     if game_field_positions[0] == "X" and game_field_positions[1] == "X" and game_field_positions[2] == "X":
#         return True
#     elif game_field_positions[3] == "X" and game_field_positions[4] == "X" and game_field_positions[5] == "X":
#         return True
#     elif game_field_positions[6] == "X" and game_field_positions[7] == "X" and game_field_positions[8] == "X":
#         return True
#     elif game_field_positions[0] == "X" and game_field_positions[3] == "X" and game_field_positions[6] == "X":
#         return True
#     elif game_field_positions[1] == "X" and game_field_positions[4] == "X" and game_field_positions[7] == "X":
#         return True
#     elif game_field_positions[2] == "X" and game_field_positions[5] == "X" and game_field_positions[8] == "X":
#         return True
#
#     elif game_field_positions[0] == "X" and game_field_positions[4] == "X" and game_field_positions[8] == "X":
#         return True
#
#     elif game_field_positions[2] == "X" and game_field_positions[4] == "X" and game_field_positions[6] == "X":
#         return True
#     else:
#         return False
#
# player_a_win_check()
#

#-----------------------------------input test--------------------------------------------------------------------------

# age = input("age: ")
#
# try:
#     new_age = int(age)
#     print(new_age + 1)
# except ValueError:
#     print("enter whole numbers only and make sure not to leave blank spaces")


#---------------------------------human player backup code--------------------------------------------------------------
# while game_length > 0:
#
#         game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
#                      f"--|---|--\n" \
#                      f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
#                      f"--|---|--\n" \
#                      f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
#         #player 1
#         print(f"{player_a}'s turn:")
#         print(game_field)
#         move1 = input(f"{player_a},enter position number: ")
#
#         try:
#             move1 = int(move1)
#         except ValueError:
#             print("")
#             print("please enter whole numbers only and don't leave blank spaces.(1) not (1.2)")
#             continue
#         else:
#             print("")
#             if gamebrain.if_datatype_same(chosen_position=move1):
#                 game_field_positions[move1] = players_symbols[player_a]
#                 if game_length == 1:
#                     game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
#
#                     print(game_field)
#                     print("draw")
#                     quit()
#                 if gamebrain.player_win_check(player_dictionary=players_symbols,player_name=player_a):
#                     game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
#          \
#
#                     print(f"{player_a} won")
#                     print(game_field)
#                     break
#                 else:
#                     game_length -= 1
#                     game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
#                                  f"--|---|--\n" \
#                                  f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
#
#             else:
#                 clear()
#                 print(game_field)
#                 print("position already occupied or position doesn't exist")
#                 continue
#
#         if game_length == 0:
#             print(game_field)
#             break
#
#         clear()
#         # player 2
#         equal = False
#         print(f"{player_b}'s turn:")
#         print(game_field)
#         while not equal:
#             print("")
#             move2 = input(f"{player_b},enter position number: ")
#             try:
#                 move2 = int(move2)
#             except ValueError:
#                 print("")
#                 print("please enter numbers only and don't leave blank spaces.(1) not (1.2)")
#                 continue
#             else:
#                 if gamebrain.if_datatype_same(chosen_position=move2):
#                     game_field_positions[move2] = players_symbols[player_b]
#                     if gamebrain.player_win_check(player_dictionary=players_symbols, player_name=player_b):
#                         game_field = f"{game_field_positions[0]} | {game_field_positions[1]} | {game_field_positions[2]} \n" \
#                                      f"--|---|--\n" \
#                                      f"{game_field_positions[3]} | {game_field_positions[4]} | {game_field_positions[5]} \n" \
#                                      f"--|---|--\n" \
#                                      f"{game_field_positions[6]} | {game_field_positions[7]} | {game_field_positions[8]}" \
#
#                         print(f"{player_b} won")
#                         print(game_field)
#                         quit()
#
#                     else:
#                         game_length -= 1
#                         equal = True
#
#
#
#                 else:
#                     clear()
#                     print(f"{player_b}'s turn:")
#                     print(game_field)
#                     print("position already occupied or position doesn't exist")
#                     continue
#         clear()

#----------------------------------------artificial intelligence test---------------------------------------------------
#
# game_field_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# players_symbols = {
#     "player": "X",
#     "ai": "O"
# }
#
# game_field_positions[6] = players_symbols["ai"]
# game_field_positions[7] = players_symbols["player"]
# game_field_positions[8] = players_symbols["player"]
#
# def check_ai_datatype(chosen_position):
#     if type(chosen_position) == int:
#         return True
#     else:
#         return False
#
# def Artificial_intelligence_selected_position(player_dictionary, player_name,ai_name):
# #-------------------------------------verticals-----------------------------------------------------------------------------------
#     # verticals one
#     if game_field_positions[0] == player_dictionary[player_name] and game_field_positions[3] == player_dictionary[player_name]:
#         return game_field_positions[6]
#
#     if game_field_positions[3] == player_dictionary[player_name] and game_field_positions[6] == player_dictionary[player_name]:
#         return game_field_positions[0]
#
#     # verticals two
#     if game_field_positions[1] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[player_name]:
#         return game_field_positions[7]
#     if game_field_positions[4] == player_dictionary[player_name] and game_field_positions[7] == player_dictionary[player_name]:
#         return game_field_positions[1]
#
#     # verticals three
#     if game_field_positions[2] == player_dictionary[player_name] and game_field_positions[5] == player_dictionary[player_name]:
#         return game_field_positions[8]
#     if game_field_positions[5] == player_dictionary[player_name] and game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[2]
# #----------------------------------------------horizontals-------------------------------------------------------------------------------------
#     # horizontal one important
#     if game_field_positions[0] == player_dictionary[player_name] and game_field_positions[1] == player_dictionary[ai_name] and game_field_positions[2] == player_dictionary[player_name]:
#         return game_field_positions[3]
#     if game_field_positions[1] == player_dictionary[player_name] and game_field_positions[2] == player_dictionary[player_name] and game_field_positions[0] == player_dictionary[ai_name]:
#         return game_field_positions[3]
#     if game_field_positions[1] == player_dictionary[ai_name] and game_field_positions[2] == player_dictionary[player_name] and game_field_positions[0] == player_dictionary[player_name]:
#         return game_field_positions[3]
#
#     #horizontal one
#     if game_field_positions[0] == player_dictionary[player_name] and game_field_positions[1] == player_dictionary[player_name]:
#         return game_field_positions[2]
#     if game_field_positions[1] == player_dictionary[player_name] and game_field_positions[2] == player_dictionary[player_name]:
#         return game_field_positions[0]
#
#
#     #horizontal two important
#     if game_field_positions[3] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[ai_name] and game_field_positions[5] == player_dictionary[player_name]:
#         return game_field_positions[6]
#     if game_field_positions[3] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[player_name] and game_field_positions[5] == player_dictionary[ai_name]:
#         return game_field_positions[6]
#     if game_field_positions[3] == player_dictionary[ai_name] and game_field_positions[4] == player_dictionary[player_name] and game_field_positions[5] == player_dictionary[player_name]:
#         return game_field_positions[6]
#
#     #horizontal two
#     if game_field_positions[3] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[player_name]:
#         return game_field_positions[5]
#     if game_field_positions[4] == player_dictionary[player_name] and game_field_positions[5] == player_dictionary[player_name]:
#         return game_field_positions[3]
#
#
#     #horizontal 3 important
#     if game_field_positions[6] == player_dictionary[player_name] and game_field_positions[7] == player_dictionary[ai_name] and game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[0]
#     if game_field_positions[6] == player_dictionary[player_name] and game_field_positions[7] == player_dictionary[player_name] and game_field_positions[8] == player_dictionary[ai_name]:
#         return game_field_positions[0]
#     if game_field_positions[6] == player_dictionary[ai_name] and game_field_positions[7] == player_dictionary[player_name] and game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[0]
#
#     #horizontal three
#     if game_field_positions[6] == player_dictionary[player_name] and game_field_positions[7] == player_dictionary[player_name]:
#         return game_field_positions[8]
#     if game_field_positions[7] == player_dictionary[player_name] and game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[6]
# #----------------------------------------------diagnols----------------------------------------------------------------------------
#
#     #diagnol 1
#     if game_field_positions[0] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[player_name]:
#         return game_field_positions[8]
#     if game_field_positions[4] == player_dictionary[player_name] and game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[0]
#
#
#     #diagnol 2
#     if game_field_positions[2] == player_dictionary[player_name] and game_field_positions[4] == player_dictionary[player_name]:
#         return game_field_positions[6]
#     if game_field_positions[4] == player_dictionary[player_name] and game_field_positions[6] == player_dictionary[player_name]:
#         return game_field_positions[2]
#
#
#     #  X O X ,O X O, X O X  style
#     if game_field_positions[0] == player_dictionary[player_name]:
#         return game_field_positions[1]
#
#     elif game_field_positions[1] == player_dictionary[player_name]:
#         return game_field_positions[2]
#
#     elif game_field_positions[2] == player_dictionary[player_name]:
#         return game_field_positions[3]
#
#     elif game_field_positions[3] == player_dictionary[player_name]:
#         return game_field_positions[4]
#
#     elif game_field_positions[4] == player_dictionary[player_name]:
#         return game_field_positions[5]
#
#     elif game_field_positions[5] == player_dictionary[player_name]:
#         return game_field_positions[6]
#
#     elif game_field_positions[6] == player_dictionary[player_name]:
#         return game_field_positions[7]
#
#     elif game_field_positions[7] == player_dictionary[player_name]:
#         return game_field_positions[8]
#     elif game_field_positions[8] == player_dictionary[player_name]:
#         return game_field_positions[0]
#
#
#
#
#
#
#
#
#
#
# def Artificial_intelligence_occupy_position(selected_position, player_dictionary, ai_name):
#     game_field_positions[selected_position] = player_dictionary[ai_name]
#
#
# print(f"player: {game_field_positions}")
#
# ai_pos=Artificial_intelligence_selected_position(players_symbols,"player","ai")
#
#
# if check_ai_datatype(ai_pos):
#     Artificial_intelligence_occupy_position(ai_pos,players_symbols,"ai")
#     print(f"ai: {game_field_positions}")
# else:
#     print(ai_pos)
#     print(type(ai_pos))

# print(f"ai-ai-: {game_field_positions}")