from player import Player


class Game:
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.game_status = 'Introduction'

    def run(self):
        while self.game_status == 'Introduction':
            self.introduction()
        while self.game_status == True:
            self.turn()
        self.conclusion()

    def introduction(self):
        print("Welcome to Chess bass-ass")
        self.setPlayer1()
        self.setPlayer2()

    def turn(self):
        pass

    def conclusion(self):
        pass

    def availableMove(self):
        pass

    def movePiece(self):
        pass

    def getPlayer1(self):
        pass

    def setPlayer1(self):
        player_1_name = input('Player 1''s name:')
        self.player1 = Player(player_1_name)

    def getPlayer2(self):
        pass

    def setPlayer2(self):
        player_2_name = input('Player 2''s name:')
        self.player2 = Player(player_2_name)

    def getBoard(self):
        pass

    def setBoard(self):
        pass

    def getGameStatus(self):
        pass

    def setGameStatus(self):
        pass

game = Game()
game.run()