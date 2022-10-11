import pygame

class Ship:
    #Manages ship
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Start at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store decimal value for horizontal position
        self.x = float(self.rect.x)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #Update ship's position based on movement flag
        #Update ships value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.x += 1
            self.x += self.settings.ship_speed
            
        elif self.moving_left and self.rect.left > 0:
            #self.rect.x -= 1
            self.x -= self.settings.ship_speed
            
        #Update rect object from self.x
        self.rect.x = self.x
        
    def center_ship(self):
        #Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)