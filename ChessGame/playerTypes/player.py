
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

    def select_piece(self, previous_turn, **kwargs):
        try:
            if previous_turn['check_status']:
                print(f'{self.name}, your king is in check.')
            selected_piece = None
            while selected_piece is None:
                piece_name = input(f'{self.name}, what piece would you like to move?')
                piece_name = piece_name.upper()
                for piece in self.pieces:
                    if piece.short_hand_name == piece_name and piece.alive:
                        selected_piece = piece
                        break
                if selected_piece is None:
                    print(f'Invalid name')
            return selected_piece
        except Exception as e:
            print(f'function move within class player. Exception: {e}')

    def select_piece_new_location(self, selected_piece, possible_locations, **kwargs):
        valid_location = False
        while valid_location == False:
            selected_location = input(f'You selected {selected_piece.short_hand_name}, which of these locations will you move it to? {self.list_out_possible_locations(possible_locations)}')
            selected_location = selected_location.upper()
            for location in possible_locations:
                if location.name == selected_location:
                    valid_location = True
                    turn_type = possible_locations[location]
                    return location, turn_type
            print(f'invalid location, enter location again. possible locations: {self.list_out_possible_locations(possible_locations)}')

    def list_out_possible_locations(self, possible_locations, *args):
        locs = ''
        for location in possible_locations:
            name_formatted = f'|{location.name}|'
            locs += name_formatted
        return locs

    def promotion_selection(self, **kwargs):
        valid_entree = False
        while not valid_entree:
            piece_type = input(f'The pawn is promoted! What type would you like it promoted to? '
                               f'Queen, Rook, Bishop, Knight?').upper()
            if piece_type == 'QUEEN' or piece_type == 'ROOK' or piece_type == 'BISHOP' or piece_type == 'KNIGHT':
                return piece_type
            else:
                print('Invalid piece name')
