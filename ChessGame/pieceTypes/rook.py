from ChessGame.pieceTypes.piece import Piece


class Rook(Piece):
    def __init__(self, piece_key, player):
        super(Rook, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.find_bottom(loc))
        possible_moves.update(self.find_top(loc))
        possible_moves.update(self.find_left(loc))
        possible_moves.update(self.find_right(loc))
        return possible_moves

    def find_bottom(self, loc):
        bottom_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_cent_loc is None: #no location
                limit_found = True
            elif loc.bot_cent_loc.current_piece is not None and loc.bot_cent_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.bot_cent_loc.current_piece is not None and loc.bot_cent_loc.current_piece.owner != self.owner: #apponant piece blocking path
                bottom_moves[loc.bot_cent_loc] = 'Kill'
                limit_found = True
            elif loc.bot_cent_loc.current_piece is None: #Empty location
                bottom_moves[loc.bot_cent_loc] = 'StandardMove'
                loc = loc.bot_cent_loc
        return bottom_moves

    def find_top(self, loc):
        top_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_cent_loc is None: #no location
                limit_found = True
            elif loc.top_cent_loc.current_piece is not None and loc.top_cent_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.top_cent_loc.current_piece is not None and loc.top_cent_loc.current_piece.owner != self.owner: #apponant piece blocking path
                top_moves[loc.top_cent_loc] = 'Kill'
                limit_found = True
            elif loc.top_cent_loc.current_piece is None: #Empty location
                top_moves[loc.top_cent_loc] = 'StandardMove'
                loc = loc.top_cent_loc
        return top_moves

    def find_left(self, loc):
        left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_left_loc is None: #no location
                limit_found = True
            elif loc.mid_left_loc.current_piece is not None and loc.mid_left_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.mid_left_loc.current_piece is not None and loc.mid_left_loc.current_piece.owner != self.owner: #apponant piece blocking path
                left_moves[loc.mid_left_loc] = 'Kill'
                limit_found = True
            elif loc.mid_left_loc.current_piece is None: #Empty location
                left_moves[loc.mid_left_loc] = 'StandardMove'
                loc = loc.mid_left_loc
        return left_moves

    def find_right(self, loc):
        right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_rght_loc is None: #no location
                limit_found = True
            elif loc.mid_rght_loc.current_piece is not None and loc.mid_rght_loc.current_piece.owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.mid_rght_loc.current_piece is not None and loc.mid_rght_loc.current_piece.owner != self.owner: #apponant piece blocking path
                right_moves[loc.mid_rght_loc] = 'Kill'
                limit_found = True
            elif loc.mid_rght_loc.current_piece is None: #Empty location
                right_moves[loc.mid_rght_loc] = 'StandardMove'
                loc = loc.mid_rght_loc
        return right_moves
