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
        possible_moves = self.king_standard_moves(loc, previous_turn)
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

    def validate_check_mate(self, king_loc, previous_turn, board):
        possible_moves = self.find_possible_moves(king_loc, previous_turn)
        for move in possible_moves:
            hypothetical_threat = self.hypothetical_threat_move(king_loc, previous_turn, move, king_loc, board)
            if not hypothetical_threat:
                return False
        for row in range(1, 9):
            for column in board.structure:
                test_loc = board.structure[column][str(row)]
                if test_loc.current_piece is not None and test_loc.current_piece.owner == self.owner:
                    test_loc_possible_moves = test_loc.current_piece.find_possible_moves(loc=test_loc, previous_turn=previous_turn)
                    for move in test_loc_possible_moves:
                        hypothetical_threat = self.hypothetical_threat_move(test_loc, previous_turn, move, king_loc, board)
                        if not hypothetical_threat:
                            return False
        return True


