from ChessGame.pieceTypes.piece import Piece


class King(Piece):
    def __init__(self, piece_key, player):
        super(King, self).__init__(piece_key, player)

        self.paired_4_rook_old_loc = None #will hold location type
        self.paired_4_rook_new_loc = None  # will hold location type
        self.castling_4_king_loc = None

        self.paired_3_rook_old_loc = None #will hold location type
        self.paired_3_rook_new_loc = None  # will hold location type
        self.castling_3_king_loc = None

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
        if self.moved_status == False:
            space_3_status = self.castling_3_space(loc)
            if space_3_status == True:
                possible_moves[self.castling_3_king_loc] = 'Castling'
            space_4_status = self.castling_4_space(loc)
            if space_4_status == True:
                possible_moves[self.castling_4_king_loc] = 'Castling'
        return possible_moves

    def is_check(self):
        pass

    def castling_3_space(self, loc):

        if loc.mid_rght_loc.current_piece is None:
            rook_validated_loc = loc.mid_rght_loc
            if rook_validated_loc.mid_rght_loc.current_piece is None:
                king_validated_loc = rook_validated_loc.mid_rght_loc
                if king_validated_loc.mid_rght_loc.current_piece is not None \
                        and king_validated_loc.mid_rght_loc.current_piece.key.__contains__('rook') \
                        and king_validated_loc.mid_rght_loc.current_piece.moved_status == False:#this line checks for the rook in the right location
                    self.paired_3_rook_new_loc = rook_validated_loc
                    self.paired_3_rook_old_loc = king_validated_loc.mid_rght_loc
                    self.castling_3_king_loc = king_validated_loc
                    return True

        elif loc.mid_left_loc.current_piece is None:
            rook_validated_loc = loc.mid_left_loc
            if rook_validated_loc.mid_left_loc.current_piece is None:
                king_validated_loc = rook_validated_loc.mid_left_loc
                if king_validated_loc.mid_left_loc.current_piece is not None  \
                        and king_validated_loc.mid_left_loc.current_piece.key.__contains__('rook') \
                        and king_validated_loc.mid_left_loc.current_piece.moved_status == False:#this line checks for the rook in the right location
                    self.paired_3_rook_new_loc = rook_validated_loc
                    self.paired_3_rook_old_loc = king_validated_loc.mid_left_loc
                    self.castling_3_king_loc = king_validated_loc
                    return True

    def castling_4_space(self, loc):

        if loc.mid_rght_loc.current_piece is None:
            rook_validated_loc = loc.mid_rght_loc
            if rook_validated_loc.mid_rght_loc.current_piece is None:
                king_validated_loc = rook_validated_loc.mid_rght_loc
                if king_validated_loc.mid_rght_loc.current_piece is None \
                    and king_validated_loc.mid_rght_loc.mid_rght_loc is not None \
                    and king_validated_loc.mid_rght_loc.mid_rght_loc.current_piece is not None \
                    and king_validated_loc.mid_rght_loc.mid_rght_loc.current_piece.key.__contains__('rook') \
                    and king_validated_loc.mid_rght_loc.mid_rght_loc.current_piece.moved_status == False:
                        self.paired_4_rook_new_loc = rook_validated_loc
                        self.paired_4_rook_old_loc = king_validated_loc.mid_rght_loc.mid_rght_loc
                        self.castling_4_king_loc = king_validated_loc
                        return True

        elif loc.mid_left_loc.current_piece is None:
            rook_validated_loc = loc.mid_left_loc
            if rook_validated_loc.mid_left_loc.current_piece is None:
                king_validated_loc = rook_validated_loc.mid_left_loc
                if king_validated_loc.mid_left_loc.current_piece is None \
                        and king_validated_loc.mid_left_loc.mid_left_loc is not None \
                        and king_validated_loc.mid_left_loc.mid_left_loc.current_piece is not None \
                        and king_validated_loc.mid_left_loc.mid_left_loc.current_piece.key.__contains__('rook') \
                        and king_validated_loc.mid_left_loc.mid_left_loc.current_piece.moved_status == False:
                    self.paired_4_rook_new_loc = rook_validated_loc
                    self.paired_4_rook_old_loc = king_validated_loc.mid_left_loc.mid_left_loc
                    self.castling_4_king_loc = king_validated_loc
                    return True


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


