
class Player:
    def __init__(self, key, name):
        self.player_key = key
        self.name = name
        self.pieces = []

    def set_name(self, name):
        self.player_key += 1
        self.name = name

    def add_piece(self, piece):
        self.pieces.append(piece)

    def move(self, board):
        selected_piece = self.select_piece()
        possible_locations = selected_piece.find_possible_moves(board)#return list of locations
        self.select_piece_new_location(possible_locations)

    def select_piece(self):
        try:
            selected_piece = None
            while selected_piece is None:
                piece_name = input(f'{self.name}, what piece would you like to move?')
                for piece in self.pieces:
                    if piece.short_hand_name == piece_name:
                        selected_piece = piece
                if selected_piece is None:
                    print(f'Invalid name')
            return selected_piece
        except Exception as e:
            print(f'function move within class player. Exception: {e}')

    def select_piece_new_location(self):
        pass