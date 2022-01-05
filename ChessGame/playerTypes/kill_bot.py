import random
from ChessGame.playerTypes.player import Player


class KillBot(Player):
    def __init__(self, key, name):
        super(KillBot, self).__init__(key, name)
        self.pieces_random_order = []
        self.previous_turn_copy = None
        self.current_turn_count = 0

    def select_piece(self, previous_turn, **kwargs):
        def make_selection():
            selected_piece = self.pieces_random_order[self.current_turn_count]
            self.current_turn_count += 1
            return selected_piece

        def next_turn():
            self.pieces_random_order = []
            self.previous_turn_copy = previous_turn
            self.current_turn_count = 0
            piece_count = 0
            for piece in self.pieces:
                if piece.alive:
                    piece_count += 1
                    self.pieces_random_order.append(piece)
            random.shuffle(self.pieces_random_order)

        def select_piece_main():
            if self.previous_turn_copy is None:
                self.previous_turn_copy = previous_turn
                next_turn()
                return make_selection()
            elif game_turn_count == self.current_turn_count: #same turn, iterate to next selection
                return make_selection()
            else:
                next_turn()
                return make_selection()

        game_turn_count = kwargs.pop('turn_count')
        var = select_piece_main()
        #print(var.short_hand_name)
        return var

    def select_piece_new_location(self, selected_piece, possible_locations, **kwargs):
        def random_selection():
            loc_total = len(possible_locations.keys())
            random_selection_key = random.randrange(0, loc_total)
            loc_list = []
            for loc in possible_locations:
                loc_list.append(loc)
            #print(f'{loc_list[random_selection_key].name}, {possible_locations[loc_list[random_selection_key]]}')
            return loc_list[random_selection_key], possible_locations[loc_list[random_selection_key]]

        for loc in possible_locations:
            if possible_locations[loc] == 'Kill':
                return loc, possible_locations[loc]
            elif possible_locations[loc] == 'Promotion':
                return loc, possible_locations[loc]
            elif possible_locations[loc] == 'EnPassant':
                return loc, possible_locations[loc]
            elif possible_locations[loc] == 'Castling':
                return loc, possible_locations[loc]
        return random_selection()


    def promotion_selection(self, **kwargs):
        key = random.randrange(0,4)
        piece_types = ['QUEEN', 'ROOK', 'BISHOP', 'KNIGHT']
        return piece_types[key]
