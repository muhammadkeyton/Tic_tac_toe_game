class GameBrain:
    def __init__(self, positions):
        self.positions = positions
        self.ai_chosen_position = 0

    def if_datatype_same(self,chosen_position):
        if chosen_position in self.positions:
            return True
        else:
            return False

    def check_ai_datatype(self,chosen_position):
        if type(chosen_position) == int:
            return True
        else:
            return False


    def player_win_check(self, player_dictionary, player_name):
        if self.positions[0] == player_dictionary[player_name] and self.positions[1] == player_dictionary[player_name] \
                and self.positions[2] == player_dictionary[player_name]:
            return True
        elif self.positions[3] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]\
                and self.positions[5] == player_dictionary[player_name]:
            return True
        elif self.positions[6] == player_dictionary[player_name] and self.positions[7] == player_dictionary[player_name]\
                and self.positions[8] == player_dictionary[player_name]:
            return True
        elif self.positions[0] == player_dictionary[player_name] and self.positions[3] == player_dictionary[player_name]\
                and self.positions[6] == player_dictionary[player_name]:
            return True
        elif self.positions[1] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]\
                and self.positions[7] == player_dictionary[player_name]:
            return True
        elif self.positions[2] == player_dictionary[player_name] and self.positions[5] == player_dictionary[player_name]\
                and self.positions[8] == player_dictionary[player_name]:
            return True

        elif self.positions[0] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]\
                and self.positions[8] == player_dictionary[player_name]:
            return True

        elif self.positions[2] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]\
                and self.positions[6] == player_dictionary[player_name]:
            return True
        else:
            return False

    def Artificial_intelligence_selected_position(self,player_dictionary, player_name,ai_name):
        # -------------------------------------verticals-----------------------------------------------------------------------------------
        # verticals one
        if self.positions[0] == player_dictionary[player_name] and self.positions[3] == player_dictionary[player_name]:
            return self.positions[6]

        if self.positions[3] == player_dictionary[player_name] and self.positions[6] == player_dictionary[player_name]:
            return self.positions[0]

        # verticals two
        if self.positions[1] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]:
            return self.positions[7]
        if self.positions[4] == player_dictionary[player_name] and self.positions[7] == player_dictionary[player_name]:
            return self.positions[1]

        # verticals three
        if self.positions[2] == player_dictionary[player_name] and self.positions[5] == player_dictionary[player_name]:
            return self.positions[8]
        if self.positions[5] == player_dictionary[player_name] and self.positions[8] == player_dictionary[player_name]:
            return self.positions[2]
        # ----------------------------------------------horizontals-------------------------------------------------------------------------------------
        # horizontal one important
        if self.positions[0] == player_dictionary[player_name] and self.positions[1] == player_dictionary[ai_name] and self.positions[2] == player_dictionary[player_name]:
            return self.positions[3]
        if self.positions[1] == player_dictionary[player_name] and self.positions[2] == player_dictionary[player_name] and self.positions[0] == player_dictionary[ai_name]:
            return self.positions[3]
        if self.positions[1] == player_dictionary[ai_name] and self.positions[2] == player_dictionary[player_name] and self.positions[0] == player_dictionary[player_name]:
            return self.positions[3]
        
        # horizontal one
        if self.positions[0] == player_dictionary[player_name] and self.positions[1] == player_dictionary[player_name]:
            return self.positions[2]
        if self.positions[1] == player_dictionary[player_name] and self.positions[2] == player_dictionary[player_name]:
            return self.positions[0]


        #horizontal two important
        if self.positions[3] == player_dictionary[player_name] and self.positions[4] == player_dictionary[ai_name] and self.positions[5] == player_dictionary[player_name]:
            return self.positions[6]
        if self.positions[3] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name] and self.positions[5] == player_dictionary[ai_name]:
            return self.positions[6]
        if self.positions[3] == player_dictionary[ai_name] and self.positions[4] == player_dictionary[player_name] and self.positions[5] == player_dictionary[player_name]:
            return self.positions[6]
        
        # horizontal two
        if self.positions[3] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]:
            return self.positions[5]
        if self.positions[4] == player_dictionary[player_name] and self.positions[5] == player_dictionary[player_name]:
            return self.positions[3]


        #horizontal three important
        if self.positions[6] == player_dictionary[player_name] and self.positions[7] == player_dictionary[ai_name] and self.positions[8] == player_dictionary[player_name]:
            return self.positions[0]
        if self.positions[6] == player_dictionary[player_name] and self.positions[7] == player_dictionary[player_name] and self.positions[8] == player_dictionary[ai_name]:
            return self.positions[0]
        if self.positions[6] == player_dictionary[ai_name] and self.positions[7] == player_dictionary[player_name] and self.positions[8] == player_dictionary[player_name]:
            return self.positions[0]
        
        
        # horizontal three
        if self.positions[6] == player_dictionary[player_name] and self.positions[7] == player_dictionary[player_name]:
            return self.positions[8]
        if self.positions[7] == player_dictionary[player_name] and self.positions[8] == player_dictionary[player_name]:
            return self.positions[6]
        # ----------------------------------------------diagnols----------------------------------------------------------------------------

        # diagnol 1
        if self.positions[0] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]:
            return self.positions[8]
        if self.positions[4] == player_dictionary[player_name] and self.positions[8] == player_dictionary[player_name]:
            return self.positions[0]

        # diagnol 2
        if self.positions[2] == player_dictionary[player_name] and self.positions[4] == player_dictionary[player_name]:
            return self.positions[6]
        if self.positions[4] == player_dictionary[player_name] and self.positions[6] == player_dictionary[player_name]:
            return self.positions[2]

        #  X O X ,O X O, X O X  style
        if self.positions[0] == player_dictionary[player_name]:
            return self.positions[1]

        if self.positions[1] == player_dictionary[player_name]:
            return self.positions[2]

        if self.positions[2] == player_dictionary[player_name]:
            return self.positions[3]

        if self.positions[3] == player_dictionary[player_name]:
            return self.positions[4]

        if self.positions[4] == player_dictionary[player_name]:
            return self.positions[5]

        if self.positions[5] == player_dictionary[player_name]:
            return self.positions[6]

        if self.positions[6] == player_dictionary[player_name]:
            return self.positions[7]

        if self.positions[7] == player_dictionary[player_name]:
            return self.positions[8]
        if self.positions[8] == player_dictionary[player_name]:
            return self.positions[0]


    def Artificial_intelligence_occupy_position(self,selected_position,player_dictionary,ai_name):
        self.positions[selected_position] = player_dictionary[ai_name]







