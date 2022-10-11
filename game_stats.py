class GameStats:
    #Track Stats
    
    def __init__(self, ai_game):
        #Initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start game with inactive stats
        self.game_active = False
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0