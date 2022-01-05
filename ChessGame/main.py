from ChessGame.game import Game
for i in range(0, 30):
    key = i % 2
    if key == 0:
        bot_1 = 'RANDBOT'
        bot_2 = 'KILLBOT'
    if key == 0:
        bot_1 = 'KILLBOT'
        bot_2 = 'RANDBOT'
    game = Game(bot_game=True, player_1_bot_type=bot_1, player_2_bot_type=bot_2)
    #game = Game()
    game.run()
