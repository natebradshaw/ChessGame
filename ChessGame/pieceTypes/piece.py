from ChessGame.config2 import players_pieces_location_map
import abc

class Piece(object):#object OR abc.ABC
    count = 0
    def __init__(self, key, player):
        Piece.count += 1
        self.key = key
        self.initial_location = None
        self.owner = player
        self.alive = True
        self.short_hand_name = f'{player.player_key}{self.key[0].upper()}{self.piece_origin()}'
        self.moved_status = False

#consider initiallizing from the child class.. maybe it'd work
    # def set_piece_type(self, piece_type):
    #     for item in possible_piece_types:
    #         if item['name'] == piece_type:
    #             piece = item['cls']
    #             return piece
    def piece_origin(self):
        if Piece.count <= 32:
            return self.key[-1].upper()
        else:
            pieces = self.owner.pieces
            player_piece_count = len(pieces)
            key = player_piece_count - 13
            return key

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

    def find_bottom(self, loc):
        bottom_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_cent_loc is None:  # no location
                limit_found = True
            elif loc.bot_cent_loc.current_piece is not None and loc.bot_cent_loc.current_piece.owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.bot_cent_loc.current_piece is not None and loc.bot_cent_loc.current_piece.owner != self.owner:  # apponant piece blocking path
                bottom_moves[loc.bot_cent_loc] = 'Kill'
                limit_found = True
            elif loc.bot_cent_loc.current_piece is None:  # Empty location
                bottom_moves[loc.bot_cent_loc] = 'StandardMove'
                loc = loc.bot_cent_loc
        return bottom_moves

    def find_top(self, loc):
        top_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_cent_loc is None:  # no location
                limit_found = True
            elif loc.top_cent_loc.current_piece is not None and loc.top_cent_loc.current_piece.owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.top_cent_loc.current_piece is not None and loc.top_cent_loc.current_piece.owner != self.owner:  # apponant piece blocking path
                top_moves[loc.top_cent_loc] = 'Kill'
                limit_found = True
            elif loc.top_cent_loc.current_piece is None:  # Empty location
                top_moves[loc.top_cent_loc] = 'StandardMove'
                loc = loc.top_cent_loc
        return top_moves

    def find_left(self, loc):
        left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_left_loc is None:  # no location
                limit_found = True
            elif loc.mid_left_loc.current_piece is not None and loc.mid_left_loc.current_piece.owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.mid_left_loc.current_piece is not None and loc.mid_left_loc.current_piece.owner != self.owner:  # apponant piece blocking path
                left_moves[loc.mid_left_loc] = 'Kill'
                limit_found = True
            elif loc.mid_left_loc.current_piece is None:  # Empty location
                left_moves[loc.mid_left_loc] = 'StandardMove'
                loc = loc.mid_left_loc
        return left_moves

    def find_right(self, loc):
        right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_rght_loc is None:  # no location
                limit_found = True
            elif loc.mid_rght_loc.current_piece is not None and loc.mid_rght_loc.current_piece.owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.mid_rght_loc.current_piece is not None and loc.mid_rght_loc.current_piece.owner != self.owner:  # apponant piece blocking path
                right_moves[loc.mid_rght_loc] = 'Kill'
                limit_found = True
            elif loc.mid_rght_loc.current_piece is None:  # Empty location
                right_moves[loc.mid_rght_loc] = 'StandardMove'
                loc = loc.mid_rght_loc
        return right_moves

    def find_bottom_right(self, loc):
        bottom_right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_rght_loc is None: #no location
                limit_found = True
            elif loc.bot_rght_loc.current_piece is not None and loc.bot_rght_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.bot_rght_loc.current_piece is not None and loc.bot_rght_loc.current_piece.owner != self.owner: #apponant piece blocking path
                bottom_right_moves[loc.bot_rght_loc] = 'Kill'
                limit_found = True
            elif loc.bot_rght_loc.current_piece is None: #Empty location
                bottom_right_moves[loc.bot_rght_loc] = 'StandardMove'
                loc = loc.bot_rght_loc
        return bottom_right_moves

    def find_top_right(self, loc):
        top_right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_rght_loc is None: #no location
                limit_found = True
            elif loc.top_rght_loc.current_piece is not None and loc.top_rght_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.top_rght_loc.current_piece is not None and loc.top_rght_loc.current_piece.owner != self.owner: #apponant piece blocking path
                top_right_moves[loc.top_rght_loc] = 'Kill'
                limit_found = True
            elif loc.top_rght_loc.current_piece is None: #Empty location
                top_right_moves[loc.top_rght_loc] = 'StandardMove'
                loc = loc.top_rght_loc
        return top_right_moves

    def find_bottom_left(self, loc):
        bottom_left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_left_loc is None: #no location
                limit_found = True
            elif loc.bot_left_loc.current_piece is not None and loc.bot_left_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.bot_left_loc.current_piece is not None and loc.bot_left_loc.current_piece.owner != self.owner: #apponant piece blocking path
                bottom_left_moves[loc.bot_left_loc] = 'Kill'
                limit_found = True
            elif loc.bot_left_loc.current_piece is None: #Empty location
                bottom_left_moves[loc.bot_left_loc] = 'StandardMove'
                loc = loc.bot_left_loc
        return bottom_left_moves

    def find_top_left(self, loc):
        top_left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_left_loc is None: #no location
                limit_found = True
            elif loc.top_left_loc.current_piece is not None and loc.top_left_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.top_left_loc.current_piece is not None and loc.top_left_loc.current_piece.owner != self.owner: #apponant piece blocking path
                top_left_moves[loc.top_left_loc] = 'Kill'
                limit_found = True
            elif loc.top_left_loc.current_piece is None: #Empty location
                top_left_moves[loc.top_left_loc] = 'StandardMove'
                loc = loc.top_left_loc
        return top_left_moves



