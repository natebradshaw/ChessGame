
from ChessGame.player import Player
from ChessGame.pieceTypes.piece import Piece
from ChessGame.board import Board
from ChessGame.config import possible_piece_types
from ChessGame.config2 import players_pieces_map


class Game:
    def __init__(self):
        self.board = self.setBoard()
        self.players = {'1': None, '2': None}
        self.game_status = 'Introduction'
        self.winner = None
        self.loser = None

    def run(self):
        self.introduction()
        while self.winner is None:
            self.turn()
        self.conclusion()

    def introduction(self):
        print("Welcome to Chess")
        for player_count in self.players:
            player = self.setPlayer(int(player_count))
            self.players[player_count] = player
        self.game_status = 'Player1'

    def turn(self):
        self.board.present_board() #Present the user the board
        current_player = self.players[self.game_status] #Player makes a move
        #current_player
        self.next_player()

    def set_players_pieces(self, player):
        for piece_key in players_pieces_map:
            piece_type = players_pieces_map[piece_key]
            for item in possible_piece_types:
                if item['name'] == piece_type:
                    class_sub_type = item['cls']
                    piece = class_sub_type(piece_key, player)
                    piece.set_starting_position(self.board)
                    player.add_piece(piece)
                    #self.set_initial_piece_location(piece)

    def inital_piece_placement(self):
        pass

    # def set_piece_type(self, piece_type):
    #     for item in possible_piece_types:
    #         if item['name'] == piece_type:
    #             piece = item['cls']
    #             return piece

    def next_player(self):
        if self.game_status == 'Player1':
            self.game_status = 'Player2'
        else:
            self.game_status = 'Player2'

    def setPlayer(self, player_count):
        player_name = input(f'Player {player_count}, what is your name?')
        player = Player(player_count, player_name)
        self.set_players_pieces(player)
        return player

    def setBoard(self):
        board = Board()
        return board

    def set_initial_piece_location(self, piece):
        pass
    #run some loop on the location piece map and write the answers only in the location

    def conclusion(self):
        pass




