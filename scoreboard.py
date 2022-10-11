import pygame.font

class Scoreboard:
    #A class to report scoring information
    
    def __init__(self, ai_game):
        #initialize scorekeeping
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #Font settings for scoring information
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        #Prepare the initial score image
        self.prep_score()
        
    def prep_score(self):
        #Turn scoreboard into image
        rounded_score = round(self.stats.score, -1)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Display on top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right - 100
        self.score_rect.top = 100
        
    def show_score(self):
        #Draw score to sc reen
        self.screen.blit(self.score_image, self.score_rect)