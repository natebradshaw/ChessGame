from ChessGame.config2 import players_pieces_location_map
import abc

class Piece(object):#object OR abc.ABC
    def __init__(self, key, player):
        self.key = key
        self.initial_location = None
        self.short_hand_name = f'{player.player_key}{self.key[0].upper()}{self.key[-1].upper()}'
        self.owner = player
        self.alive = True

#consider initiallizing from the child class.. maybe it'd work
    # def set_piece_type(self, piece_type):
    #     for item in possible_piece_types:
    #         if item['name'] == piece_type:
    #             piece = item['cls']
    #             return piece

    def set_starting_position(self, board):
        column = players_pieces_location_map[self.key]
        if self.owner.player_key == 1:
            row = '8'
        else:
            row = '1'
        loc = board.structure[column][row]
        loc.add_piece(self)
        self.initial_location = loc
        return loc

    def set_location(self, location):
        self.location = location

    def set_dead(self):
        self.alive = False

    @abc.abstractmethod
    def find_possible_moves(self):
        "Finds possible move"

    def find_loc(self, board):
        for column in range(1, 9):
            for row in range(1, 9):
                column_key = str(column)
                row_key = str(row)
                if board.structure[column_key][row_key].current_piece == self:
                    return board.structure[column_key][row_key]


