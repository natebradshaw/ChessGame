
class Player:
    def __init__(self, key, name):
        self.player_key = key
        self.name = name
        self.pieces = []
        self.win_status = None

    def set_name(self, name):
        self.player_key += 1
        self.name = name

    def add_piece(self, piece):
        self.pieces.append(piece)

    def set_win_status(self, win_status):
        self.win_status = win_status

    def select_piece(self, previous_turn):
        try:
            selected_piece = None
            while selected_piece is None:
                piece_name = input(f'{self.name}, what piece would you like to move?')
                for piece in self.pieces:
                    if piece.short_hand_name == piece_name and piece.alive == True:
                        selected_piece = piece
                        break
                if selected_piece is None:
                    print(f'Invalid name')
            return selected_piece
        except Exception as e:
            print(f'function move within class player. Exception: {e}')

    def select_piece_new_location(self):
        loc = 'test'
        return loc