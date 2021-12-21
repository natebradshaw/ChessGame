from ChessGame.pieceTypes.piece import Piece


class King(Piece):

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.find_bottom_right(loc))
        possible_moves.update(self.find_bottom_center(loc))
        possible_moves.update(self.find_bottom_left(loc))
        possible_moves.update(self.find_mid_right(loc))
        possible_moves.update(self.find_mid_left(loc))
        possible_moves.update(self.find_top_right(loc))
        possible_moves.update(self.find_top_center(loc))
        possible_moves.update(self.find_top_left(loc))
        filtered_possible_moves = self.filter_possible_moves(possible_moves)
        return filtered_possible_moves

    def is_check(self):
        pass

    def filter_possible_moves(self, possible_moves):
        return possible_moves

    def find_bottom_right(self, loc):
        bottom_right = {}
        if loc.bot_rght_loc is None:
            return bottom_right
        elif loc.bot_rght_loc.current_piece is None:
            bottom_right[loc.bot_rght_loc] = 'StandardMove'
            return bottom_right
        elif loc.bot_rght_loc.current_piece.owner == self.owner:
            return bottom_right
        elif loc.bot_rght_loc.current_piece.owner != self.owner:
            bottom_right[loc.bot_rght_loc] = 'Kill'
            return bottom_right

    def find_bottom_center(self, loc):
        bottom_center = {}
        if loc.bot_cent_loc is None:
            return bottom_center
        elif loc.bot_cent_loc.current_piece is None:
            bottom_center[loc.bot_cent_loc] = 'StandardMove'
            return bottom_center
        elif loc.bot_cent_loc.current_piece.owner == self.owner:
            return bottom_center
        elif loc.bot_cent_loc.current_piece.owner != self.owner:
            bottom_center[loc.bot_cent_loc] = 'Kill'
            return bottom_center

    def find_bottom_left(self, loc):
        bottom_left = {}
        if loc.bot_left_loc is None:
            return bottom_left
        elif loc.bot_left_loc.current_piece is None:
            bottom_left[loc.bot_left_loc] = 'StandardMove'
            return bottom_left
        elif loc.bot_left_loc.current_piece.owner == self.owner:
            return bottom_left
        elif loc.bot_left_loc.current_piece.owner != self.owner:
            bottom_left[loc.bot_left_loc] = 'Kill'
            return bottom_left

    def find_mid_right(self, loc):
        mid_right = {}
        if loc.mid_rght_loc is None:
            return mid_right
        elif loc.mid_rght_loc.current_piece is None:
            mid_right[loc.mid_rght_loc] = 'StandardMove'
            return mid_right
        elif loc.mid_rght_loc.current_piece.owner == self.owner:
            return mid_right
        elif loc.mid_rght_loc.current_piece.owner != self.owner:
            mid_right[loc.mid_rght_loc] = 'Kill'
            return mid_right

    def find_mid_left(self, loc):
        mid_left = {}
        if loc.mid_left_loc is None:
            return mid_left
        elif loc.mid_left_loc.current_piece is None:
            mid_left[loc.mid_left_loc] = 'StandardMove'
            return mid_left
        elif loc.mid_left_loc.current_piece.owner == self.owner:
            return mid_left
        elif loc.mid_left_loc.current_piece.owner != self.owner:
            mid_left[loc.mid_left_loc] = 'Kill'
            return mid_left

    def find_top_right(self, loc):
        top_right = {}
        if loc.top_rght_loc is None:
            return top_right
        elif loc.top_rght_loc.current_piece is None:
            top_right[loc.top_rght_loc] = 'StandardMove'
            return top_right
        elif loc.top_rght_loc.current_piece.owner == self.owner:
            return top_right
        elif loc.top_rght_loc.current_piece.owner != self.owner:
            top_right[loc.top_rght_loc] = 'Kill'
            return top_right

    def find_top_center(self, loc):
        top_center = {}
        if loc.top_cent_loc is None:
            return top_center
        elif loc.top_cent_loc.current_piece is None:
            top_center[loc.top_cent_loc] = 'StandardMove'
            return top_center
        elif loc.top_cent_loc.current_piece.owner == self.owner:
            return top_center
        elif loc.top_cent_loc.current_piece.owner != self.owner:
            top_center[loc.top_cent_loc] = 'Kill'
            return top_center

    def find_top_left(self, loc):
        top_left = {}
        if loc.top_left_loc is None:
            return top_left
        elif loc.top_left_loc.current_piece is None:
            top_left[loc.top_left_loc] = 'StandardMove'
            return top_left
        elif loc.top_left_loc.current_piece.owner == self.owner:
            return top_left
        elif loc.top_left_loc.current_piece.owner != self.owner:
            top_left[loc.top_left_loc] = 'Kill'
            return top_left


