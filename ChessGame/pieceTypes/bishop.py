from ChessGame.pieceTypes.piece import Piece


class Bishop(Piece):
    def __init__(self, piece_key, player):
        super(Bishop, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.find_bottom_right(loc))
        possible_moves.update(self.find_top_right(loc))
        possible_moves.update(self.find_bottom_left(loc))
        possible_moves.update(self.find_top_left(loc))
        return possible_moves

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
